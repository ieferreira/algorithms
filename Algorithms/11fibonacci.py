# %%
# Using IPython
from functools import lru_cache
from typing import Dict


def fib0(n):
    # do not run with numbers higher than 20
    if n == 1 or n == 0:
        return n
    return fib0(n-1) + fib0(n-2)


print(fib0(10))
# result 1 1 2 3 5 8 13 21
# %%
# implementation by Kopec, 2019


def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n-2) + fib1(n-1)


print(fib1(10))
# %%
# using basic memoization

memo: Dict[int, int] = {0: 0, 1: 1}


def fib2(n: int) -> int:
    # can run with higher numbers
    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)

    return memo[n]


fib2(20)
# %%

# implementation with use of lru_cache module


@lru_cache(maxsize=None)
def fib
