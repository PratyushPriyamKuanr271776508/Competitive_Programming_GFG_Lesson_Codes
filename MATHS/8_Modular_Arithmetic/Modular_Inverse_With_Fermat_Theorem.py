def modular_inverse(a, p):
    """
    Calculate the modular inverse of a under modulo p using Fermat's
    Little Theorem.

    Fermat's Little Theorem states that for a prime p and any a not divisible
    by p, a^(p-1) = 1 (mod p). Hence a^(p-2) = a^(-1) (mod p).

    Parameters:
    a (int): The number to find the modular inverse for.
    p (int): A prime number representing the modulo.

    Returns:
    int: The modular inverse of a under modulo p.

    Note:
        Assumes p is prime and a is not a multiple of p. If p is not prime,
        the result is not a valid inverse.

    Time Complexity: O(log p)
        The built-in pow(a, p - 2, p) performs modular exponentiation, halving
        the exponent each step.

    Space Complexity: O(1)
        Modular exponentiation uses a constant number of variables.
    """
    if a == 0:
        raise ValueError("Inverse does not exist for 0.")

    # Using Fermat's Little Theorem: a^(p-1) = 1 (mod p),
    # therefore a^(p-2) = a^(-1) (mod p). pow does this in O(log p).
    return pow(a, p - 2, p)


if __name__ == "__main__":
    print(modular_inverse(3, 11))   # 4
    print(modular_inverse(10, 17))  # 12
    print(modular_inverse(7, 13))   # 2