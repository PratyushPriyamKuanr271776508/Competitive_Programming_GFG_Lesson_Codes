class Point:
    """A 2D point with x and y coordinates."""
    def __init__(self, x, y):
        self.x = x
        self.y = y


def cross_product(P1, P2, P3):
    """
    Compute the orientation of the ordered triple (P1, P2, P3).

    Returns the z-component of the cross product of the vectors P1->P2 and
    P1->P3:
        > 0  -> counterclockwise turn (P3 is left of line P1->P2)
        < 0  -> clockwise turn (P3 is right of line P1->P2)
        = 0  -> the three points are collinear
    The magnitude equals twice the signed area of triangle P1 P2 P3.

    Parameters:
    P1, P2, P3 (Point): The three points, in order.

    Returns:
    int | float: The signed cross-product value (its sign gives orientation).

    Time Complexity: O(1)
        A fixed number of arithmetic operations.

    Space Complexity: O(1)
        No extra storage is used.
    """
    # (P2 - P1) x (P3 - P1), taking the z-component of the 2D cross product.
    return (P2.x - P1.x) * (P3.y - P1.y) - (P3.x - P1.x) * (P2.y - P1.y)


if __name__ == "__main__":
    a, b, c = Point(0, 0), Point(1, 0), Point(0, 1)
    print(cross_product(a, b, c))            # 1  (counterclockwise)
    print(cross_product(a, b, Point(2, 0)))  # 0  (collinear)
    print(cross_product(a, b, Point(1, -1))) # -1 (clockwise)