#!/usr/bin/env python3
""" More involved type annotations
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')
# dct: typing.Mapping
# key: typing.Any
# default: typing.Union[~T, NoneType]
# return: typing.Union[typing.Any, ~T]


def safely_get_value(
                    dct: Mapping,
                    key: Any,
                    default: Union[T, None] = None) -> Union[Any, T]:
    """ get value from dictionary by key, default if not found"""
    if key in dct:
        return dct[key]
    else:
        return default
