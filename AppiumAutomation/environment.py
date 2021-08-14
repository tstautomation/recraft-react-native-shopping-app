import os

from core.constant import BASE_PATH, AFTER_STEP
from core.logger_manager import initialize_scenario_logger, initialize_common_logger
from core.resource_manager import load_resources
from helper.logger import Logger


def before_all(context):
    os.environ[BASE_PATH] = os.getcwd()
    initialize_common_logger()
    load_resources()


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    initialize_scenario_logger(scenario)


def before_step(context, step):
    pass


def after_step(context, step):
    try:
        if isinstance(step.status, str):
            status = str(step.status).upper()
        else:
            status = str(step.status.name).upper()
        Logger.info(AFTER_STEP.format(status, step.name))
        if status != "PASSED":
            Logger.save_screen_shot(str(step.line))
    except Exception as e:
        print("Error in after_step: %s" % str(e))


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    pass


def after_all(context):
    pass
