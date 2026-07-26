from math import dist as _euclidean, inf


class Point:
    """A 2D point with x and y coordinates."""
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(a, b):
    """Euclidean distance between two Points."""
    return _euclidean((a.x, a.y), (b.x, b.y))


def _closest_recursive(pts_x):
    """
    Recursive core of the divide-and-conquer closest-pair algorithm.

    Parameters:
    pts_x (list[Point]): Points sorted by x (then y).

    Returns:
    tuple[float, tuple[Point, Point] | None, list[Point]]:
        (best distance, best pair, the same points sorted by y).
    Returning the y-sorted order lets the caller build the strip in linear
    time, which keeps the overall algorithm at O(N log N).
    """
    n = len(pts_x)

    # Base case: brute force for small groups; return points sorted by y.
    if n <= 3:
        best, pair = inf, None
        for i in range(n):
            for j in range(i + 1, n):
                d = dist(pts_x[i], pts_x[j])
                if d < best:
                    best, pair = d, (pts_x[i], pts_x[j])
        return best, pair, sorted(pts_x, key=lambda p: p.y)

    # Divide at the vertical line x = mid_x.
    mid = n // 2
    mid_x = pts_x[mid].x
    left_best, left_pair, left_y = _closest_recursive(pts_x[:mid])
    right_best, right_pair, right_y = _closest_recursive(pts_x[mid:])

    # Best of the two halves.
    if left_best <= right_best:
        best, pair = left_best, left_pair
    else:
        best, pair = right_best, right_pair

    # Merge the two y-sorted halves into one y-sorted list (linear time).
    pts_y = []
    i = j = 0
    while i < len(left_y) and j < len(right_y):
        if left_y[i].y <= right_y[j].y:
            pts_y.append(left_y[i]); i += 1
        else:
            pts_y.append(right_y[j]); j += 1
    pts_y.extend(left_y[i:])
    pts_y.extend(right_y[j:])

    # Strip: points within `best` of the dividing line, kept in y order.
    strip = [p for p in pts_y if abs(p.x - mid_x) < best]

    # For each strip point, only the next few (in y) can be closer than `best`;
    # the geometry guarantees at most a constant number of such comparisons.
    for a in range(len(strip)):
        b = a + 1
        while b < len(strip) and (strip[b].y - strip[a].y) < best:
            d = dist(strip[a], strip[b])
            if d < best:
                best, pair = d, (strip[a], strip[b])
            b += 1

    return best, pair, pts_y


def closest_pair(points):
    """
    Find the closest pair of points among a set of 2D points using
    divide and conquer.

    The points are sorted once by x; the plane is split recursively, the best
    distance from each half is taken, and a strip around the dividing line is
    checked to catch pairs split across the boundary.

    Parameters:
    points (list[Point]): The input points (at least two).

    Returns:
    tuple[float, tuple[Point, Point]] | None:
        (minimum distance, the closest pair), or None if fewer than 2 points.

    Time Complexity: O(N log N)
        One initial O(N log N) sort; the recurrence T(N) = 2·T(N/2) + O(N)
        (linear-time merge and strip scan) also resolves to O(N log N).

    Space Complexity: O(N)
        For the recursion's sorted sublists and the strip.
    """
    if len(points) < 2:
        return None
    pts_x = sorted(points, key=lambda p: (p.x, p.y))
    best, pair, _ = _closest_recursive(pts_x)
    return best, pair


if __name__ == "__main__":
    pts = [Point(2, 3), Point(12, 30), Point(40, 50),
           Point(5, 1), Point(12, 10), Point(3, 4)]
    d, (a, b) = closest_pair(pts)
    print(f"closest distance = {d:.4f} between ({a.x}, {a.y}) and ({b.x}, {b.y})")
    # closest distance = 1.4142 between (2, 3) and (3, 4)
