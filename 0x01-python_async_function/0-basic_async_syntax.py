#!/usr/bin/env python3
""" The basics of async """
import random


async def wait_random(max_delay: int = 10) -> float:
    """ function that takes an integer as max delay
        and wait for a random delay between 0 and max_delay
        and return it"""
    f = random.uniform(0, max_delay)
    return f
