def euler_totient(n):
    """
    Compute Euler's Totient function phi(n) using a sieve based on the
    divisor-sum identity:  n = SUM over d | n of phi(d).

    Rearranged, phi(n) = n - SUM of phi(d) for every proper divisor d of n.
    We initialize euler[i] = i - 1, which already accounts for the divisor
    d = 1 (phi(1) = 1) for every i. Then for each p from 2 upward we subtract
    the (now final) euler[p] from all its multiples. Processing p in increasing
    order ensures every proper divisor of a number has contributed before that
    number is read.

    Parameters:
    n (int): The integer for which to calculate the totient function.

    Returns:
    int: The value of phi(n).

    Time Complexity: O(n log n)
        The outer loop runs n times; for each p the inner loop runs about n/p
        times. Summing n/p over p from 2 to n gives n * H(n) ~ O(n log n).

    Space Complexity: O(n)
        An array of size n + 1 is maintained to hold the totient of every
        value from 0 to n.
    """
    if n < 1:
        raise ValueError("Input must be a positive integer.")

    # euler[i] starts at i - 1, pre-subtracting phi(1) = 1 (divisor d = 1).
    euler = [i - 1 for i in range(n + 1)]
    euler[0], euler[1] = 0, 1

    for p in range(2, n + 1):
        div = p
        # euler[p] is final here; subtract it from every multiple 2p, 3p, ...
        for i in range(div * 2, n + 1, div):
            euler[i] -= euler[div]

    return euler[n]


if __name__ == "__main__":
    for x in [1, 6, 10, 12, 36]:
        print(f"phi({x}) = {euler_totient(x)}")