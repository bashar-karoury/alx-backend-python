#!/usr/bin/env python3
"""
Measure the runtime
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        measures the total execution time for wait_n(n, max_delay)
        , and returns total_time / n.
    """

    # calculate the time before
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    p = time.perf_counter()
    # calculate the time after
    totalTime = p - s
    average = totalTime / n
    return average
