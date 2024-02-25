import time
from functools import wraps

def profiler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'is_running'):
            wrapper.is_running = True
            wrapper.calls = 0
            start_time = time.perf_counter()

        wrapper.calls += 1
        result = func(*args, **kwargs)

        if wrapper.is_running:
            end_time = time.perf_counter()
            wrapper.last_time_taken = end_time - start_time
            wrapper.is_running = False

        return result

    wrapper.is_running = False
    wrapper.calls = 0
    wrapper.last_time_taken = 0
    return wrapper

@profiler
def ackermann(n: int, m: int) -> int:
    """
    Ackermann function, a classic example of a recursive function.
    """
    if n == 0:
        return m + 1
    if m == 0:
        return ackermann(n - 1, 1)
    return ackermann(n - 1, ackermann(n, m - 1))

print(ackermann(2, 1))  
print(f"Time taken: {ackermann.last_time_taken}, Calls: {ackermann.calls}")
