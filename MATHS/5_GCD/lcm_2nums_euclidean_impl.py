import importlib.util
from pathlib import Path


MODULE_DIR = Path(__file__).resolve().parent
GCD_MODULE_PATH = MODULE_DIR / "gcd_2nums_optimized_euclidean_impl.py"

spec = importlib.util.spec_from_file_location("gcd_2nums_optimized_euclidean_impl", GCD_MODULE_PATH)
gcd_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gcd_module)
optimized_euclidean_gcd = gcd_module.optimized_euclidean_gcd


def find_lcm(a, b):
    """
    Return the least common multiple of two numbers using the Euclidean
    algorithm through the identity lcm(a, b) = (a * b) // gcd(a, b).

    This is a correct and efficient approach because it computes the gcd first
    and then derives the lcm from it.

    Time Complexity: O(log(min(a, b))) for the gcd computation, plus O(1) for
    the final arithmetic, so the overall complexity is O(log(min(a, b))).
    Space Complexity: O(1), because it uses only a constant amount of extra
    space.
    """
    if a == 0 or b == 0:
        return 0

    return (a * b) // optimized_euclidean_gcd(a, b)