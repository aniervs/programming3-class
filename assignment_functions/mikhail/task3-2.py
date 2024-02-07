def is_prime(n: int) -> bool:
    """
    Checks if a number n is prime or not.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Parameters:
    n (int): The number to check for primality.

    Returns:
    bool: True if n is prime, False otherwise.
    """

    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

# Example of using this function:
print(is_prime(11))  # True
print(is_prime(4))   # False
