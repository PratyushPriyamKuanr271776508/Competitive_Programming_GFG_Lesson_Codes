# Divisors Practice Repository

This repository is a small practice collection focused entirely on divisor-related problems and implementations.

## Purpose

The goal of this project is to explore different ways of finding and working with divisors and prime factors of a number, including:

- finding all divisors of a number
- using the square-root approach for efficiency
- printing divisors in sorted order
- finding prime factors of a number
- testing divisor and prime-factor logic with sample inputs

## Project Structure

- [MATHS/2_Divisors](MATHS/2_Divisors) - Contains implementations for divisor-related problems.
  - [MATHS/2_Divisors/sqrtN_impl.py](MATHS/2_Divisors/sqrtN_impl.py) - Basic divisor finder using the square-root method.
  - [MATHS/2_Divisors/sqrtN_impl_sorted.py](MATHS/2_Divisors/sqrtN_impl_sorted.py) - Divisor finder that prints divisors in sorted order.
  - [MATHS/2_Divisors/nums_with_3_divisors.py](MATHS/2_Divisors/nums_with_3_divisors.py) - Prints numbers that have exactly three divisors, i.e. squares of primes.
  - [MATHS/2_Divisors/total_divisors_sqrtN_impl.py](MATHS/2_Divisors/total_divisors_sqrtN_impl.py) - Counts the total number of divisors using the square-root method.
  - [MATHS/2_Divisors/total_divisors_least_prime_impl.py](MATHS/2_Divisors/total_divisors_least_prime_impl.py) - Counts the total number of divisors using least prime factor logic.
  - [MATHS/2_Divisors/sum_of_divisors.py](MATHS/2_Divisors/sum_of_divisors.py) - Calculates the sum of all divisors of a number using prime factorization.
- [MATHS/3_Prime_Numbers/isPrime_sqrtN_impl.py](MATHS/3_Prime_Numbers/isPrime_sqrtN_impl.py) - Checks whether a number is prime using a square-root bound and 6k ± 1 optimization.
  - [MATHS/3_Prime_Numbers/sieve_of_eratosthenes.py](MATHS/3_Prime_Numbers/sieve_of_eratosthenes.py) - Generates a boolean prime table up to n using the Sieve of Eratosthenes.
- [MATHS/4_Prime_Factors/prime_factors_sqrtN_impl.py](MATHS/4_Prime_Factors/prime_factors_sqrtN_impl.py) - Prints the prime factors of a number using the square-root approach by repeatedly dividing by the current prime factor.
- [MATHS/5_GCD/gcd_2nums_min(a_b)_impl.py](MATHS/5_GCD/gcd_2nums_min(a_b)_impl.py) - Finds the GCD by checking divisors from the smaller input down to 1. This is a correct brute-force implementation with O(min(a, b)) time and O(1) extra space.
- [MATHS/5_GCD/gcd_2nums_euclidean_impl.py](MATHS/5_GCD/gcd_2nums_euclidean_impl.py) - Finds the GCD using the Euclidean algorithm with repeated subtraction. This is a correct implementation with O(max(a, b)) time and O(1) extra space in the subtraction-based form.
- [MATHS/5_GCD/gcd_2nums_optimized_euclidean_impl.py](MATHS/5_GCD/gcd_2nums_optimized_euclidean_impl.py) - Finds the GCD using the optimized Euclidean algorithm with modulo reduction. This is the standard efficient form with O(log(min(a, b))) time and O(1) extra space.
- [MATHS/5_GCD/lcm_2nums_brute_impl.py](MATHS/5_GCD/lcm_2nums_brute_impl.py) - Finds the LCM by checking multiples of the larger input until a common multiple is found. This is a correct brute-force implementation with O(lcm(a, b) / max(a, b)) time and O(1) extra space.
- [MATHS/5_GCD/lcm_2nums_euclidean_impl.py](MATHS/5_GCD/lcm_2nums_euclidean_impl.py) - Finds the LCM using the Euclidean algorithm through the identity lcm(a, b) = (a * b) // gcd(a, b). This is an efficient implementation with O(log(min(a, b))) time and O(1) extra space.
- [MATHS/5_GCD/extended_euclidean_impl.py](MATHS/5_GCD/extended_euclidean_impl.py) - Computes gcd(a, b) and Bézout coefficients x, y such that a*x + b*y = gcd(a, b). This uses the extended Euclidean algorithm with O(log(min(|a|, |b|))) time and O(log(min(|a|, |b|))) space due to recursion.
- [MATHS/5_GCD/diophantine_equation_impl.py](MATHS/5_GCD/diophantine_equation_impl.py) - Solves the linear Diophantine equation a*x + b*y = c using extended Euclidean coefficients. This implementation returns a particular integer solution if one exists, in O(log(min(|a|, |b|))) time and O(log(min(|a|, |b|))) space.
- [MATHS/6_Mathematical_Principles/numbers_till_n_divisible_by_3_and_5.py](MATHS/6_Mathematical_Principles/numbers_till_n_divisible_by_3_and_5.py) - Counts numbers from 1 to n that are divisible by 3 or 5 using the inclusion-exclusion principle. This is an O(1) time and O(1) space implementation.
- [MATHS/6_Mathematical_Principles/derangements.py](MATHS/6_Mathematical_Principles/derangements.py) - Computes the number of derangements for n objects using the recurrence D(n) = (n - 1)(D(n - 1) + D(n - 2)). This is an O(n) time and O(1) space implementation.
- [MATHS/6_Mathematical_Principles/find_start_end_idx_for_subarray_sum_divisible_by_size_of_arr.py](MATHS/6_Mathematical_Principles/find_start_end_idx_for_subarray_sum_divisible_by_size_of_arr.py) - Finds the start and end indices of a subarray whose sum is divisible by the size of the array, using the pigeonhole principle on prefix-sum remainders.
- [MATHS/7_Euler_Totient_Function/euler_totient_brute.py](MATHS/7_Euler_Totient_Function/euler_totient_brute.py) - Computes Euler's Totient function φ(n) by counting integers from 1 to n that are coprime with n (gcd(i, n) == 1). This is a correct brute-force implementation with O(n log n) time and O(1) extra space.
- [MATHS/7_Euler_Totient_Function/euler_totient_sqrt(n).py](MATHS/7_Euler_Totient_Function/euler_totient_sqrt(n).py) - Computes Euler's Totient function φ(n) using the product formula φ(n) = n·∏(1 - 1/p) over distinct primes p, factoring n by trial division up to √n. This is a correct and efficient implementation with O(sqrt(n)) time and O(1) extra space.
- [MATHS/7_Euler_Totient_Function/euler_totient_nlogn_impl.py](MATHS/7_Euler_Totient_Function/euler_totient_nlogn_impl.py) - Computes Euler's Totient function φ for all values up to n using a sieve based on the divisor-sum identity n = Σ_{d|n} φ(d), subtracting each finalized φ(p) from its multiples. This is a correct implementation with O(n log n) time and O(n) extra space.
- [MATHS/8_Modular_Arithmetic/Modular_inverse_with_extended_euclidean.py](MATHS/8_Modular_Arithmetic/Modular_inverse_with_extended_euclidean.py) - Computes the modular multiplicative inverse of a modulo m using the extended Euclidean algorithm, returning None when gcd(a, m) ≠ 1. This is a correct implementation with O(log(min(a, m))) time and O(log(min(a, m))) space due to recursion.

## Complexity Notes

- The square-root method in [MATHS/2_Divisors/total_divisors_sqrtN_impl.py](MATHS/2_Divisors/total_divisors_sqrtN_impl.py) runs in O(sqrt(n)) time and uses O(1) extra space.
- The least-prime-factor approach in [MATHS/2_Divisors/total_divisors_least_prime_impl.py](MATHS/2_Divisors/total_divisors_least_prime_impl.py) runs in O(n log log n) time for building the factor table and uses O(n) extra space.
- The sum-of-divisors in [MATHS/2_Divisors/sum_of_divisors.py](MATHS/2_Divisors/sum_of_divisors.py) runs in O(sqrt(n)) time and uses O(1) extra space, using the formula: σ(n) = ∏(p^(k+1) - 1) / (p - 1) for each prime power p^k in n's factorization.
- The prime check in [MATHS/3_Prime_Numbers/isPrime_sqrtN_impl.py](MATHS/3_Prime_Numbers/isPrime_sqrtN_impl.py) runs in O(sqrt(n)) time and uses O(1) extra space. It tests only 2, 3, and numbers of the form 6k ± 1 up to √n.
- The sieve in [MATHS/3_Prime_Numbers/sieve_of_eratosthenes.py](MATHS/3_Prime_Numbers/sieve_of_eratosthenes.py) runs in O(n log log n) time and uses O(n) space to build a prime table up to n.
- The prime factor finder in [MATHS/4_Prime_Factors/prime_factors_sqrtN_impl.py](MATHS/4_Prime_Factors/prime_factors_sqrtN_impl.py) runs in O(sqrt(n)) time and uses O(1) extra space, because it tests possible divisors only up to √n while repeatedly dividing the number.
- The GCD implementation in [MATHS/5_GCD/gcd_2nums_min(a_b)_impl.py](MATHS/5_GCD/gcd_2nums_min(a_b)_impl.py) runs in O(min(a, b)) time and uses O(1) extra space, because it checks each candidate divisor from the smaller input down to 1.
- The Euclidean GCD implementation in [MATHS/5_GCD/gcd_2nums_euclidean_impl.py](MATHS/5_GCD/gcd_2nums_euclidean_impl.py) runs in O(max(a, b)) time and uses O(1) extra space in this subtraction-based form, because each step subtracts one value from the other while preserving the gcd.
- The optimized Euclidean GCD implementation in [MATHS/5_GCD/gcd_2nums_optimized_euclidean_impl.py](MATHS/5_GCD/gcd_2nums_optimized_euclidean_impl.py) runs in O(log(min(a, b))) time and uses O(1) extra space, because each modulo step shrinks the problem size exponentially faster than repeated subtraction.
- The extended Euclidean implementation in [MATHS/5_GCD/extended_euclidean_impl.py](MATHS/5_GCD/extended_euclidean_impl.py) runs in O(log(min(|a|, |b|))) time and uses O(log(min(|a|, |b|))) space, because the recursive algorithm repeatedly reduces the second argument and builds Bézout coefficients on the call stack.
- The Diophantine equation implementation in [MATHS/5_GCD/diophantine_equation_impl.py](MATHS/5_GCD/diophantine_equation_impl.py) runs in O(log(min(|a|, |b|))) time and uses O(log(min(|a|, |b|))) space, because it relies on the extended Euclidean algorithm and scales the Bézout coefficients to solve a*x + b*y = c.
- The inclusion-exclusion implementation in [MATHS/6_Mathematical_Principles/numbers_till_n_divisible_by_3_and_5.py](MATHS/6_Mathematical_Principles/numbers_till_n_divisible_by_3_and_5.py) runs in O(1) time and uses O(1) extra space, because it computes the three floor divisions directly.
- The derangements implementation in [MATHS/6_Mathematical_Principles/derangements.py](MATHS/6_Mathematical_Principles/derangements.py) runs in O(n) time and uses O(1) extra space, because it iteratively applies the recurrence using only two previous values.
- The Euclidean LCM implementation in [MATHS/5_GCD/lcm_2nums_euclidean_impl.py](MATHS/5_GCD/lcm_2nums_euclidean_impl.py) runs in O(log(min(a, b))) time and uses O(1) extra space, because it computes the gcd with the Euclidean algorithm and then derives the LCM in constant time.
- The extended Euclidean implementation in [MATHS/5_GCD/extended_euclidean_impl.py](MATHS/5_GCD/extended_euclidean_impl.py) runs in O(log(min(|a|, |b|))) time and uses O(log(min(|a|, |b|))) space, because the recursive algorithm repeatedly reduces the second argument and builds Bezout coefficients on the call stack.
- The pigeonhole-based implementation in [MATHS/6_Mathematical_Principles/find_start_end_idx_for_subarray_sum_divisible_by_size_of_arr.py](MATHS/6_Mathematical_Principles/find_start_end_idx_for_subarray_sum_divisible_by_size_of_arr.py) runs in O(n) time and uses O(n) extra space, because it computes prefix sums modulo n and uses the pigeonhole principle (n+1 prefix remainders into n possible values) to guarantee two indices with the same remainder, giving a subarray whose sum is divisible by n.
- The Euler Totient implementation in [MATHS/7_Euler_Totient_Function/euler_totient_brute.py](MATHS/7_Euler_Totient_Function/euler_totient_brute.py) runs in O(n log n) time and uses O(1) extra space, because it loops over all integers from 1 to n and calls the Euclidean gcd (O(log n)) for each, while keeping only a single counter.
- The sqrt(n) Euler Totient implementation in [MATHS/7_Euler_Totient_Function/euler_totient_sqrt(n).py](MATHS/7_Euler_Totient_Function/euler_totient_sqrt(n).py) runs in O(sqrt(n)) time and uses O(1) extra space, because it factors n by trial division up to √n and applies the (1 - 1/p) factor once per distinct prime, using only a few scalar variables.
- The sieve-based Euler Totient implementation in [MATHS/7_Euler_Totient_Function/euler_totient_nlogn_impl.py](MATHS/7_Euler_Totient_Function/euler_totient_nlogn_impl.py) runs in O(n log n) time and uses O(n) extra space, because the outer loop runs n times and each p iterates over its ~n/p multiples (summing to n·H(n) ~ n log n), while an array of size n + 1 stores the totient of every value up to n.
- The modular inverse implementation in [MATHS/8_Modular_Arithmetic/Modular_inverse_with_extended_euclidean.py](MATHS/8_Modular_Arithmetic/Modular_inverse_with_extended_euclidean.py) runs in O(log(min(a, m))) time and uses O(log(min(a, m))) space, because it relies on a single recursive extended Euclidean call to obtain the Bézout coefficient x and then normalizes x mod m in constant time.

## How to Run

You can run any Python file directly:

```bash
python MATHS/2_Divisors/sqrtN_impl.py
```

Or for the sorted version:

```bash
python MATHS/2_Divisors/sqrtN_impl_sorted.py
```

## Notes

This repository is intentionally centered around the topic of divisors, making it a simple and focused practice space for number theory and problem-solving concepts.

As new divisor-related programs and examples are added in the future, this README should be updated to keep the project documentation accurate and consistent.