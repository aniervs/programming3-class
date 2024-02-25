def is_prime(n: int) -> bool:
    """
    Checks if the given number n is a prime number.

    Args:
    - n: The number to check for primality.

    Returns:
    - bool: True if n is prime, False otherwise.
    """
    if n < 2 or (n > 2 and n % 2 == 0):
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(2))  # Should return True
print(is_prime(11))  # Should return True
print(is_prime(4))  # Should return False
