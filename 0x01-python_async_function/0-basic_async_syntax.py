#!/usr/bin/env python3
"""A coroutine that waits for a random delay and eventually returns it"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns random float between 0 and max_delay
    Args:
        max_delay: The maximum delay to return
    Returns:
        A random float between 0 and max_delay
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
