#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ functions that takes a list mxd_lst of integers and floats
        and returns their sum as a float
    """
    sum: float = 0
    for n in mxd_lst:
        sum += n
    return sum
