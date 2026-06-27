# A number has exactly 3 divisors if and only if it is the square of a prime.
# This function prints all such numbers up to n.
def print3divNums(n):
    # isPrime[i] will be True if i is considered prime so far
    isPrime = [True] * (n + 1)
    p = 2

    while p * p <= n:
        if isPrime[p]:
            # Every prime p gives one valid number: p^2
            print(p * p)

            # Mark multiples of p as non-prime
            for i in range(p * p, n + 1, p):
                isPrime[i] = False
        p += 1