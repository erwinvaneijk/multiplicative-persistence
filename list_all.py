#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
"""
List the multiplicative order of numbers.

Try possible candidates to find the next higher order number, starting
from the number 20. Print the lowest of the higher orders.
"""

import itertools
import sys

import multpersist


def main(args):
    """List the multiplicative order of the numbers.

    List the multiplicative order of the numbers, starting from the first
    argument, until the second number of numbers are done.
    """
    generator = multpersist.infinite_candidate_generator(int(args[0]))
    for number in itertools.islice(generator, int(args[1])):
        order = multpersist.compute_mp_order(number)
        print("O({}) = {}".format(order, number))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
