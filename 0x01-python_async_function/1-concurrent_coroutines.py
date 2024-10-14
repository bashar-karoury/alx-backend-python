#!/usr/bin/env python3
"""
 Let's execute multiple coroutines at the same time with async
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
        function spawn wait_random n times with the specified max_delay
    """

    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return delays
