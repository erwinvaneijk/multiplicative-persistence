# Multiplicative Persistence

## Status

[![Build Status](https://github.com/erwinvaneijk/multiplicative-persistence/workflows/python-multiplicatve-persistence/badge.svg)]

## Description

Multiplicative Persistence Order is the number you get when you start
multiplying all the (base 10) digits in a number, and multiply the digits
of the results again, until you get a one digit number.

So

to compute the order of 35 =>

- 3 * 5 = 15
- 1 * 5 = 5
- The order is 2

to compute the order of 39 =>

- 3 * 9 = 27
- 2 * 7 = 14
- 1 * 4 = 4
- The order is 3

to compute the order of 237 =>

- 2 * 3 * 7 = 42
- 4 * 2 = 8
- The order is 2
