import time
import functools

def profiler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        wrapper.calls += 1
        result = func(*args, **kwargs)
        wrapper.last_time_taken = time.time() - start_time
        return result

    wrapper.calls = 0
    wrapper.last_time_taken = 0
    return wrapper

@profiler
def ackermann(m, n):
    """Ackermann function"""
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Example usage
print(ackermann(3, 2))
print("Calls:", ackermann.calls)
print("Last time taken:", ackermann.last_time_taken, "seconds")
