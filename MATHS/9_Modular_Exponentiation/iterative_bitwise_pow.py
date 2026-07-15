def pow(x, n, mod):
    """
    Iterative bitwise binary (fast) modular exponentiation.

    Computes (x ^ n) mod by scanning the bits of n from least to most
    significant. `temp` holds x^(2^k) for the current bit position k; whenever
    bit k of n is set, that power is multiplied into the running result.

    Parameters:
    x (int): The base.
    n (int): The exponent (assumed non-negative).
    mod (int): The modulus.

    Returns:
    int: (x ^ n) mod.

    Note:
        This function is named `pow`, which shadows Python's built-in pow
        within this module. Consider renaming to mod_pow to avoid confusion.

    Time Complexity: O(log n)
        The loop runs once per bit of n, and n is halved each iteration.

    Space Complexity: O(1)
        Only a constant number of variables are maintained (iterative, no
        recursion stack).
    """
    temp = x    # temp = x^(2^k) for the current bit position k
    res = 1
    while n > 0:
        # If the current lowest bit is set, include this power of x.
        if n & 1:
            res = (res * temp) % mod
        # Square the base for the next-higher bit and shift the exponent.
        temp = (temp * temp) % mod
        n >>= 1
    return res


if __name__ == "__main__":
    print(pow(3, 5, 11))    # 1
    print(pow(2, 10, 1000)) # 24
    print(pow(7, 0, 13))    # 1