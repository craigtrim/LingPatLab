# -*- coding: utf-8 -*-
""" Environment Variable Utility Methods """


import os

from typing import List


class EnvIO(object):
    """ Environment Variable Utility Methods """

    @staticmethod
    def exists(env_var: str) -> bool:
        """Check if Environment Variable exists

        Args:
            env_var (str): the Environment Variable name

        Returns:
            bool: True if the Environment Variable exists
        """
        return env_var in os.environ and len(os.environ[env_var])

    @staticmethod
    def float_or_exception(*args) -> float:
        """Retrieve Environment Variable by Name or throw exception

        Args:
            args (list): a list of Environment Variable names

        Raises:
            ValueError: none of the Environment Variables were not found

        Returns:
            str: the first Environment Variable value to be found
        """
        for env_var in args:
            if EnvIO.exists(env_var):
                return EnvIO.as_float(env_var)
        raise ValueError(env_var)

    @staticmethod
    def float_or_default(env_var: str,
                         default: int) -> float:
        """Retrieve Environment Variable by Name or return default

        Args:
            env_var (str): the Environment Variable name
            default (float): the default value

        Returns:
            float: the Environment Variable value
        """
        if EnvIO.exists(env_var):
            return EnvIO.as_float(env_var)
        return default

    @staticmethod
    def int_or_exception(*args) -> int:
        """Retrieve Environment Variable by Name or throw exception

        Args:
            args (list): a list of Environment Variable names

        Raises:
            ValueError: none of the Environment Variables were not found

        Returns:
            str: the first Environment Variable value to be found
        """
        for env_var in args:
            if EnvIO.exists(env_var):
                return EnvIO.as_int(env_var)
        raise ValueError(env_var)

    @staticmethod
    def int_or_default(env_var: str,
                       default: int) -> int:
        """Retrieve Environment Variable by Name or return a default value

        Args:
            env_var (str): the Environment Variable name
            default (intg): the default value

        Returns:
            int: the Environment Variable value
        """
        if EnvIO.exists(env_var):
            return EnvIO.as_int(env_var)

        return default

    @staticmethod
    def str_or_default(env_var: str,
                       default: str) -> str:
        """Retrieve Environment Variable by Name or return a default value

        Args:
            env_var (str): the Environment Variable name
            default (str): the default value

        Returns:
            str: the Environment Variable value
        """
        return os.environ.get(env_var, default)

    @staticmethod
    def str_or_exception(*args) -> str:
        """Retrieve Environment Variable by Name or throw exception

        Args:
            args (list): a list of Environment Variable names

        Raises:
            ValueError: none of the Environment Variables were not found

        Returns:
            str: the first Environment Variable value to be found
        """
        for env_var in args:
            if EnvIO.exists(env_var):
                return EnvIO.as_str(env_var)

        raise ValueError(args)

    @staticmethod
    def as_list(*args,
                lower: bool = True) -> list:
        """Retrieve Environment Variable as a tokenized value to list

        Args:
            args (str): a list of one-or-more Environment Variable names

        Returns:
            str or None: a list representation of the values
        """
        for env_var in args:
            if env_var in os.environ:
                values = [x.strip() for x in os.environ[env_var].split(',')]
                values = [x for x in values if x and len(x)]
                if lower:
                    values = [x.lower() for x in values]
                return values

        return []

    @staticmethod
    def as_str(*args) -> str or None:
        """Retrieve Environment Variable as a string value

        Args:
            args (str): a list of one-or-more Environment Variable names

        Returns:
            str or None: a String representation of the value
        """
        for env_var in args:
            if env_var in os.environ:
                return str(os.environ[env_var])

    @staticmethod
    def as_int(*args) -> int or None:
        """Retrieve Environment Variable as an int value

        Args:
            args (str): a list of one-or-more Environment Variable names

        Returns:
            str or None: an int representation of the value
        """
        for env_var in args:
            if env_var in os.environ:
                try:
                    return int(os.environ[env_var])
                except ValueError:
                    pass

    @staticmethod
    def as_float(*args) -> float or None:
        """Retrieve Environment Variable as a float value

        Args:
            args (str): a list of one-or-more Environment Variable names

        Returns:
            str or None: a float representation of the value
        """
        for env_var in args:
            if env_var in os.environ:
                try:
                    return float(os.environ[env_var])
                except ValueError:
                    pass

    @staticmethod
    def is_true(env_var: str) -> bool:
        return os.getenv(env_var, 'False').lower() in ('true', '1', 't')

    @staticmethod
    def is_false(env_var: str) -> bool:
        return not EnvIO.is_true(env_var)

    @staticmethod
    def set_true(env_var: str) -> None:
        os.environ[env_var] = str(True)

    @staticmethod
    def set_false(env_var: str) -> None:
        os.environ[env_var] = str(False)

    @staticmethod
    def exists_as_true(env_var: str) -> bool:
        if EnvIO.exists(env_var):
            return EnvIO.is_true(env_var)
        return False

    @staticmethod
    def set_string(key: str,
                   value: str) -> None:
        os.environ[key] = value

    @staticmethod
    def set_int(key: str,
                value: int) -> None:
        os.environ[key] = str(value)

    @staticmethod
    def set_float(key: str,
                  value: float) -> None:
        os.environ[key] = str(value)
