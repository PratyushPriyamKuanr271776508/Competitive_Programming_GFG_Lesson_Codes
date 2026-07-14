def extended_euclidean(a, b):
    """
    Extended Euclidean algorithm.

    Computes gcd(a, b) along with Bezout coefficients x, y such that
    a*x + b*y = gcd(a, b).

    Time Complexity: O(log(min(a, b)))
        Each recursive call reduces the arguments like the Euclidean algorithm.

    Space Complexity: O(log(min(a, b)))
        The recursion depth matches the number of Euclidean steps.
    """
    # Base case: gcd(0, b) = b, with coefficients x = 0, y = 1.
    if a == 0:
        return b, 0, 1
    # Recurse on (b mod a, a), then back-substitute the coefficients.
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def inverse_mod(a, m):
    """
    Compute the modular multiplicative inverse of a modulo m.

    The inverse exists if and only if gcd(a, m) == 1; otherwise a ValueError
    is raised.

    Time Complexity: O(log(min(a, m)))
        Dominated by the single extended Euclidean call.

    Space Complexity: O(log(min(a, m)))
        Due to the recursion depth of the extended Euclidean call.
    """
    gcd, x, _ = extended_euclidean(a, m)
    # An inverse exists only when a and m are coprime.
    if gcd != 1:
        raise ValueError("Inverse does not exist")
    else:
        # x may be negative; normalize it into [0, m).
        return x % m


def chinese_remainder_theorem(a, n):
    """
    Solve a system of congruences x = a[i] (mod n[i]) via the Chinese
    Remainder Theorem.

    With N = product of all n[i], N_i = N / n[i], and m_i = inverse of N_i
    modulo n[i], the solution is x = sum(a[i] * m_i * N_i) mod N. Each term
    is 0 modulo every n[j] with j != i and equals a[i] modulo n[i], so the
    sum satisfies all congruences simultaneously.

    Parameters:
    a (list[int]): Remainders.
    n (list[int]): Moduli, assumed pairwise coprime.

    Returns:
    int: The unique solution x in [0, N).

    Preconditions:
        len(a) == len(n) and the moduli in n are pairwise coprime (required
        for each inverse_mod(N_i, n_i) to exist).

    Time Complexity: O(k log N)
        For k congruences, each iteration does an O(log n_i) modular inverse
        plus big-integer arithmetic on values up to N.

    Space Complexity: O(log(max n_i))
        Beyond the inputs, only the recursion of extended_euclidean and a few
        accumulator variables are used.
    """
    if len(a) != len(n):
        raise ValueError("Lists a and n must have the same length")

    # Product of all moduli.
    N = 1
    for ni in n:
        N *= ni

    x = 0
    for ai, ni in zip(a, n):
        Ni = N // ni              # product of all moduli except ni
        mi = inverse_mod(Ni, ni)  # inverse of Ni modulo ni
        # This term is congruent to ai mod ni and 0 mod every other modulus.
        x += ai * mi * Ni

    return x % N


if __name__ == "__main__":
    print(chinese_remainder_theorem([2, 3, 2], [3, 5, 7]))  # 23
    print(chinese_remainder_theorem([1, 2], [4, 5]))        # 17