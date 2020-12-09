import time
import functools

# Calculating Fibonacci in 3 ways:
#   - easy code, bad performance
#   - more complex code, good performance
#   - easy code, good performance


# most simple recursive fib calculation
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


# using memoization to reduce Complexity from O(n**2) to O(n) for recursive fib calculation
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo.update({n: fib_memo(n-1, memo)+fib_memo(n-2, memo)})
    return memo[n]
# If we use memo={} as default arg value, there is a warning for 'default arg value is mutable',
# we avoid this by assigning None as default value and check it inside of the function and assign {} to memo
# see here: https://florimond.dev/blog/articles/2018/08/python-mutable-defaults-are-the-source-of-all-evil/


# using tabulation to reduce complexity to O(n) for iterative calculation
def fib_tab(n: int):
    tab = [0]*(n+2)
    tab[1] = 1
    for x in range(0, n):
        tab[x+1] += tab[x]
        tab[x+2] += tab[x]
    return tab[n]


# using python builtin functools module to implement memoization.
@functools.cache
def fib_cached(n):
    if n <= 2:
        return 1
    return fib_cached(n-1) + fib_cached(n-2)


# The Fibonacci number to calculate in all 3 algorithms
fib_to_calc = 37

print('\nPrimitive Fib Calc:')
start = time.time()
print(fib(fib_to_calc))
end = time.time()
print(f"Time taken: {end-start}")

print('\nMemoization Fib Calc:')
start = time.time()
print(fib_memo(fib_to_calc))
end = time.time()
print(f"Time taken: {end-start}")

print('\nTabulation Fib Calc:')
start = time.time()
print(fib_tab(fib_to_calc))
end = time.time()
print(f"Time taken: {end-start}")

print('\nfunctools.cache Fib Calc:')
start = time.time()
print(fib_cached(fib_to_calc))
end = time.time()
print(f"Time taken: {end-start}")
