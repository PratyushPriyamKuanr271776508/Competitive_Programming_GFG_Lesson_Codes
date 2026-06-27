def least_prime_factors(n):
    # least_prime[i] stores the smallest prime factor of i.
    # A value of 0 means it has not been assigned yet.
    least_prime = [0] * (n + 1)

    p = 2
    # Sieve-like approach: mark the smallest prime factor for each number.
    while p * p <= n:
        if least_prime[p] == 0:
            least_prime[p] = p
            for i in range(p * p, n + 1, p):
                if least_prime[i] == 0:
                    least_prime[i] = p
        p += 1

    # Any number left unassigned is a prime itself.
    for i in range(2, n + 1):
        if least_prime[i] == 0:
            least_prime[i] = i

    return least_prime


def count_divisors(n):
    # A number less than 1 has no positive divisors in this context.
    if n == 0:
        return 0
    if n == 1:
        return 1

    # We factorize n using the least prime factors and count the exponent of each prime.
    res = 1
    least_primes = least_prime_factors(n)
    prev_prime = least_primes[n]
    count = 1

    n //= prev_prime
    while n > 1:
        least_prime_n = least_primes[n]
        if least_prime_n == prev_prime:
            count += 1
        else:
            prev_prime = least_prime_n
            res *= (count + 1)
            count = 1
        n //= prev_prime

    res *= (count + 1)
    return res


# Time Complexity: O(n log log n) for building the least prime factor array,
# because this is a sieve-like process.
# Space Complexity: O(n) because we store an array of size n + 1.
# This approach is more structured than the simple sqrt(n) method and is useful
# when you want to factor numbers efficiently in repeated operations.