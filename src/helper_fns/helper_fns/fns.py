import os
from typing import Any

from .exceptions import EnvironmentVariableNotFound, DictionaryKeyNotFound


def get_env_var(variable_name: str) -> str:
    try:
        return os.environ[variable_name]
    except KeyError:
        message = f'Environment variable {variable_name} not found'
        raise EnvironmentVariableNotFound(message=message)


def get_key(dictionary: dict, *keys) -> Any:
    for k in keys:
        try:
            dictionary = dictionary[k]
        except KeyError:
            raise DictionaryKeyNotFound(message=f'Key {k} not found')
    return dictionary
