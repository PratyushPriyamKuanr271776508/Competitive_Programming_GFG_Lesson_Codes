def gcd_euclidean(a, b):
    """
    Return the greatest common divisor of two numbers using the Euclidean
    algorithm with repeated subtraction.

    This implementation is correct because each step replaces the larger of the
    two numbers with the difference between them, preserving the gcd.

    Time Complexity: O(max(a, b)) in the worst case for this subtraction-based
    version, because each subtraction can reduce the larger value by at most one
    step per iteration and the number of iterations is proportional to the
    larger input.
    Space Complexity: O(1), because it uses only a constant amount of extra
    space.
    """
    if a == 0:
        return b
    if b == 0:
        return a

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


    