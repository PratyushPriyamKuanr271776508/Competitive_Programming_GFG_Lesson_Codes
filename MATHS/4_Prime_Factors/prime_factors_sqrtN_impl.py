def print_prime_factors(n):
    """
    Print all prime factors of n in ascending order.

    The function repeatedly divides n by the smallest possible prime factor.
    """
    if n <= 1:
        print("No prime factors for numbers less than or equal to 1")
        return

    p = 2
    # Check divisors up to sqrt(n); every division reduces n, making the loop efficient.
    while p * p <= n:
        while n % p == 0:
            print(p)
            n //= p
        p += 1

    if n > 1:
        print(n)


# Time complexity: O(sqrt(n)) in the worst case
# Space complexity: O(1) extra space