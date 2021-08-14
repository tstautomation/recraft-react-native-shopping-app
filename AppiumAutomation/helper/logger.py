import logging.config
from configparser import ConfigParser, ExtendedInterpolation
import sys
import os
from core.driver_manager import DriverFactory


class Logger(object):
    logger = None
    log_path = None

    def __init__(self, log_path, logger_key="[TEST_CASE]]"):
        Logger.log_path = log_path

        logger_config_data = ConfigParser(interpolation=ExtendedInterpolation())
        logger_config_data.read("resources/logger_config.ini")
        self.logger_config = logger_config_data[logger_config_data.default_section]

        self.streaming_handler = logging.StreamHandler(sys.stdout)
        self.file_handler = self.get_handler(Logger.log_path)

        logger = logging.getLogger(logger_key)
        logger.addHandler(self.file_handler)
        logger.addHandler(self.streaming_handler)
        logger.setLevel(self.logger_config["level"])

        Logger.logger = logger

    def get_handler(self, log_file_path):
        file_handler = logging.FileHandler(log_file_path, mode=self.logger_config["mode"])
        formatter = logging.Formatter(self.logger_config["format"])
        file_handler.setFormatter(formatter)
        return file_handler

    def remove_handler(self):
        Logger.logger.removeHandler(self.file_handler)
        Logger.logger.removeHandler(self.streaming_handler)

    @staticmethod
    def log(message):
        Logger.logger.log(Logger.logger.level, message)

    @staticmethod
    def info(message):
        Logger.logger.log(logging.INFO, message)

    @staticmethod
    def debug(message):
        Logger.logger.log(logging.DEBUG, message)

    @staticmethod
    def error(message):
        Logger.logger.log(logging.ERROR, message)

    @staticmethod
    def critical(message):
        Logger.logger.log(logging.CRITICAL, message)

    @staticmethod
    def warn(message):
        Logger.logger.log(logging.WARN, message)

    @staticmethod
    def save_screen_shot(file_name=None):
        image_path = os.path.splitext(Logger.log_path)[0] + file_name + ".png"
        DriverFactory().get_driver().save_screenshot(image_path)
