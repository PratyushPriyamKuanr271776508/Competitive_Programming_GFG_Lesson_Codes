def pow(base, exponent, mod):
    """
    Recursive binary (fast) modular exponentiation.

    Computes (base ^ exponent) mod using the identity:
        base^e = (base^2)^(e // 2)              if e is even
        base^e = (base^2)^(e // 2) * base       if e is odd
    Squaring the base while halving the exponent reduces the number of
    multiplications from e to about log2(e).

    Parameters:
    base (int): The base.
    exponent (int): The exponent (assumed non-negative).
    mod (int): The modulus.

    Returns:
    int: (base ^ exponent) mod.

    Note:
        This function is named `pow`, which shadows Python's built-in pow
        within this module. Consider renaming to mod_pow to avoid confusion.

    Time Complexity: O(log exponent)
        The exponent is halved on each recursive call.

    Space Complexity: O(log exponent)
        The recursion depth equals the number of halving steps.
    """
    # Base case: anything to the power 0 is 1.
    if exponent == 0:
        return 1
    # Square the base (mod) and halve the exponent.
    temp = pow(base * base % mod, exponent // 2, mod)
    # If the exponent bit is odd, multiply in one extra factor of base.
    if exponent % 2 == 1:
        temp = (temp * base) % mod
    return temp


if __name__ == "__main__":
    print(pow(3, 5, 11))    # 1
    print(pow(2, 10, 1000)) # 24
    print(pow(7, 0, 13))    # 1