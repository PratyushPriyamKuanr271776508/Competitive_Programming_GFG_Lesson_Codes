def derangements(n):
    """
    Return the number of derangements of n objects.

    A derangement is a permutation where no object appears in its original
    position. The recurrence is:
    D(n) = (n - 1) * (D(n - 1) + D(n - 2))
    with base cases D(0) = 1 and D(1) = 0.

    Time Complexity: O(n), because the loop iterates once for each value from 2
    to n.
    Space Complexity: O(1), because it uses only a constant number of scalar
    variables.
    """
    if n == 0:
        return 1
    if n == 1:
        return 0

    prev2 = 1
    prev1 = 0
    for i in range(2, n + 1):
        current = (i - 1) * (prev1 + prev2)
        prev2, prev1 = prev1, current

    return prev1