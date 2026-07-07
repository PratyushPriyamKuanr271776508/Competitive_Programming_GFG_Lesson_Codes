def compute_inverse(n, mod):
    """
    Compute the modular inverses of all integers from 1 to n modulo mod.

    Uses the classic linear recurrence for inverses modulo a prime. Writing
    mod = floor(mod / i) * i + (mod mod i), reducing modulo mod and solving
    for i^(-1) gives:

        i^(-1) = -floor(mod / i) * (mod mod i)^(-1)   (mod mod)

    Because (mod mod i) < i, its inverse is already known, so each value is
    filled in O(1) from an earlier entry.

    Parameters:
    n (int): The upper limit of the range (inclusive).
    mod (int): The modulus for which to compute the inverses.

    Returns:
    list: A list where index i holds i^(-1) mod (for 1 <= i <= n).

    Preconditions:
        mod must be prime and n < mod, so that every i in [1, n] is invertible
        and mod % i is never 0.

    Time Complexity: O(n)
        A single pass fills each of the n entries with constant work.

    Space Complexity: O(n)
        An array of size n + 1 stores every inverse from 1 to n.
    """
    inverses = [0] * (n + 1)
    inverses[1] = 1  # The modular inverse of 1 is always 1

    for i in range(2, n + 1):
        # i^(-1) = -(mod // i) * inverses[mod % i], taken mod `mod`.
        # The outer (... % mod) and leading `mod -` keep the result in [0, mod).
        inverses[i] = (mod - (mod // i) * inverses[mod % i] % mod) % mod

    return inverses


if __name__ == "__main__":
    print(compute_inverse(10, 11))  # [0, 1, 6, 4, 3, 9, 2, 8, 7, 5, 10]