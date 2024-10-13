#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ function takes a list input_list of floats as argument
        and returns their sum as a float
    """
    sum = 0.0
    for n in input_list:
        sum += n
    return sum
