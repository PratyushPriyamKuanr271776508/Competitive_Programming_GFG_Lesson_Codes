def optimized_euclidean_gcd(a, b):
    """
    Return the greatest common divisor of two numbers using the optimized
    Euclidean algorithm.

    This is the standard Euclidean algorithm. In each iteration, it replaces
    the pair (a, b) with (b, a % b), which preserves the gcd and quickly
    reduces the numbers.

    Time Complexity: O(log(min(a, b))) in the average and worst case for the
    standard Euclidean algorithm, because the remainder decreases rapidly.
    Space Complexity: O(1), because it uses only a constant amount of extra
    space.
    """
    if a > b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a
