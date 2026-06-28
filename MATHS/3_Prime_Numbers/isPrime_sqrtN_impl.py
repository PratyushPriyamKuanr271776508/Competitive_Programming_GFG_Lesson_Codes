import math


def isPrime(n):
    """Return True if n is a prime number, otherwise False.

    This implementation uses the 6k ± 1 optimization:
    - all primes greater than 3 are of the form 6k ± 1
    - first reject n <= 1, then handle 2 and 3 explicitly
    - skip multiples of 2 and 3
    - test only odd candidates up to sqrt(n)

    Time complexity: O(sqrt(n))
    Space complexity: O(1)
    """
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = math.isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True
