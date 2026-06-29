def lcm_2nums(a, b):
    """
    Return the least common multiple of two numbers using a brute-force
    approach.

    This implementation checks multiples of the larger of the two input values
    until it finds the first number divisible by both numbers.

    Time Complexity: O(lcm(a, b) / max(a, b)) in the worst case, which is
    proportional to the number of candidate multiples tested before the LCM is
    found. In practice, this can be as large as O(min(a, b)) for the first
    common multiple after the maximum input.
    Space Complexity: O(1), because it uses only a constant amount of extra
    space.
    """
    if a == 0 or b == 0:
        return 0

    res = max(a, b)
    while True:
        if res % a == 0 and res % b == 0:
            return res
        res += 1