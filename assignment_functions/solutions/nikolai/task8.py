import time
from functools import wraps


def profiler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'last_time_taken'):
            wrapper.last_time_taken = 0
        if not hasattr(wrapper, 'calls'):
            wrapper.calls = 0

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        wrapper.last_time_taken = end - start
        wrapper.calls += 1

        return result

    return wrapper


@profiler
def ackermann(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))



print("res:", ackermann(3, 4))
print("time:", ackermann.last_time_taken)
print("calls:", ackermann.calls)
