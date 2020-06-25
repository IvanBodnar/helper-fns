class BaseHelperFnsException(Exception):
    def __init__(self, message: str = None):
        self._message = message


class EnvironmentVariableNotFound(BaseHelperFnsException):
    pass


class DictionaryKeyNotFound(BaseHelperFnsException):
    pass
