def count_divisors(n):
    # If n is not positive, it cannot have any positive divisors.
    if n <= 0:
        return 0

    # 1 has exactly one positive divisor: itself.
    if n == 1:
        return 1

    count = 0
    i = 1

    # We only need to check values up to sqrt(n).
    # For each such i, if it divides n, then n // i is its paired divisor.
    while i * i <= n:
        if n % i == 0:
            count += 1
            if n // i != i:  # Avoid counting the square root twice.
                count += 1
        i += 1

    return count


# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)
# This approach is efficient because we only iterate up to the square root of n.
