#!/usr/bin/env python3
"""
 Let's execute multiple coroutines at the same time with async
"""
import asyncio
import importlib


# wait_random = __import__('0-basic_async_syntax').wait_random
module = importlib.import_module('0-basic_async_syntax')


async def wait_n(n: int, max_delay: int):
    """
        function spawn wait_random n times with the specified max_delay
    """

    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return delays
