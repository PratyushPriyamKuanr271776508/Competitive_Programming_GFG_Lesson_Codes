# Competitive Programming — Mathematical Algorithms

A focused practice collection of number-theory and computational-geometry algorithms implemented in Python. Each file is a small, self-contained implementation of a single classic technique, annotated with its time and space complexity.

> The project began as a divisors-only practice space and has since grown to cover prime numbers, GCD/LCM, modular arithmetic, modular exponentiation, and geometric algorithms.

## Topics Covered

- **Divisors** — enumerating divisors, counting them, and summing them
- **Prime numbers** — primality testing and sieving
- **Prime factorization** — extracting prime factors efficiently
- **GCD & LCM** — brute-force, Euclidean, extended Euclidean, and Diophantine equations
- **Combinatorial / counting principles** — inclusion–exclusion, derangements, pigeonhole
- **Euler's Totient function** — brute-force, √n factorization, and sieve variants
- **Modular arithmetic** — modular inverses (several methods) and the Chinese Remainder Theorem
- **Modular exponentiation** — scalar and matrix fast exponentiation
- **Geometric algorithms** — orientation, segment intersection, and convex hull

## Repository Layout

All code lives under `MATHS/`, grouped into numbered topic folders. Complexities are stated per file; `n`/`N` denotes the primary input size and `a`, `b`, `m`, `p` denote numeric operands.

### `2_Divisors`

| File | Description | Time | Space |
|------|-------------|------|-------|
| [`sqrtN_impl.py`](MATHS/2_Divisors/sqrtN_impl.py) | All divisors of a number via the √n method | O(√n) | O(1) |
| [`sqrtN_impl_sorted.py`](MATHS/2_Divisors/sqrtN_impl_sorted.py) | Divisors printed in sorted order | O(√n) | O(√n) |
| [`nums_with_3_divisors.py`](MATHS/2_Divisors/nums_with_3_divisors.py) | Numbers with exactly three divisors (squares of primes) | — | — |
| [`total_divisors_sqrtN_impl.py`](MATHS/2_Divisors/total_divisors_sqrtN_impl.py) | Count of divisors via the √n method | O(√n) | O(1) |
| [`total_divisors_least_prime_impl.py`](MATHS/2_Divisors/total_divisors_least_prime_impl.py) | Count of divisors via least-prime-factor table | O(n log log n) build | O(n) |
| [`sum_of_divisors.py`](MATHS/2_Divisors/sum_of_divisors.py) | Sum of divisors σ(n) = ∏ (pᵏ⁺¹ − 1)/(p − 1) via factorization | O(√n) | O(1) |

### `3_Prime_Numbers`

| File | Description | Time | Space |
|------|-------------|------|-------|
| [`isPrime_sqrtN_impl.py`](MATHS/3_Prime_Numbers/isPrime_sqrtN_impl.py) | Primality test with a √n bound and 6k ± 1 optimization | O(√n) | O(1) |
| [`sieve_of_eratosthenes.py`](MATHS/3_Prime_Numbers/sieve_of_eratosthenes.py) | Boolean prime table up to n | O(n log log n) | O(n) |

### `4_Prime_Factors`

| File | Description | Time | Space |
|------|-------------|------|-------|
| [`prime_factors_sqrtN_impl.py`](MATHS/4_Prime_Factors/prime_factors_sqrtN_impl.py) | Prime factors via repeated division up to √n | O(√n) | O(1) |

### `5_GCD`

| File | Description | Time | Space |
|------|-------------|------|-------|
| [`gcd_2nums_min(a_b)_impl.py`](MATHS/5_GCD/gcd_2nums_min%28a_b%29_impl.py) | GCD by brute-force divisor scan from min(a, b) down | O(min(a, b)) | O(1) |
| [`gcd_2nums_euclidean_impl.py`](MATHS/5_GCD/gcd_2nums_euclidean_impl.py) | GCD via subtraction-based Euclidean algorithm | O(max(a, b)) | O(1) |
| [`gcd_2nums_optimized_euclidean_impl.py`](MATHS/5_GCD/gcd_2nums_optimized_euclidean_impl.py) | GCD via modulo-based Euclidean algorithm | O(log min(a, b)) | O(1) |
| [`lcm_2nums_brute_impl.py`](MATHS/5_GCD/lcm_2nums_brute_impl.py) | LCM by scanning multiples of the larger input | O(lcm(a, b) / max(a, b)) | O(1) |
| [`lcm_2nums_euclidean_impl.py`](MATHS/5_GCD/lcm_2nums_euclidean_impl.py) | LCM via lcm(a, b) = a·b / gcd(a, b) | O(log min(a, b)) | O(1) |
| [`extended_euclidean_impl.py`](MATHS/5_GCD/extended_euclidean_impl.py) | gcd plus Bézout coefficients (a·x + b·y = gcd) | O(log min(\|a\|, \|b\|)) | O(log min(\|a\|, \|b\|)) |
| [`diophantine_equation_impl.py`](MATHS/5_GCD/diophantine_equation_impl.py) | Particular integer solution to a·x + b·y = c | O(log min(\|a\|, \|b\|)) | O(log min(\|a\|, \|b\|)) |

### `6_Mathematical_Principles`

| File | Description | Time | Space |
|------|-------------|------|-------|
| [`numbers_till_n_divisible_by_3_and_5.py`](MATHS/6_Mathematical_Principles/numbers_till_n_divisible_by_3_and_5.py) | Count of 1..n divisible by 3 or 5 (inclusion–exclusion) | O(1) | O(1) |
| [`derangements.py`](MATHS/6_Mathematical_Principles/derangements.py) | Derangements via D(n) = (n − 1)(D(n − 1) + D(n − 2)) | O(n) | O(1) |
| [`find_start_end_idx_for_subarray_sum_divisible_by_size_of_arr.py`](MATHS/6_Mathematical_Principles/find_start_end_idx_for_subarray_sum_divisible_by_size_of_arr.py) | Subarray with sum divisible by array size (pigeonhole on prefix remainders) | O(n) | O(n) |

### `7_Euler_Totient_Function`

| File | Description | Time | Space |
|------|-------------|------|-------|
| [`euler_totient_brute.py`](MATHS/7_Euler_Totient_Function/euler_totient_brute.py) | φ(n) by counting integers coprime with n | O(n log n) | O(1) |
| [`euler_totient_sqrt(n).py`](MATHS/7_Euler_Totient_Function/euler_totient_sqrt%28n%29.py) | φ(n) via φ(n) = n·∏(1 − 1/p), factoring up to √n | O(√n) | O(1) |
| [`euler_totient_nlogn_impl.py`](MATHS/7_Euler_Totient_Function/euler_totient_nlogn_impl.py) | φ for all values ≤ n via the sieve identity n = Σ_{d\|n} φ(d) | O(n log n) | O(n) |

### `8_Modular_Arithmetic`

| File | Description | Time | Space |
|------|-------------|------|-------|
| [`Modular_inverse_with_extended_euclidean.py`](MATHS/8_Modular_Arithmetic/Modular_inverse_with_extended_euclidean.py) | Modular inverse via extended Euclidean (None if gcd ≠ 1) | O(log min(a, m)) | O(log min(a, m)) |
| [`Modular_Inverse_with_Euler_Theorem.py`](MATHS/8_Modular_Arithmetic/Modular_Inverse_with_Euler_Theorem.py) | Modular inverse via a⁻¹ ≡ a^(φ(m)−1) (√n totient + fast pow) | O(√m) | O(1) |
| [`Modular_Inverse_With_Fermat_Theorem.py`](MATHS/8_Modular_Arithmetic/Modular_Inverse_With_Fermat_Theorem.py) | Modular inverse mod prime p via a⁻¹ ≡ a^(p−2) | O(log p) | O(1) |
| [`Modular_Inverse_from_1_to_n.py`](MATHS/8_Modular_Arithmetic/Modular_Inverse_from_1_to_n.py) | Inverses of 1..n mod a prime via linear recurrence | O(n) | O(n) |
| [`Chinese_Remainder_Theorem.py`](MATHS/8_Modular_Arithmetic/Chinese_Remainder_Theorem.py) | Solve x ≡ a[i] (mod n[i]) for pairwise-coprime moduli | O(k log N) | O(log max nᵢ) |

### `9_Modular_Exponentiation`

| File | Description | Time | Space |
|------|-------------|------|-------|
| [`recursive_pow.py`](MATHS/9_Modular_Exponentiation/recursive_pow.py) | (base^exp) mod m via recursive binary exponentiation | O(log exp) | O(log exp) |
| [`iterative_bitwise_pow.py`](MATHS/9_Modular_Exponentiation/iterative_bitwise_pow.py) | (x^n) mod m via iterative bitwise exponentiation | O(log n) | O(1) |
| [`brute_force_matrix_exponentiation.py`](MATHS/9_Modular_Exponentiation/brute_force_matrix_exponentiation.py) | Mⁿ by repeated multiplication from the identity | O(n·N³) | O(N²) |
| [`Matrix_Exponentiation_size3logN_impl.py`](MATHS/9_Modular_Exponentiation/Matrix_Exponentiation_size3logN_impl.py) | Mⁿ via fast binary matrix exponentiation | O(N³ log N) | O(N²) |

### `10_Geometric_Algorithms`

| File | Description | Time | Space |
|------|-------------|------|-------|
| [`orientation_of_3_points.py`](MATHS/10_Geometric_Algorithms/orientation_of_3_points.py) | Orientation of a point triple via cross product (CCW / CW / collinear) | O(1) | O(1) |
| [`line_segment_intersection.py`](MATHS/10_Geometric_Algorithms/line_segment_intersection.py) | Segment intersection via four-orientation test + on-segment checks | O(1) | O(1) |
| [`convex_hull_brute_force.py`](MATHS/10_Geometric_Algorithms/convex_hull_brute_force.py) | Convex hull by keeping edges with all points on one side | O(N³) | O(N²) |
| [`convex_hull_Jarvis_March.py`](MATHS/10_Geometric_Algorithms/convex_hull_Jarvis_March.py) | Convex hull via Jarvis march (gift wrapping) | O(N·H) | O(H) |
| [`convex_hull_Graham_Scan.py`](MATHS/10_Geometric_Algorithms/convex_hull_Graham_Scan.py) | Convex hull via Graham scan (polar-angle sort + stack sweep) | O(N log N) | O(N) |

## Assumptions & Caveats

Some implementations assume specific input conditions:

- **Fermat-based inverse** assumes `p` is prime and `a` is not a multiple of `p`.
- **1-to-n inverses** and the **linear-recurrence** approach assume a prime modulus with `n < mod`.
- **Chinese Remainder Theorem** assumes the moduli are pairwise coprime.
- **Modular / matrix exponentiation** assume a non-negative exponent (and a square matrix for the matrix variants).
- **Convex hull** routines assume the points are not all collinear; the brute-force variant additionally assumes no three hull vertices are collinear.

## Running the Code

Each file is standalone and can be run directly:

```bash
python MATHS/2_Divisors/sqrtN_impl.py
python MATHS/9_Modular_Exponentiation/iterative_bitwise_pow.py
python MATHS/10_Geometric_Algorithms/convex_hull_Graham_Scan.py
```

Files that expose reusable functions include a small `if __name__ == "__main__":` demo block so you can see example output immediately.

## Contributing / Extending

When adding a new implementation:

1. Place it in the matching numbered topic folder (or create a new one).
2. Add a module-level docstring stating what it does and its time/space complexity.
3. Include a short `__main__` demo with a couple of sample inputs.
4. Add a row for it in the relevant table above so this README stays accurate.
