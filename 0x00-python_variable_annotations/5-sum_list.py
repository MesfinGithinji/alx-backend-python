#!/usr/bin/env python3
"""A function that sums a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of floats
    Args:
        input_list (list): List of floats
    Returns:
        float: Sum of the floats in the List
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
