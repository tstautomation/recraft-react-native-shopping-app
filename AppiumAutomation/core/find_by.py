from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from helper.exception import AutomationError


def get_find_by(locator):
    if locator.startswith('xpath='):
        by = By.XPATH
        locator = locator.split('xpath=', 1)[1]
    elif locator.startswith('//'):
        by = By.XPATH
    elif locator.startswith('id='):
        by = MobileBy.ACCESSIBILITY_ID
        locator = locator.split('id=', 1)[1]
    elif locator.startswith('name='):
        by = By.XPATH
        locator = "//*[@name='" + locator.split('name=', 1)[1] + "']"
    elif locator.startswith('class='):
        by = By.CLASS_NAME
        locator = locator.split('class=', 1)[1]
    elif locator.startswith('text='):
        raise AutomationError('invalid locator strategy')
    elif locator.startswith('content-desc='):
        by = By.XPATH
        locator = '//*[@*="' + locator.split('content-desc=', 1)[1] + '"]'
    elif locator.startswith('predicate='):
        by = MobileBy.IOS_PREDICATE
        locator = locator.split('predicate=', 1)[1]
    elif locator.startswith('class-chain='):
        by = MobileBy.IOS_CLASS_CHAIN
        locator = locator.split('class-chain=', 1)[1]
    else:
        by = MobileBy.ACCESSIBILITY_ID
        locator = str(locator)
    return by, locator
