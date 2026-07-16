def matrix_multiplication(A, B):
    """
    Multiply two matrices A and B.

    A is r x x and B is x x c; the result is r x c, where
    res[i][j] = sum over k of A[i][k] * B[k][j].

    Parameters:
    A (list[list[int]]): Left matrix (r x x).
    B (list[list[int]]): Right matrix (x x c).

    Returns:
    list[list[int]]: The product matrix (r x c).

    Preconditions:
        A's column count equals B's row count, and both are non-empty.

    Time Complexity: O(r * c * x)
        Three nested loops over result rows, result columns, and the shared
        inner dimension. For square N x N matrices this is O(N^3).

    Space Complexity: O(r * c)
        For the result matrix (O(N^2) in the square case).
    """
    r, x, c = len(A), len(B), len(B[0])
    res = [[0 for i in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for k in range(x):
                # Accumulate the dot product of A's row i and B's column j.
                res[i][j] += A[i][k] * B[k][j]
    return res


def mat_exp(M, N):
    """
    Raise a square matrix M to the power N using fast (binary) exponentiation.

    Scans the bits of N: whenever a bit is set, the current power of M
    (M^(2^k)) is multiplied into the result; M is squared each step. This
    performs O(log N) matrix multiplications instead of N.

    Parameters:
    M (list[list[int]]): A square matrix (n x n).
    N (int): The exponent (assumed non-negative).

    Returns:
    list[list[int]]: M raised to the power N (M^0 = identity when N = 0).

    Time Complexity: O(N^3 * log N)
        About log2(N) matrix multiplications, each O(n^3) for an n x n matrix.

    Space Complexity: O(n^2)
        Stores the running result and squared-base matrices.
    """
    n = len(M)
    # Start with the n x n identity matrix.
    res = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        res[i][i] = 1
    while N > 0:
        # If the current lowest bit is set, fold in the current power of M.
        if N & 1:
            res = matrix_multiplication(res, M)
        # Square the base for the next-higher bit and shift the exponent.
        M = matrix_multiplication(M, M)
        N >>= 1
    return res


if __name__ == "__main__":
    M = [[1, 1], [1, 0]]
    print(mat_exp(M, 5))  # [[8, 5], [5, 3]]
    print(mat_exp(M, 0))  # [[1, 0], [0, 1]]