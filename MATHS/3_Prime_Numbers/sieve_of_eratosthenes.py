def sieve_of_erathosthenes(n):
    """Return a boolean list isPrime[0..n] where isPrime[i] is True if i is prime.

    This uses the classic Sieve of Eratosthenes:
    - initialize all entries as potential primes
    - mark 0 and 1 as non-prime
    - for each prime p, mark multiples of p starting from p*p as non-prime

    Time complexity: O(n log log n)
    Space complexity: O(n)
    """
    isPrime = [True] * (n + 1)
    isPrime[0:2] = [False] * 2  # 0 and 1 are not prime

    p = 2
    while p * p <= n:
        if isPrime[p]:
            # Mark all multiples of p as composite, starting from p*p
            for i in range(p * p, n + 1, p):
                isPrime[i] = False
        p += 1

    return isPrime