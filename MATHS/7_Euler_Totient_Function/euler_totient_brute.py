from math import gcd


def euler_totient(n):
    """
    Calculate the Euler's Totient function phi(n) for a given integer n.

    The Euler's Totient function counts the positive integers up to a given
    integer n that are relatively prime to n (i.e. gcd(i, n) == 1).

    Parameters:
    n (int): The integer for which to calculate the totient function.

    Returns:
    int: The value of phi(n).

    Time Complexity: O(n log n)
        The loop runs n times, and each iteration calls gcd(i, n), which
        uses the Euclidean algorithm running in O(log n). Multiplying the
        two gives O(n log n) overall.

    Space Complexity: O(1)
        Only a single counter is maintained regardless of the size of n.
        (The recursive/iterative gcd uses O(log n) at most, but the standard
        library gcd is iterative and uses O(1) auxiliary space.)
    """
    if n < 1:
        raise ValueError("Input must be a positive integer.")

    count = 0
    # Check every integer from 1 to n and count those coprime with n.
    for i in range(1, n + 1):
        if gcd(i, n) == 1:  # i and n share no common factor other than 1
            count += 1
    return count


if __name__ == "__main__":
    for x in [1, 6, 10, 12, 36]:
        print(f"phi({x}) = {euler_totient(x)}")