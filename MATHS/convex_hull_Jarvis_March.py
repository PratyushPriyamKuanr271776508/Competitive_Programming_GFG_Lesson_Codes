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


def convex_hull(points):
    """
    Compute the convex hull of a set of 2D points using Jarvis march
    (gift wrapping).

    Starting from the leftmost point, repeatedly pick the point that is the
    most clockwise relative to the current hull edge; wrapping around all
    points yields the hull. On collinear candidates the farthest point is
    kept so intermediate collinear points are skipped.

    Parameters:
    points (list[Point]): The input points.

    Returns:
    list[int]: Indices of the hull vertices in counterclockwise order.

    Assumptions:
        At least three points, not all collinear.

    Time Complexity: O(N * H)
        For each of the H hull vertices, all N points are scanned. Worst case
        H = N gives O(N^2).

    Space Complexity: O(H)
        For the output hull (O(N) in the worst case), beyond the input.
    """
    N = len(points)
    # Leftmost (then lowest) point is guaranteed to be on the hull.
    start = min(range(N), key=lambda i: (points[i].x, points[i].y))

    hull = []
    curr = start
    while True:
        hull.append(curr)

        # Seed the candidate with any index other than curr.
        candidate = (curr + 1) % N
        for i in range(N):
            if i == curr:
                continue
            o = orientation(points[curr], points[candidate], points[i])
            # Pick i if it is more clockwise than the current candidate, or,
            # if collinear, if it is farther from curr (skip inner points).
            if o < 0 or (o == 0 and dist(points[curr], points[i]) > dist(points[curr], points[candidate])):
                candidate = i

        curr = candidate
        # Back to the start => the wrap is complete.
        if curr == start:
            break

    return hull


if __name__ == "__main__":
    pts = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2), Point(1, 1)]
    print(convex_hull(pts))  # indices of the 4 corners (interior point excluded)
