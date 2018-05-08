# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import timeit

start = timeit.default_timer()
"""from itertools import chain, combinations
def powerSet(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

print(list(powerSet("abcd"))) """
p = lambda s: [[x for j,x in enumerate(s) if (i >> j) & 1] for i in range(2**len(s))]

print(p(['a','b','c','d']))

stop = timeit.default_timer()

print stop - start
#print(len(list(powerSet("abcd"))))
