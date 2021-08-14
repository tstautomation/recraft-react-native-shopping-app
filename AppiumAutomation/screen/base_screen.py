import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from core.constant import *
from core.driver_manager import DriverFactory
from core.find_by import get_find_by
from helper.exception import ElementNotFoundError
from helper.logger import Logger


class BaseScreen:
    def __init__(self):
        pass

    def driver(self):
        return DriverFactory().get_driver()

    def wait_for_visible(self, locator, wait_time=WAIT_TIME):
        Logger.info(COMMAND_WAIT_FOR_VISIBLE.format(locator))
        return WebDriverWait(self.driver(), wait_time).until(
            ec.visibility_of_element_located(get_find_by(locator))
        )

    def assert_present(self, locator):
        Logger.info(COMMAND_VERIFY_PRESENT.format(locator))
        try:
            WebDriverWait(self.driver(), NO_WAIT).until(
                ec.presence_of_element_located(get_find_by(locator))
            )
            Logger.info(MESSAGE_VERIFY_PRESENT_PASS.format(locator))
        except Exception as e:
            Logger.error(str(e.__dict__))
            raise ElementNotFoundError(MESSAGE_VERIFY_PRESENT_FAIL.format(locator))

    def click(self, locator):
        Logger.info(COMMAND_CLICK_ELEMENT.format(locator))
        try:
            element = self.wait_for_visible(locator)
            element.click()
            Logger.info(MESSAGE_CLICK_ELEMENT_PASS.format(locator))
        except Exception as e:
            raise ElementNotFoundError(MESSAGE_CLICK_ELEMENT_FAIL.format(str(e.__dict__)))

    def send_keys(self, locator, value):
        Logger.info(COMMAND_CLICK_ELEMENT.format(locator))
        try:
            element = self.wait_for_visible(locator)
            element.clear()
            element.send_keys(value)
            Logger.info(MESSAGE_CLICK_ELEMENT_PASS.format(locator))
        except Exception as e:
            raise ElementNotFoundError(MESSAGE_CLICK_ELEMENT_FAIL.format(str(e.__dict__)))

    def find_element(self, key):
        value = os.getenv(key)
        by, value = get_find_by(value)
        return self.driver().find_element(by=by, value=value)

    def find_elements(self, key):
        value = os.getenv(key)
        by, value = get_find_by(value)
        return self.driver().find_elements(by=by, value=value)

    def __getattr__(self, key):
        try:
            if hasattr(BaseScreen, key):
                return object.__getattribute__(self, key)
            return os.getenv(str(key).lower())
        except AttributeError:
            super(BaseScreen, self).__getattribute__("locator_key_missing")(key)

    def locator_key_missing(self, key):
        self.logger.info("No %s here!" % key)
