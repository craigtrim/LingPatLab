# -*- coding: utf-8 -*-


from pprint import pprint

from typing import List
from typing import Callable

from collections import defaultdict


class DataTypeNotExpectedError(Exception):
    """Exception raised for data type errors

    Attributes:
        actual_value -- the actual value
        expected_type -- the expected value
    """

    def __init__(self,
                 actual_value: str,
                 expected_type: object):
        message = '\n'.join([
            'Data Type Not Expected',
            f'\tActual Value: {expected_type}',
            f'\tActual Type: {type(actual_value)}',
            f'\tExpected Type: {expected_type}'])
        super().__init__(message)


class ContentNotExpectedError(Exception):
    """Exception raised for data content errors

    Attributes:
        actual_content -- the actual content
        expected_content -- the expected content
    """

    def __init__(self,
                 actual_content: str,
                 expected_content: object):
        message = '\n'.join([
            'Data Content Not Expected',
            f'\tExpected Content: {actual_content}',
            f'\tActual Content: {type(expected_content)}'])
        super().__init__(message)


class Enforcer(object):

    def __init__(self):
        pass

    @classmethod
    def is_tuple(cls,
                 value: object) -> None:
        if type(value) != tuple:
            raise DataTypeNotExpectedError(actual_value=value,
                                           expected_type='tuple')

    @classmethod
    def is_optional_tuple(cls,
                          value: object) -> None:
        if value is not None:
            cls.is_tuple(value)

    @classmethod
    def is_bool(cls,
                value: object,
                display: bool = False) -> None:
        if type(value) != bool:
            raise DataTypeNotExpectedError(actual_value=value,
                                           expected_type='bool')

        if display:
            print(value)

    @classmethod
    def is_str(cls,
               value: object,
               display: bool = False) -> None:
        if type(value) != str:
            raise DataTypeNotExpectedError(actual_value=value,
                                           expected_type='str')

        if display:
            print(value)

    @classmethod
    def is_optional_str(cls,
                        value: object,
                        display: bool = False) -> None:
        if value is not None:
            cls.is_str(value, display=display)

    @classmethod
    def is_int_or_float(cls,
                        value: object,
                        display: bool = False) -> None:
        """ Check if the incoming value is an Int or Float

        Args:
            value (object): the incoming value
            display (bool, optional): if True, display the value. Defaults to False.

        Raises:
            DataTypeNotExpectedError: the incoming value was neither an int nor a float
        """
        _type = type(value)
        if _type == int or _type == float:
            if display:
                print(value)
            return None

        raise DataTypeNotExpectedError(actual_value=value,
                                       expected_type='int or float')

    @classmethod
    def is_int(cls,
               value: object,
               display: bool = False) -> None:
        if type(value) != int:
            raise DataTypeNotExpectedError(actual_value=value,
                                           expected_type='int')

        if display:
            print(value)

    @classmethod
    def is_optional_int(cls,
                        value: object,
                        display: bool = False) -> None:
        if value is not None:
            cls.is_int(value, display=display)

    @classmethod
    def is_float(cls,
                 value: object,
                 display: bool = False) -> None:
        if type(value) != float:
            raise DataTypeNotExpectedError(actual_value=value,
                                           expected_type='float')

        if display:
            print(value)

    @classmethod
    def is_optional_float(cls,
                          value: object,
                          display: bool = False) -> None:
        if value is not None:
            cls.is_float(value, display=display)

    @classmethod
    def is_list(cls,
                value: object,
                display: bool = False) -> None:
        if type(value) != list:
            raise DataTypeNotExpectedError(actual_value=value,
                                           expected_type='list')

        if display:
            [print(x) for x in value]

    @classmethod
    def is_optional_list(cls,
                         value: object,
                         display: bool = False) -> None:
        if value is not None:
            cls.is_list(value, display=display)

    @classmethod
    def is_nonempty_list(cls,
                         value: object,
                         display: bool = False) -> None:
        """ Test for Non-Empty List

        Args:
            value (object): any list

        Raises:
            ContentNotExpectedError: list is empty (has no values)
        """
        cls.is_list(value, display=display)
        if not len(value):
            raise ContentNotExpectedError(actual_content=value,
                                          expected_content='Non Empty List')

    @classmethod
    def is_empty_list(cls,
                      value: object) -> None:
        """ Test for Empty List

        Args:
            value (object): any list

        Raises:
            ContentNotExpectedError: list is non-empty (has at least one value)
        """
        cls.is_list(value)
        if len(value):
            raise ContentNotExpectedError(actual_content=value,
                                          expected_content='List has Value')

    @classmethod
    def is_dict(cls,
                value: object,
                display: bool = False) -> None:
        if type(value) not in [dict, defaultdict]:
            raise DataTypeNotExpectedError(actual_value=value,
                                           expected_type='dict')

        if display:
            pprint(value)

    @classmethod
    def is_dict_of_lists(cls,
                         value: object,
                         display: bool = False) -> None:
        cls.is_dict(value)

        for k in value:
            cls.is_list(value[k])

        if display:
            pprint(value)

    @classmethod
    def _is_dict_of_list_of_type(cls,
                                 value: object,
                                 list_of_type: Callable,
                                 display: bool = False) -> None:
        cls.is_dict(value)

        for k in value:
            list_of_type(value[k])

        if display:
            pprint(value)

    @classmethod
    def is_dict_of_list_of_strs(cls,
                                value: object,
                                display: bool = False) -> None:
        return cls._is_dict_of_list_of_type(
            value=value,
            list_of_type=cls.is_list_of_str,
            display=display)

    @classmethod
    def is_dict_of_list_of_floats(cls,
                                  value: object,
                                  display: bool = False) -> None:
        return cls._is_dict_of_list_of_type(
            value=value,
            list_of_type=cls.is_list_of_float,
            display=display)

    @classmethod
    def is_dict_of_list_of_ints(cls,
                                value: object,
                                display: bool = False) -> None:
        return cls._is_dict_of_list_of_type(
            value=value,
            list_of_type=cls.is_list_of_int,
            display=display)

    @classmethod
    def is_dict_of_list_of_tuples(cls,
                                  value: object,
                                  display: bool = False) -> None:
        return cls._is_dict_of_list_of_type(
            value=value,
            list_of_type=cls.is_list_of_tuples,
            display=display)

    @classmethod
    def is_dict_of_list_of_dicts(cls,
                                 value: object,
                                 display: bool = False) -> None:
        return cls._is_dict_of_list_of_type(
            value=value,
            list_of_type=cls.is_list_of_dicts,
            display=display)

    @classmethod
    def is_dict_of_list_of_typed_dicts(cls,
                                       value: object,
                                       keys: List[str],
                                       display: bool = False) -> None:

        cls.is_dict(value)
        cls.is_list_of_str(keys)
        keys = sorted(keys)

        for k in value:

            cls.is_list_of_dicts(value[k])
            for list_item in value[k]:

                actual_keys = sorted(list_item.keys())
                if actual_keys != keys:
                    raise ContentNotExpectedError(
                        actual_content=actual_keys,
                        expected_content=keys)

        if display:
            pprint(value)

    @classmethod
    def is_nonempty_dict(cls,
                         value: object,
                         display: bool = False) -> None:
        """ Test for Non-Empty Dict

        Args:
            value (object): any dict

        Raises:
            ContentNotExpectedError: dict is empty (has no values)
        """
        cls.is_dict(value, display=display)
        if not len(value):
            raise ContentNotExpectedError(actual_content=value,
                                          expected_content='Non Empty Dict')

    @classmethod
    def is_empty_dict(cls,
                      value: object) -> None:
        """ Test for Empty Dict

        Args:
            value (object): any dict

        Raises:
            ContentNotExpectedError: dict is non-empty (has at least one value)
        """
        cls.is_dict(value)
        if len(value):
            raise ContentNotExpectedError(actual_content=value,
                                          expected_content='Dict has Value')

    @classmethod
    def is_optional_dict(cls,
                         value: object,
                         display: bool = False) -> None:
        if value is not None:
            cls.is_dict(value, display=display)

    @classmethod
    def keys(cls,
             d: dict, *args):
        """ Compare actual dictionary keys with expected dictionary keys

        Usage:
            Enforcer.keys(d_results, 'result', 'tokens')
            This will assert 'd_results' contains the keys 'result' and 'tokens' and only these keys

        Args:
            d (dict): the dictionary to test

        Raises:
            ContentNotExpectedError: the actual keys do not match the expected keys
        """
        cls.is_dict(d)
        args = sorted(args)
        keys = sorted(d.keys())
        if keys != args:
            raise ContentNotExpectedError(actual_content=keys,
                                          expected_content=args)

    @classmethod
    def is_list_of_float(cls,
                         value: object) -> None:
        """ This is a highly specialized data type checker

        Args:
            value (object): True if this is a list of float elements
        """

        def _is_list_of_floats() -> bool:
            """ List of Integers
                Sample Format:
                    ['alpha', 'beta']

            Returns:
                bool: True if list of ints
            """
            if not len(value):
                return False
            if type(value) != list:
                return False
            for item in value:
                if type(item) != float:
                    return False
            return True

        if not _is_list_of_floats():
            raise DataTypeNotExpectedError(actual_value=value,
                                           expected_type='List[float]')

    @classmethod
    def is_list_of_int(cls,
                       value: object) -> None:
        """ This is a highly specialized data type checker

        Args:
            value (object): True if this is a list of int elements
        """

        def _is_list_of_ints() -> bool:
            """ List of Integers
                Sample Format:
                    ['alpha', 'beta']

            Returns:
                bool: True if list of ints
            """
            if not len(value):
                return False
            if type(value) != list:
                return False
            for item in value:
                if type(item) != int:
                    return False
            return True

        if not _is_list_of_ints():
            raise DataTypeNotExpectedError(actual_value=value,
                                           expected_type='List[int]')

    @classmethod
    def is_list_of_str(cls,
                       value: object) -> None:
        """ This is a highly specialized data type checker

        Args:
            value (object): True if this is a list of str elements
        """

        def _is_list_of_strings() -> bool:
            """ List of Strings
                Sample Format:
                    ['alpha', 'beta']

            Returns:
                bool: True if list of strings
            """
            if not len(value):
                return False
            if type(value) != list:
                return False
            for item in value:
                if type(item) != str:
                    return False
            return True

        if not _is_list_of_strings():
            raise DataTypeNotExpectedError(actual_value=value,
                                           expected_type='List[str]')

    @classmethod
    def is_list_of_list_of_dicts(cls,
                                 value: object) -> None:
        """ This is a highly specialized data type checker

        Args:
            value (object): True if this is a list of dict elements
        """

        if type(value) != list:
            raise DataTypeNotExpectedError(actual_value=value,
                                           expected_type='List[List[Dict]]')

        [Enforcer.is_list_of_dicts(x) for x in value]

    @classmethod
    def is_list_of_tuples(cls,
                          value: object) -> None:
        """ This is a highly specialized data type checker

        Args:
            value (object): True if this is a list of tuple elements
        """

        def _is_list_of_tuples() -> bool:
            """ List of Tuples
                Sample Format:
                    [('alpha', 'beta')]

            Returns:
                bool: True if list of tuples
            """
            if not len(value):
                return False
            if type(value) != list:
                return False
            for item in value:
                if type(item) != tuple:
                    return False
            return True

        if not _is_list_of_tuples():
            raise DataTypeNotExpectedError(actual_value=value,
                                           expected_type='List[tuple]')

    @classmethod
    def is_list_of_dicts(cls,
                         value: object) -> None:
        """ This is a highly specialized data type checker

        Args:
            value (object): True if this is a list of dict elements
        """

        def _is_list_of_dicts() -> bool:
            """ List of Dicts
                Sample Format:
                    [{'entity': 'Late_Transport'}]

            Returns:
                bool: True if list of dicts
            """
            if not len(value):
                return False
            if type(value) != list:
                return False
            for item in value:
                if type(item) != dict:
                    return False
            return True

        if not _is_list_of_dicts():
            raise DataTypeNotExpectedError(actual_value=value,
                                           expected_type='List[dict]')

    @classmethod
    def is_none(cls,
                value) -> None:
        """ Assert Value is None
        this is typically used in Unit Testing1

        Args:
            value (None): a null (and therefore untyped) object

        Raises:
            ContentNotExpectedError: object is non-null
        """
        if value is not None:
            raise ContentNotExpectedError(actual_value=value,
                                          expected_type='None')

    @classmethod
    def is_json(cls,
                value: object) -> None:
        if Enforcer.is_dict(value=value, display=False):
            return True
        if Enforcer.is_list(value=value, display=False):
            return True
        return False
