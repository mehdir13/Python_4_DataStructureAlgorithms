import time
from functools import lru_cache


# 1. Iterative Approach with List
def fibonacci_iterative_with_list(n):
    if n <= 1:
        return n
    fib_sequence = [0, 1]  # Initialize the list with the first two Fibonacci numbers
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence[n]  # Return the nth Fibonacci number


# 2. Recursive Approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# 3. Recursive with Caching using lru_cache
@lru_cache(maxsize=None)
def fibonacci_recursive_cached(n):
    if n <= 1:
        return n
    return fibonacci_recursive_cached(n - 1) + fibonacci_recursive_cached(n - 2)


# Function to time a given Fibonacci function
def time_fibonacci_function(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time


# Example usage
n = 38  # Choose a Fibonacci term to calculate for timing purposes

# Timing Iterative Approach
result_iterative, time_iterative = time_fibonacci_function(
    fibonacci_iterative_with_list, n
)
print(
    f"Iterative with List Fibonacci Result: {result_iterative}, Time: {time_iterative:.6f} seconds"
)

# Timing Recursive Approach
result_recursive, time_recursive = time_fibonacci_function(fibonacci_recursive, n)
print(
    f"Recursive Fibonacci Result: {result_recursive}, Time: {time_recursive:.6f} seconds"
)

# Timing Cached Recursive Approach
result_recursive_cached, time_recursive_cached = time_fibonacci_function(
    fibonacci_recursive_cached, n
)
print(
    f"Cached Recursive Fibonacci Result: {result_recursive_cached}, Time: {time_recursive_cached:.6f} seconds"
)
