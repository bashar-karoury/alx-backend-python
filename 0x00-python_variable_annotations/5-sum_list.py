#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    sum = 0.0
    for n in input_list:
        sum += n
    return sum
