def matmul(A, B):
    """
    Multiply two matrices A and B.

    A is n x p and B is p x m; the result C is n x m, where
    C[i][j] = sum over k of A[i][k] * B[k][j].

    Parameters:
    A (list[list[int]]): Left matrix (n x p).
    B (list[list[int]]): Right matrix (p x m).

    Returns:
    list[list[int]]: The product matrix (n x m).

    Preconditions:
        A is non-empty and its column count equals B's row count.

    Time Complexity: O(n * m * p)
        Three nested loops over the result rows, result columns, and the
        shared inner dimension. For square N x N matrices this is O(N^3).

    Space Complexity: O(n * m)
        For the result matrix (O(N^2) in the square case).
    """
    n = len(A)
    m = len(B[0])
    p = len(B)

    # Initialize the result matrix with zeros (n x m).
    C = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(p):
                # Accumulate the dot product of A's row i and B's column j.
                C[i][j] += A[i][k] * B[k][j]

    return C


def matExp(M, n):
    """
    Raise a square matrix M to the power n by brute-force repeated
    multiplication.

    Starts from the identity matrix and multiplies by M exactly n times, so
    it returns M^n (and M^0 = I when n = 0).

    Parameters:
    M (list[list[int]]): A square matrix (N x N).
    n (int): The exponent (assumed non-negative).

    Returns:
    list[list[int]]: M raised to the power n.

    Time Complexity: O(n * N^3)
        Performs n matrix multiplications, each O(N^3). (Fast exponentiation
        would reduce the factor n to log n.)

    Space Complexity: O(N^2)
        Stores the running result matrix.
    """
    N = len(M)
    # Start with the N x N identity matrix (the multiplicative identity).
    res = [[0 for _ in range(N)] for i in range(N)]
    for i in range(N):
        res[i][i] = 1
    # Multiply by M a total of n times to obtain M^n.
    for i in range(1, n + 1):
        res = matmul(res, M)
    return res


if __name__ == "__main__":
    M = [[1, 1], [1, 0]]
    print(matExp(M, 5))  # [[8, 5], [5, 3]]
    print(matExp(M, 0))  # [[1, 0], [0, 1]]