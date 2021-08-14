import json
import os
from configparser import ConfigParser, ExtendedInterpolation
from os.path import basename

BEHAVE_JSON = "results.json"
RESULT_DIRECTORY = "logs/results"
EXPECTED_JSON = RESULT_DIRECTORY + "/cucumber_output.json"


def behave_to_cucumber():
    _create_directory()
    converted = convert_json_file()
    with open(EXPECTED_JSON, "w") as cucumber_report_file:
        json.dump(converted, cucumber_report_file)


def _create_directory():
    if not os.path.exists(RESULT_DIRECTORY):
        os.makedirs(RESULT_DIRECTORY)
    return RESULT_DIRECTORY


def convert_json_file():
    with open(BEHAVE_JSON) as f:
        return convert(json.load(f))


def convert(json_file):
    json_nodes = ['feature', 'elements', 'steps']

    fields_not_exist_in_cucumber_json = ['status', 'step_type']

    def format_level(tree, index=0, id_counter=0, scenario_name=""):

        for item in tree:
            # Location in behave json translates to uri and line in cucumber json
            location = item.pop("location")
            uri = ':'.join(location.split(":")[:-1])
            line_number = ':'.join(location.split(":")[-1:])

            item["line"] = int(line_number)
            for field in fields_not_exist_in_cucumber_json:
                if field in item:
                    item.pop(field)

                if "Scenario" in item['keyword']:
                    log_details = get_log(uri, item['name'])
                    item['comments'] = log_details

            if json_nodes[index] == 'steps':
                if 'result' in item:
                    # Because several problems with long error messages the message sub-stringed to maximum 2000 chars.
                    if 'duration' in item["result"]:
                        item["result"]["duration"] = int(float(item["result"]["duration"]) * 1000)

                    if 'error_message' in item["result"]:
                        error_msg = item["result"].pop('error_message')
                        error_msg = '\n'.join(str(x) for x in error_msg)
                        item["result"]["error_message"] = str(error_msg).replace("\"", "").replace("\\'", "")

                        image_data = get_image_data(uri, scenario_name, line_number)
                        screen_shot_data = {"data": str(image_data)[2:-1], "mime_type": "image/png"}
                        embeddings = [screen_shot_data]
                        item["embeddings"] = embeddings
                else:
                    # In behave, skipped tests doesn't have result object in their json, there-fore when we generating
                    # Cucumber report for every skipped test we need to generated a new result with status skipped
                    item["result"] = {"status": "skipped", "duration": 0}

                if 'table' in item:
                    item['rows'] = []
                    t_line = 1
                    item['rows'].append({"cells": item['table']['headings'], "line": item["line"] + t_line})
                    for table_row in item['table']['rows']:
                        t_line += 1
                        item['rows'].append({"cells": table_row, "line": item["line"] + t_line})
            else:
                # uri is the name of the feature file the current item located
                item["uri"] = uri
                item["description"] = ""
                item["id"] = id_counter
                id_counter += 1
            # If the scope is not "steps" proceed with the recursion
            if index != 2 and json_nodes[index + 1] in item:
                item[json_nodes[index + 1]] = format_level(
                    item[json_nodes[index + 1]], index + 1, id_counter=id_counter, scenario_name=item['name']
                )
        return tree

    return format_level(json_file)


def get_image_data(feature_filename, scenario_name, screenshot_name):
    basename(feature_filename)

    logger_config_data = ConfigParser(interpolation=ExtendedInterpolation())
    logger_config_data.read("resources/logger_config.ini")
    logger_config = logger_config_data[logger_config_data.default_section]

    log_base_path = logger_config["base_path"]
    log_file_dir = log_base_path + "/" + os.path.splitext(basename(feature_filename))[0] + "/" + scenario_name.replace(
        " ", "_")

    screen_shot_path = log_file_dir + "/feature" + screenshot_name + ".png"

    import base64
    if os.path.exists(screen_shot_path):
        with open(screen_shot_path, "rb") as image_file:
            return base64.b64encode(image_file.read())


def get_log(feature_filename, scenario_name):
    try:
        basename(feature_filename)

        logger_config_data = ConfigParser(interpolation=ExtendedInterpolation())
        logger_config_data.read("resources/logger_config.ini")
        logger_config = logger_config_data[logger_config_data.default_section]

        log_base_path = logger_config["base_path"]
        log_file_dir = log_base_path + "/" + os.path.splitext(basename(feature_filename))[
            0] + "/" + scenario_name.replace(
            " ", "_")
        log_details = log_file_dir + "/feature.log"
        if os.path.exists(log_details):
            with open(log_details, 'r') as log_file:
                data = log_file.read()
                log_file.close()
            return [{"line": 1, "value": data}]
        else:
            return [{"line": 1, "value": 'Log file not available'}]
    except Exception as e:
        print('get_log:' + str(e.__dict__))


def main():
    behave_to_cucumber()
