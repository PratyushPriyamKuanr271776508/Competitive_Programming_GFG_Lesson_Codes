def sum_of_divisors(n):
    # Edge cases: sum of divisors of 0 is 0, and 1 is 1.
    if n == 0 or n == 1:
        return n

    res = 1
    p = 2

    # Prime factorization using trial division up to sqrt(n).
    while p * p <= n:
        if n % p == 0:
            cnt = 0
            # Count the exponent of prime p in n.
            while n % p == 0:
                cnt += 1
                n //= p

            # Apply the divisor sum formula for this prime:
            # If p^cnt is a prime power factor, its contribution is (p^(cnt+1) - 1) / (p - 1).
            res *= (p ** (cnt + 1) - 1) // (p - 1)

        p += 1

    # If n > 1 at this point, then n itself is a prime factor > sqrt(original n).
    # Its contribution to the divisor sum is (n^2 - 1) / (n - 1) = n + 1.
    if n > 1:
        res *= (n + 1)

    return res


# Time Complexity: O(sqrt(n))
# We iterate through all numbers from 2 to sqrt(n), checking divisibility.
# For each prime factor found, we divide n by that prime until it's no longer divisible.
# Overall, the loop runs at most O(sqrt(n)) iterations.

# Space Complexity: O(1)
# We only use a constant amount of extra space for variables (res, p, cnt, n).
# No data structures that grow with n are used.
