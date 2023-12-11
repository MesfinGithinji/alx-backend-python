#!/usr/bin/env python3
"""A method that returns a task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return a task that waits for a random number of seconds
    Args:
        max_delay: is the maximum number of seconds that the task will wait
    Returns: the asyncio.Task object
    """
    return asyncio.create_task(wait_random(max_delay))
