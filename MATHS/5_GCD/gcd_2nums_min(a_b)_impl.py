def gcd_of_2nums(a, b):
    """
    Return the greatest common divisor of two numbers.

    This is a straightforward brute-force approach that checks divisors
    starting from the smaller of the two numbers and moving downward.
    Time Complexity: O(min(a, b)) in the worst case, because the loop may
    test every value from min(a, b) down to 1.
    Space Complexity: O(1), because it uses only a constant amount of extra
    space for the loop variable and temporary comparisons.
    """
    if a == 0:
        return b
    if b == 0:
        return a

    res = min(a, b)
    while res > 1:
        if a % res == 0 and b % res == 0:
            return res
        res -= 1

    return res
