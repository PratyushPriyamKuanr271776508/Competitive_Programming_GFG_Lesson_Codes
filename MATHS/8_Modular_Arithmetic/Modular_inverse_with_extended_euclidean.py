def extended_euclidean(a, b):
    """
    Extended Euclidean algorithm.

    Computes gcd(a, b) along with Bezout coefficients x, y such that
    a*x + b*y = gcd(a, b).

    Parameters:
    a (int): First integer.
    b (int): Second integer.

    Returns:
    tuple[int, int, int]: (gcd, x, y) satisfying a*x + b*y = gcd.

    Time Complexity: O(log(min(a, b)))
        Each recursive call reduces the arguments like the Euclidean algorithm,
        where the smaller value shrinks at least geometrically.

    Space Complexity: O(log(min(a, b)))
        The recursion depth matches the number of Euclidean steps, and each
        frame holds a constant number of variables on the call stack.
    """
    # Base case: gcd(0, b) = b, with coefficients x = 0, y = 1.
    if a == 0:
        return b, 0, 1
    # Recurse on (b mod a, a); then back-substitute the coefficients.
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def modular_inverse(a, m):
    """
    Compute the modular multiplicative inverse of a modulo m.

    Finds an integer in [0, m) whose product with a is congruent to 1 mod m.
    The inverse exists if and only if gcd(a, m) == 1.

    Parameters:
    a (int): The value whose inverse is sought.
    m (int): The modulus.

    Returns:
    int | None: The inverse of a mod m in [0, m), or None if it does not exist.

    Time Complexity: O(log(min(a, m)))
        Dominated by the single extended Euclidean call.

    Space Complexity: O(log(min(a, m)))
        Due to the recursion depth of the extended Euclidean call.
    """
    gcd, x, _ = extended_euclidean(a, m)
    # An inverse exists only when a and m are coprime.
    if gcd != 1:
        return None
    else:
        # x may be negative; normalize it into the range [0, m).
        return x % m