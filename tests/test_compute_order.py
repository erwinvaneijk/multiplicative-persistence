#
# Test the functions in multpersist.__init__.py
#

import itertools
from multpersist import *


def predetermined_number_generator():
    for x in [10, 18, 237, 2777778888899, 277777788888899]:
        yield x


def ranged_generator(start, stop):
    for x in list(range(start, stop)):
        s = str(x)
        if '5' in s:
            next
        elif not is_in_order(s):
            next
        else:
            yield x


def test_is_in_order():
    assert is_in_order(str(11))
    assert is_in_order(str(123))
    assert not is_in_order(str(321))


def test_ranged_generator():
    count = 0
    for xl in ranged_generator(10, 999):
        count += 1
    assert count == 155

def test_efficient_candidate_generator():
    count = 0
    for xl in efficient_candidate_generator(10, 999):
        count += 1
    assert count == 155


def test_compute_order():
    assert compute_mp_order(10) == 1
    assert compute_mp_order(18) == 1
    assert compute_mp_order(237) == 2
    assert compute_mp_order(2777778888899) == 3
    assert compute_mp_order(277777788888899) == 11


def test_find_order():
    assert find_max_order(predetermined_number_generator) == (11, 277777788888899)


def test_largest_order_under_1e6():
    generator = lambda : efficient_candidate_generator(10, 1000000)
    assert find_max_order(generator) == (7, 68889)


def test_largest_order_between_1e6_3e6():
    generator = lambda : efficient_candidate_generator(1000000, 10000000)
    assert find_max_order(generator) == (8, 2677889)


def test_infinite_generator():
    generator = infinite_candidate_generator(10)
    l = list(itertools.islice(generator, 10))
    assert l == [11, 12, 13, 14, 16, 17, 18, 19, 22, 23]


def test_find_smallest_with_order():
    generator = lambda: infinite_candidate_generator(10)
    assert find_with_order(generator, 6) == (6, 6788)
    assert find_with_order(generator, 7) == (7, 68889)
    assert find_with_order(generator, 8) == (8, 2677889)
    assert find_with_order(generator, 9) == (9, 26888999)