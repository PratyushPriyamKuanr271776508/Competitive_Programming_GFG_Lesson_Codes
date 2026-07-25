from math import dist as _euclidean


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


def dist(a, b):
    """Euclidean distance between two Points (used for collinear tie-breaks)."""
    return _euclidean((a.x, a.y), (b.x, b.y))


class PolarPoint:
    """
    Wraps a Point for polar-angle sorting about a pivot. Points are ordered
    counterclockwise by the angle of pivot->point; ties (collinear with the
    pivot) are broken by increasing distance from the pivot.
    """
    def __init__(self, point, pivot):
        self.point = point
        self.pivot = pivot

    def __lt__(self, other):
        o = orientation(self.pivot, self.point, other.point)
        if o > 0:
            return True
        if o == 0 and dist(self.pivot, self.point) < dist(self.pivot, other.point):
            return True
        return False


def convex_hull(points):
    """
    Compute the convex hull of a set of 2D points using the Graham scan.

    The lowest point (ties broken by x) is chosen as the pivot; the remaining
    points are sorted counterclockwise by polar angle about it. A stack is then
    swept through the sorted points, popping any that would create a
    non-left (clockwise or collinear) turn, leaving only hull vertices.

    Parameters:
    points (list[Point]): The input points.

    Returns:
    list[Point]: Hull vertices in counterclockwise order.

    Assumptions:
        At least three points, not all collinear.

    Time Complexity: O(N log N)
        Dominated by the polar-angle sort; the scan itself is O(N) since each
        point is pushed and popped at most once.

    Space Complexity: O(N)
        For the sorted list and the hull stack.
    """
    N = len(points)
    if N < 3:
        return points[:]

    # Pick the lowest (then leftmost) point as the pivot and move it to front.
    pivot_idx = min(range(N), key=lambda i: (points[i].y, points[i].x))
    points[0], points[pivot_idx] = points[pivot_idx], points[0]
    pivot = points[0]

    # Sort the rest by polar angle about the pivot, then unwrap to Points.
    ordered = [pp.point for pp in sorted(PolarPoint(points[i], pivot) for i in range(1, N))]

    # Graham scan.
    hull = [pivot]
    for p in ordered:
        # Pop while the last turn is not a left turn (clockwise or collinear).
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    return hull


if __name__ == "__main__":
    pts = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2), Point(1, 1)]
    print([(p.x, p.y) for p in convex_hull(pts)])  # the 4 corners, CCW
