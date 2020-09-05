#
# Multiplicative Persistence - simple algorithm to find out the order.
#

import functools
import operator


class OrderNotFound(Exception):
    def __init__(self):
        pass


def is_in_order(num_as_str):
    a = num_as_str[0]
    for n in num_as_str[1:]:
        if n < a:
            return False
        a = n
    return True


def efficient_candidate_generator(start, stop):
    for x in list(range(start, stop)):
        s = str(x)
        if ('5' in s) or ('0' in s):
            next
        elif not is_in_order(s):
            next
        else:
            yield x


def infinite_candidate_generator(start):
    """Generate possible candidate numbers, starting at start.
    """
    now = start
    while (True):
        s = str(now)
        if not (('5' in s) or ('0' in s)) and is_in_order(s):
            yield now
        now += 1


def compute_mp_order(number):
    """Compute the multiplicative persistence order of number.
    number: the number to compute the order on.
    """
    if (number < 10):
        return 0
    number_set = [int(i) for i in str(number)]
    reduced_number = functools.reduce(operator.mul, number_set, 1)
    return 1 + compute_mp_order(reduced_number)


def order_from_generator(generator):
    """Generate the order belonging to the generator items
    """
    for num in generator():
        yield (compute_mp_order(num), num)

def find_max_order(generator):
    max_order = 0
    max_number = 0
    for order, num in order_from_generator(generator):
        if order > max_order:
            max_order = order
            max_number = num
    return (max_order, max_number)


def find_with_order(generator, order):
    for this_order, num in order_from_generator(generator):
        if this_order == order:
            return (order, num)
    raise OrderNotFound()