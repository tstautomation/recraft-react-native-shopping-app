class AutomationError(Exception):
    def __init__(self, message=""):
        super(AutomationError, self).__init__(message)


class ElementNotFoundError(Exception):
    def __init__(self, message=""):
        super(ElementNotFoundError, self).__init__(message)
