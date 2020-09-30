#!/usr/bin/env python3
# -*- coding=utf-8 -*-
"""
Find multiplicative numbers.

Starting from 10, with order 1 find the next order number, and print
that number, and the time it took to find it.
"""

import sys
import time

import multpersist


def generator():
    """Create the generator to find possible candidates."""
    return multpersist.infinite_candidate_generator(10)


def main():
    """Find all multiplicative orders.

    Starting from 10, with order 1, find the lowest number with the
    next multiplicative order.
    """
    start_time = time.time()
    for order, number in multpersist.find_next(generator, 1):
        current_time = time.time()
        difference = current_time - start_time
        print("{}\tO({}) = {}".format(difference, order, number))
    return 0


if __name__ == "__main__":
    sys.exit(main())
