def extended_euclidean(a, b):
    """
    Return (g, x, y) for gcd(a, b) = g and Bezout coefficients x, y such
    that a*x + b*y = g.

    This implements the extended Euclidean algorithm recursively. Each step
    reduces the second argument using a modulo operation, preserving the gcd
    and building the coefficients for Bezout's identity.

    Time Complexity: O(log(min(|a|, |b|))) because the pair (a, b) is reduced by
    the modulo operation at each recursive step.
    Space Complexity: O(log(min(|a|, |b|))) due to recursion stack depth.
    """
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y
