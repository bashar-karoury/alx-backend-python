#!/usr/bin/env python3
"""
 Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        function spawn wait_random n times with the specified max_delay
    """

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    # Use asyncio.as_completed() to get coroutines in the order they complete
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        delays.append(result)
    return delays
