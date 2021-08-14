import os
from configparser import ConfigParser, ExtendedInterpolation
from helper.exception import AutomationError


def load_resources():
    load_app_config()
    load_locators()


def load_app_config():
    try:
        config = ConfigParser(interpolation=ExtendedInterpolation())
        config.read('resources/application.ini')

        for each_section in config.sections():
            for each_key, each_val in config.items(each_section):
                os.environ[each_key] = each_val

    except Exception as e:
        raise SystemExit(1)


def load_locators():
    if 'platform' in os.environ:
        platform = os.getenv('platform')
    else:
        raise AutomationError('Please add `platform` value in application.ini file')

    try:
        config = ConfigParser(interpolation=ExtendedInterpolation())
        config.read('resources/locators/{platform}/locators.ini'.format(platform=platform))

        for each_section in config.sections():
            for each_key, each_val in config.items(each_section):
                os.environ[each_key] = each_val

    except Exception as e:
        raise SystemExit(1)
