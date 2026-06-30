# Exclusion and Inclusion principle

def nums_divisible_by_3_or_5(n):
    """
    Return the count of numbers from 1 to n that are divisible by 3 or 5.

    This uses the inclusion-exclusion principle:
    count(3 or 5) = count(3) + count(5) - count(3 and 5).

    Time Complexity: O(1), because it performs a constant number of arithmetic
    operations.
    Space Complexity: O(1), because it uses only a constant amount of extra
    space.
    """
    db_3 = n // 3
    db_5 = n // 5
    db_3_5 = n // 15
    return db_3 + db_5 - db_3_5
