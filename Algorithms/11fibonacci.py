# %%
# Using IPython
from typing import Generator
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
def fib3(n: int) -> int:
    if n < 2:
        return n
    return fib3(n - 2) + fib3(n - 1)


# big number
%timeit fib3(100)
# result: 354224848179261915075
# time taken: 117 ns ± 0.6 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
# %%

# performance through iterative approach


def fib4(n: int) -> int:
    if n == 0:
        return n  # base cases and special case
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


%timeit fib4(100)
# result: 354224848179261915075
# time taken: 5.21 µs ± 356 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

# %%
# generate the values up two certain value


def fib5(n: int) -> Generator[int, None, None]:

    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


for i in fib5(50):
    print(i)

# %%
