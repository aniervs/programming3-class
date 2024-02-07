
from math import sqrt

def is_prime(n: int) -> bool:

    """
        A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
        If the number is less than 2, it's not prime.
        This function checks divisibility by all numbers up to the square root of n to determine
        which number are prime.
        """

    if n < 2:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


print(f"1: {is_prime(1)}")
print(f"2: {is_prime(2)}")
print(f"3: {is_prime(3)}")
print(f"4: {is_prime(4)}")
print(f"7: {is_prime(7)}")
print(f"9: {is_prime(9)}")



