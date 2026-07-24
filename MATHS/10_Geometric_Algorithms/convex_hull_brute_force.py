from collections import defaultdict


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


def convexHull(points):
    """
    Compute the convex hull of a set of 2D points by brute force.

    An edge (i, j) belongs to the hull if and only if every other point lies
    strictly on one side of the line through points[i] and points[j] (all
    orientations share a sign). Each qualifying edge is recorded in an
    adjacency map, and the hull is then recovered by walking the edges from the
    lexicographically smallest point until returning to the start.

    Parameters:
    points (list[Point]): The input points.

    Returns:
    list[int]: Indices of the hull vertices in traversal order.

    Assumptions:
        No three hull vertices are collinear (each hull vertex has exactly two
        hull neighbors), and there are at least three non-collinear points.

    Time Complexity: O(N^3)
        Every pair of points (O(N^2)) is tested against all other points (O(N)).

    Space Complexity: O(N^2)
        The adjacency map may store up to O(N^2) edge entries in the worst case.
    """
    N = len(points)
    adj = defaultdict(list)

    for i in range(N):
        for j in range(i + 1, N):
            p1, p2 = points[i], points[j]
            # Re-initialize per candidate edge (this was the main bug).
            isValid = True
            side = 0
            for k in range(N):
                if k == i or k == j:
                    continue
                o = orientation(p1, p2, points[k])
                if o != 0:
                    if side == 0:
                        # Lock in the side of the first non-collinear point.
                        side = o
                    elif o != side:
                        # A point on the opposite side => edge is interior.
                        isValid = False
                        break
            if isValid:
                # Edge (i, j) is a hull edge; record both directions.
                adj[i].append(j)
                adj[j].append(i)

    # Start from the lexicographically smallest point (guaranteed on the hull).
    start = min(range(N), key=lambda idx: (points[idx].x, points[idx].y))

    hull = [start]
    prev = None
    curr = start
    while True:
        # Each hull vertex has exactly two neighbors; step to the one we did
        # not just come from.
        n1, n2 = adj[curr][0], adj[curr][1]
        nxt = n1 if n1 != prev else n2
        prev, curr = curr, nxt
        if curr == start:
            break
        hull.append(curr)

    return hull


if __name__ == "__main__":
    pts = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2), Point(1, 1)]
    print(convexHull(pts))  # indices of the 4 corners (interior point 4 excluded)