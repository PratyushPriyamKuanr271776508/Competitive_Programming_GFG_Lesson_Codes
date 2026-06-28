# Divisors Practice Repository

This repository is a small practice collection focused entirely on divisor-related problems and implementations.

## Purpose

The goal of this project is to explore different ways of finding and working with divisors of a number, including:

- finding all divisors of a number
- using the square-root approach for efficiency
- printing divisors in sorted order
- testing divisor logic with sample inputs

## Project Structure

- [MATHS/2_Divisors](MATHS/2_Divisors) - Contains implementations for divisor-related problems.
  - [MATHS/2_Divisors/sqrtN_impl.py](MATHS/2_Divisors/sqrtN_impl.py) - Basic divisor finder using the square-root method.
  - [MATHS/2_Divisors/sqrtN_impl_sorted.py](MATHS/2_Divisors/sqrtN_impl_sorted.py) - Divisor finder that prints divisors in sorted order.
  - [MATHS/2_Divisors/nums_with_3_divisors.py](MATHS/2_Divisors/nums_with_3_divisors.py) - Prints numbers that have exactly three divisors, i.e. squares of primes.
  - [MATHS/2_Divisors/total_divisors_sqrtN_impl.py](MATHS/2_Divisors/total_divisors_sqrtN_impl.py) - Counts the total number of divisors using the square-root method.
  - [MATHS/2_Divisors/total_divisors_least_prime_impl.py](MATHS/2_Divisors/total_divisors_least_prime_impl.py) - Counts the total number of divisors using least prime factor logic.
  - [MATHS/2_Divisors/sum_of_divisors.py](MATHS/2_Divisors/sum_of_divisors.py) - Calculates the sum of all divisors of a number using prime factorization.
- [MATHS/3_Prime_Numbers/isPrime_sqrtN_impl.py](MATHS/3_Prime_Numbers/isPrime_sqrtN_impl.py) - Checks whether a number is prime using a square-root bound and 6k ± 1 optimization.

## Complexity Notes

- The square-root method in [MATHS/2_Divisors/total_divisors_sqrtN_impl.py](MATHS/2_Divisors/total_divisors_sqrtN_impl.py) runs in O(sqrt(n)) time and uses O(1) extra space.
- The least-prime-factor approach in [MATHS/2_Divisors/total_divisors_least_prime_impl.py](MATHS/2_Divisors/total_divisors_least_prime_impl.py) runs in O(n log log n) time for building the factor table and uses O(n) extra space.
- The sum-of-divisors in [MATHS/2_Divisors/sum_of_divisors.py](MATHS/2_Divisors/sum_of_divisors.py) runs in O(sqrt(n)) time and uses O(1) extra space, using the formula: σ(n) = ∏(p^(k+1) - 1) / (p - 1) for each prime power p^k in n's factorization.
- The prime check in [MATHS/3_Prime_Numbers/isPrime_sqrtN_impl.py](MATHS/3_Prime_Numbers/isPrime_sqrtN_impl.py) runs in O(sqrt(n)) time and uses O(1) extra space. It tests only 2, 3, and numbers of the form 6k ± 1 up to √n.

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
