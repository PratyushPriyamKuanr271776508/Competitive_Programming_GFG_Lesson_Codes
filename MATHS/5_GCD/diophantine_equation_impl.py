import importlib.util
from pathlib import Path


MODULE_DIR = Path(__file__).resolve().parent
GCD_MODULE_PATH = MODULE_DIR / "extended_euclidean_impl.py"

spec = importlib.util.spec_from_file_location("extended_euclidean_impl", GCD_MODULE_PATH)
gcd_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gcd_module)
extended_euclidean = gcd_module.extended_euclidean


def diophantine(a, b, c):
    """
    Solve the linear Diophantine equation a*x + b*y = c.

    Returns a particular solution in the form of a string: "x = ..., y = ...".
    If no integer solution exists, returns None.

    This uses the extended Euclidean algorithm to compute gcd(a, b) and
    Bézout coefficients x, y such that a*x + b*y = gcd(a, b). The equation has
    a solution iff c is divisible by gcd(a, b), and the particular solution is
    obtained by scaling the coefficients by c / gcd(a, b).

    Time Complexity: O(log(min(|a|, |b|))) because the extended Euclidean
    algorithm reduces the arguments using modulo operations.
    Space Complexity: O(log(min(|a|, |b|))) due to the recursion depth of the
    extended Euclidean algorithm.
    """
    g, x, y = extended_euclidean(a, b)
    if c % g != 0:
        return None

    factor = c // g
    return f"x = {x * factor} , y = {y * factor}"