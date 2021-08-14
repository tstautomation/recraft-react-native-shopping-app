from configparser import ConfigParser, ExtendedInterpolation
from os.path import basename
import os
import shutil
from core.constant import LOG_DIRECTORY, BEFORE_SCENARIO
from helper.logger import Logger


def log_dir():
    parser = ConfigParser(interpolation=ExtendedInterpolation())
    parser.read("resources/logger_config.ini")
    logger_config = parser[parser.default_section]
    return logger_config['base_path']


def initialize_common_logger():
    if not os.path.exists(log_dir()):
        os.mkdir(log_dir())
    return Logger("{log_dir}/execution.log".format(log_dir=log_dir()), logger_key="[AUTOMATION]")


def initialize_scenario_logger(scenario):
    feature_filename = scenario.filename
    feature_filename = feature_filename.replace("'", "")
    basename(feature_filename)

    log_base_path = log_dir()
    log_file_dir = os.path.join(log_base_path, os.path.splitext(basename(feature_filename))[0])
    if not os.path.exists(log_file_dir):
        os.mkdir(log_file_dir)

    log_file_dir = os.path.join(log_file_dir, str(scenario.name).replace(" ", "_"))
    if os.path.exists(log_file_dir):
        shutil.rmtree(log_file_dir)
    os.mkdir(log_file_dir)
    os.environ[LOG_DIRECTORY] = log_file_dir
    log_file_path = os.path.join(log_file_dir, "feature.log")
    Logger(log_file_path)
    Logger.log(BEFORE_SCENARIO.format(scenario.name))
