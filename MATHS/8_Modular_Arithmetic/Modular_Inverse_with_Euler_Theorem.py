from math import gcd


def totient_function(n):
    """
    Calculate Euler's Totient function phi(n) using the sqrt(n) approach.

    Uses the product formula phi(n) = n * PRODUCT(1 - 1/p) over each distinct
    prime p dividing n, factoring n by trial division up to sqrt(n).

    Time Complexity: O(sqrt(n))
        Trial division tests factors only up to sqrt(n); the inner loop that
        strips repeated factors runs O(log n) times in total, so sqrt(n)
        dominates.

    Space Complexity: O(1)
        Only a few integer variables are used.
    """
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            # Remove all copies of prime factor p.
            while n % p == 0:
                n //= p
            # Apply the (1 - 1/p) factor.
            result -= result // p
        p += 1
    # Leftover n > 1 is a prime factor larger than sqrt(original n).
    if n > 1:
        result -= result // n
    return result


def exponentiation(a, b, m):
    """
    Calculate (a^b) mod m using binary (fast) exponentiation.

    Squares the base while halving the exponent, multiplying the result in
    whenever the current exponent bit is set.

    Time Complexity: O(log b)
        The exponent is halved each iteration.

    Space Complexity: O(1)
        Only a constant number of variables are maintained.
    """
    result = 1
    a = a % m
    while b > 0:
        # If the lowest bit of b is 1, include the current power of a.
        if b % 2 == 1:
            result = (result * a) % m
        # Square the base and move to the next bit.
        a = (a * a) % m
        b //= 2
    return result


def mod_inverrse_euler(a, m):
    """
    Calculate the modular inverse of a mod m using Euler's theorem.

    When gcd(a, m) = 1, Euler's theorem gives a^phi(m) = 1 (mod m), so the
    inverse is a^(phi(m) - 1) mod m.

    Returns:
    int | None: The inverse of a mod m, or None if gcd(a, m) != 1.

    Time Complexity: O(sqrt(m) + log(phi(m))) = O(sqrt(m))
        Dominated by computing phi(m) in O(sqrt(m)); the modular exponentiation
        adds O(log(phi(m))), which is smaller.

    Space Complexity: O(1)
        Both helper routines use constant extra space.
    """
    # An inverse exists only when a and m are coprime.
    if gcd(a, m) != 1:
        return None  # Inverse doesn't exist if a and m are not coprime
    phi_m = totient_function(m)
    # a^(phi(m) - 1) is the inverse of a modulo m.
    return exponentiation(a, phi_m - 1, m)


if __name__ == "__main__":
    print(mod_inverrse_euler(3, 11))   # 4
    print(mod_inverrse_euler(10, 17))  # 12
    print(mod_inverrse_euler(4, 8))    # None (not coprime)