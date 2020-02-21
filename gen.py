#!/usr/bin/env python3.7 -i

#Python implementation here

def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step

#Generator with an infinite Fibonacci list
def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

