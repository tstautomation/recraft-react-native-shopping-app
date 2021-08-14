BASE_PATH = 'BASE_PATH'
LOG_DIRECTORY = 'LOG_DIRECTORY'

WAIT_TIME = 60  # sec
WAIT_TIME_SHORT = 30  # sec
NO_WAIT = 1

MESSAGE_STRING_VERIFICATION = "EQUAL : EXPECTED : {0}; ACTUAL : {1}"
MESSAGE_STRING_VERIFICATION_NOT_EQUAL = "NOT EQUAL : EXPECTED : {0}; ACTUAL : {1}"
MESSAGE_STRING_VERIFICATION_GREATER_OR_EQUAL = "GREATER OR EQUAL : EXPECTED : {0}; ACTUAL : {1}"
MESSAGE_STRING_CONTAINS = "CONTAINS : EXPECTED : {0}; ACTUAL : {1}"
MESSAGE_STRING_NOT_CONTAINS = "NOT CONTAINS : EXPECTED : {0}; ACTUAL : {1}"
MESSAGE_STRING_VERIFICATION_LESS_THAN = "LESS THAN : EXPECTED : {0}; ACTUAL : {1}"

COMMAND_VERIFY_PRESENT = "[EXECUTE] ELEMENT IS PRESENT FOR LOCATOR : '{0}'"
COMMAND_VERIFY_VISIBLE = "[EXECUTE] ELEMENT IS VISIBLE FOR LOCATOR : '{0}'"
COMMAND_WAIT_FOR_PRESENT = "[EXECUTE] WAIT FOR PRESENT: '{0}'"
COMMAND_WAIT_FOR_NOT_PRESENT = "[EXECUTE] WAIT FOR NOT TO BE PRESENT: '{0}'"
COMMAND_WAIT_FOR_VISIBLE = "[EXECUTE] WAIT FOR VISIBLE: '{0}'"
COMMAND_WAIT_FOR_NOT_VISIBLE = "[EXECUTE] WAIT FOR NOT TO BE VISIBLE: '{0}'"
COMMAND_VERIFY_NOT_PRESENT = "[EXECUTE] ELEMENT IS NOT PRESENT FOR LOCATOR : '{0}'"
COMMAND_VERIFY_NOT_VISIBLE = "[EXECUTE] ELEMENT IS NOT VISIBLE FOR LOCATOR : '{0}'"
COMMAND_FIND_ELEMENT = "[EXECUTE] FIND ELEMENT FOR LOCATOR : '{0}'"
COMMAND_SEND_KEYS = "[EXECUTE] SEND KEYS FOR LOCATOR : '{0}', VALUE : {1}"
COMMAND_CLICK_ELEMENT = "[EXECUTE] CLICK ON ELEMENT FOR LOCATOR : '{0}'"
COMMAND_TAP_AT_POINT = "[EXECUTE] TAP AT POINT : 'X={0}, Y={1}'"
COMMAND_LONG_PRESS = "[EXECUTE] LONG PRESS ON ELEMENT FOR LOCATOR : '{0}'"
COMMAND_WAIT_FOR_ELEMENT_TEXT = "[EXECUTE] WAIT FOR ELEMENT TEXT,ELEMENT TEXT IS PRESENT FOR LOCATOR : '{0}'"
COMMAND_SWAPPING_ELEMENT = "[EXECUTE] SWAP BETWEEN TWO ELEMENT, LOCATOR 1 : '{0}' & LOCATOR 2 : '{1}'"
COMMAND_ELEMENT_PROPERTY = "[EXECUTE] ELEMENT '{0}', FOR LOCATOR : '{1}'"
COMMAND_SCROLL = "[EXECUTE] SCROLL TO THE ELEMENT FOR LOCATOR : '{0}'"

MESSAGE_VERIFY_PRESENT_PASS = "[RESPONSE] ELEMENT IS PRESENT FOR LOCATOR : '{0}'"
MESSAGE_VERIFY_VISIBLE_PASS = "[RESPONSE] ELEMENT IS VISIBLE FOR LOCATOR : '{0}'"
MESSAGE_WAIT_FOR_PRESENT_PASS = "[RESPONSE] WAIT FOR PRESENT,ELEMENT IS PRESENT FOR LOCATOR : '{0}'"
MESSAGE_WAIT_FOR_NOT_PRESENT_PASS = "[RESPONSE] WAIT FOR NOT TO BE PRESENT,ELEMENT IS NOT PRESENT FOR LOCATOR : '{0}'"
MESSAGE_WAIT_FOR_VISIBLE_PASS = "[RESPONSE] WAIT FOR VISIBLE,ELEMENT IS VISIBLE FOR LOCATOR : '{0}'"
MESSAGE_WAIT_FOR_NOT_VISIBLE_PASS = "[RESPONSE] WAIT FOR NOT TO BE VISIBLE,ELEMENT IS NOT VISIBLE FOR LOCATOR : '{0}'"
MESSAGE_VERIFY_NOT_PRESENT_PASS = "[RESPONSE] ELEMENT IS PRESENT FOR LOCATOR : '{0}'"
MESSAGE_FIND_ELEMENT_PASS = "[RESPONSE] FIND ELEMENT FOR LOCATOR : '{0}'"
MESSAGE_SEND_KEYS_PASS = "[RESPONSE] SEND KEYS FOR LOCATOR : '{0}', VALUE : {1}"
MESSAGE_CLICK_ELEMENT_PASS = "[RESPONSE] CLICK ON ELEMENT FOR LOCATOR : '{0}'"
MESSAGE_LONG_PRESS_PASS = "[RESPONSE] LONG PRESS ON ELEMENT FOR LOCATOR : '{0}'"
MESSAGE_WAIT_FOR_ELEMENT_TEXT_PASS = "[RESPONSE] WAIT FOR ELEMENT TEXT,ELEMENT TEXT IS PRESENT FOR LOCATOR : '{0}'"
MESSAGE_SWAPPING_ELEMENT_PASS = "[RESPONSE] SWAP BETWEEN TWO ELEMENT, LOCATOR 1 : '{0}' & LOCATOR 2 : '{1}'"

MESSAGE_VERIFY_PRESENT_FAIL = "[RESPONSE] ELEMENT IS NOT PRESENT FOR LOCATOR : '{0}'"
MESSAGE_VERIFY_VISIBLE_FAIL = "[RESPONSE] ELEMENT IS NOT PRESENT FOR LOCATOR : '{0}'"
MESSAGE_WAIT_FOR_PRESENT_FAIL = "[RESPONSE] WAIT FOR ELEMENT,ELEMENT IS NOT PRESENT FOR LOCATOR : '{0}'"
MESSAGE_WAIT_FOR_NOT_PRESENT_FAIL = "[RESPONSE] WAIT FOR ELEMENT NOT PRESENT,ELEMENT IS PRESENT FOR LOCATOR : '{0}'"
MESSAGE_WAIT_FOR_VISIBLE_FAIL = "[RESPONSE] WAIT FOR VISIBLE,ELEMENT IS NOT VISIBLE FOR LOCATOR : '{0}'"
MESSAGE_WAIT_FOR_NOT_VISIBLE_FAIL = "[RESPONSE] WAIT FOR NOT VISIBLE,ELEMENT IS VISIBLE FOR LOCATOR : '{0}'"
MESSAGE_VERIFY_NOT_PRESENT_FAIL = "[RESPONSE] ELEMENT IS PRESENT FOR LOCATOR : '{0}'"
MESSAGE_VERIFY_NOT_VISIBLE_FAIL = "[RESPONSE] ELEMENT IS VISIBLE FOR LOCATOR : '{0}'"
MESSAGE_FIND_ELEMENT_FAIL = "[RESPONSE] FIND ELEMENT FOR LOCATOR : '{0}'"
MESSAGE_SEND_KEYS_FAIL = "[RESPONSE] SEND KEYS FOR LOCATOR : '{0}', VALUE : {1}"
MESSAGE_CLICK_ELEMENT_FAIL = "[RESPONSE] CLICK ON ELEMENT FOR LOCATOR : '{0}'"
MESSAGE_LONG_PRESS_FAIL = "[RESPONSE] LONG PRESS ON ELEMENT FOR LOCATOR : '{0}'"
MESSAGE_WAIT_FOR_ELEMENT_TEXT_FAIL = "[RESPONSE] WAIT FOR ELEMENT TEXT ,ELEMENT TEXT IS NOT PRESENT FOR LOCATOR : '{0}'"
MESSAGE_SWAPPING_ELEMENT_FAIL = "[RESPONSE] SWAP BETWEEN TWO ELEMENT, LOCATOR 1 : '{0}' & LOCATOR 2 : '{1}'"

MESSAGE_ELEMENT_PROPERTY = "ELEMENT '{0}' : '{1}', FOR LOCATOR : '{2}'"
MESSAGE_SCROLL = "SCROLL TO THE ELEMENT FOR LOCATOR : '{0}'"

STATIC_WAIT = "STATIC WAIT FOR {0} SECONDS"

BEFORE_SCENARIO = "Scenario : {0} Started"
AFTER_SCENARIO = "Scenario [{0}] : {1} Finished"

BEFORE_STEP = "Step : {0} Started"
AFTER_STEP = "Step [{0}] : {1} Finished"
