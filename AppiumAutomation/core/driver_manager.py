import json
from appium import webdriver
from helper.singleton import Singleton


class DriverFactory(metaclass=Singleton):

    def __init__(self):
        self.driver = None

    def start(self):
        # file_path = 'resources/ios/driver_capabilities.json'
        file_path = 'resources/android/driver_capabilities.json'
        with open(file_path) as data_file:
            desired_capabilities = json.load(data_file)
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities=desired_capabilities)

    def get_driver(self):
        if self.driver is not None:
            return self.driver
        else:
            self.start()
            return self.driver

    def stop(self):
        self.driver.quit()
        self.driver = None
