def euler_totient(n):
    """
    Calculate Euler's Totient function phi(n) using the sqrt(n) approach.

    Uses the product formula phi(n) = n * PRODUCT(1 - 1/p) over each distinct
    prime p dividing n. We factor n by trial division up to sqrt(n), applying
    the (1 - 1/p) factor once per distinct prime.

    Parameters:
    n (int): The integer for which to calculate the totient function.

    Returns:
    int: The value of phi(n).

    Time Complexity: O(sqrt(n))
        Trial division tests candidate factors only up to sqrt(n); the inner
        while loop that strips out repeated factors runs a total of O(log n)
        times across the whole execution, so the sqrt(n) bound dominates.

    Space Complexity: O(1)
        Only a few integer variables are used regardless of the size of n.
    """
    res = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            # Remove all occurrences of prime factor p from n.
            while n % p == 0:
                n //= p
            # Apply the (1 - 1/p) factor: res = res - res/p.
            res -= res // p
        p += 1
    # If n > 1 here, the leftover n is a prime factor greater than sqrt(original n).
    if n > 1:
        res -= res // n
    return res