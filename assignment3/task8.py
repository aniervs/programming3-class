

import time
from functools import wraps

def profiler(func):
    """
        Decorates a function to profile its execution time and call count.
        It measures the total number of calls, including recursive ones, and the execution time of non-recursive calls.
        This is useful for performance analysis and debugging.
        """

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not hasattr(wrapper, 'depth'):
            wrapper.depth = 0  # Recursion depth
            wrapper.calls = 0  # Total calls including recursive ones
            wrapper.non_recursive_calls = 0  # Non-recursive initial calls

        wrapper.depth += 1
        if wrapper.depth == 1:
            wrapper.non_recursive_calls += 1
            start = time.time()

        wrapper.calls += 1
        result = func(*args, **kwargs)

        if wrapper.depth == 1:
            end = time.time()
            wrapper.last_time_taken = end - start

        wrapper.depth -= 1
        return result

    wrapper.depth = 0  # Current recursion
    wrapper.calls = 0  # Total number of calls
    wrapper.last_time_taken = 0  # Time taken for the last non-recursive call
    wrapper.non_recursive_calls = 0  # Number of non-recursive initial calls
    return wrapper

@profiler
def ackermann(m: int, n: int) -> int:
    """
        Computes the Ackermann function, a recursive mathematical function that is not primitive recursive.
        It takes two non-negative integer arguments `m` and `n` and returns a single integer.
        """

    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Example usage
print(ackermann(2, 2))
print(f"Ackermann Function Calls (total, including recursive): {ackermann.calls}")
print(f"Ackermann Function Non-Recursive Calls: {ackermann.non_recursive_calls}")
print(f"Last Execution Time: {ackermann.last_time_taken:.6f} seconds")

