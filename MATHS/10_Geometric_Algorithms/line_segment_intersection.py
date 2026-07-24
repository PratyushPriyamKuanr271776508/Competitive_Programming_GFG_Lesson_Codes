class Point:
    """A 2D point with x and y coordinates."""
    def __init__(self, x, y):
        self.x = x
        self.y = y


def orientation(p1, p2, p3):
    """
    Orientation of the ordered triple (p1, p2, p3) via the cross product of
    p1->p2 and p1->p3.

    Returns:
        0  -> collinear
        1  -> counterclockwise (left turn)
       -1  -> clockwise (right turn)

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    o = (p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y)
    if o == 0:
        return 0
    return 1 if o > 0 else -1


def onSegment(p1, p2, p3):
    """
    Assuming p1, p2, p3 are collinear, check whether p3 lies within the
    axis-aligned bounding box of segment p1-p2 (i.e., on the segment).

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    maxX, minX = max(p1.x, p2.x), min(p1.x, p2.x)
    maxY, minY = max(p1.y, p2.y), min(p1.y, p2.y)
    return minX <= p3.x <= maxX and minY <= p3.y <= maxY


def doIntersect(p1, p2, p3, p4):
    """
    Determine whether segment p1-p2 intersects segment p3-p4.

    Uses the four-orientation test. Two segments properly cross when the two
    endpoints of each segment fall on opposite sides of the other. Collinear
    touching/overlap is handled by the special (orientation == 0) cases, each
    checked independently with onSegment.

    Time Complexity: O(1)
        A fixed number of orientation and bounding-box checks.

    Space Complexity: O(1)
        Only a few scalar variables are used.
    """
    o123 = orientation(p1, p2, p3)
    o124 = orientation(p1, p2, p4)
    o341 = orientation(p3, p4, p1)
    o342 = orientation(p3, p4, p2)

    # General case: the segments straddle each other.
    if o123 != o124 and o341 != o342:
        return True

    # Special collinear cases: an endpoint of one segment lies on the other.
    if o123 == 0 and onSegment(p1, p2, p3):
        return True
    if o124 == 0 and onSegment(p1, p2, p4):
        return True
    if o341 == 0 and onSegment(p3, p4, p1):
        return True
    if o342 == 0 and onSegment(p3, p4, p2):
        return True

    return False


if __name__ == "__main__":
    A, B = Point(0, 0), Point(4, 4)
    C, D = Point(0, 4), Point(4, 0)
    print(doIntersect(A, B, C, D))                       # True  (cross)
    print(doIntersect(A, B, Point(5, 5), Point(6, 6)))   # False (disjoint, collinear)
    print(doIntersect(A, B, Point(2, 2), Point(6, 6)))   # True  (collinear overlap)