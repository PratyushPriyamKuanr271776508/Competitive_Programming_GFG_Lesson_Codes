import heapq
from sortedcontainers import SortedList


class Point:
    """A 2D point with floating-point coordinates."""
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Segment:
    """
    A line segment with a stable id. Endpoints are normalized so p1 precedes
    p2 left-to-right (bottom-to-top for vertical segments).
    """
    def __init__(self, id_tag, p1, p2):
        if abs(p1.x - p2.x) < 1e-9:
            self.is_vertical = True
            # Vertical: order endpoints bottom-to-top.
            self.p1, self.p2 = (p1, p2) if p1.y <= p2.y else (p2, p1)
        else:
            self.is_vertical = False
            # Non-vertical: order endpoints left-to-right.
            self.p1, self.p2 = (p1, p2) if p1.x <= p2.x else (p2, p1)
        self.id = id_tag

    def y_at_x(self, x):
        """y-coordinate of the segment at a given sweep x (p1.y if vertical)."""
        if self.is_vertical:
            return self.p1.y
        return self.p1.y + (x - self.p1.x) * (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

    def on_segment(self, p):
        """Whether p lies within this segment's bounding box (with tolerance)."""
        return (min(self.p1.x, self.p2.x) - 1e-9 <= p.x <= max(self.p1.x, self.p2.x) + 1e-9 and
                min(self.p1.y, self.p2.y) - 1e-9 <= p.y <= max(self.p1.y, self.p2.y) + 1e-9)

    def intersects_with(self, other):
        """
        Standard four-orientation segment-intersection test with collinear
        on-segment fallbacks. O(1).
        """
        def orientation(p, q, r):
            val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
            if abs(val) < 1e-9:
                return 0
            return 1 if val > 0 else 2

        p1, q1 = self.p1, self.p2
        p2, q2 = other.p1, other.p2

        o1, o2 = orientation(p1, q1, p2), orientation(p1, q1, q2)
        o3, o4 = orientation(p2, q2, p1), orientation(p2, q2, q1)

        if o1 != o2 and o3 != o4:
            return True
        if o1 == 0 and self.on_segment(p2):
            return True
        if o2 == 0 and self.on_segment(q2):
            return True
        if o3 == 0 and other.on_segment(p1):
            return True
        if o4 == 0 and other.on_segment(q1):
            return True
        return False

    def __repr__(self):
        return f"Seg{self.id}"


class SweepState:
    """Holds the current sweep-line x, read by SweepKey during comparisons."""
    x = float('-inf')


class SweepKey:
    """
    Ordering key for the active-segment structure: segments are ordered by
    their y-coordinate at the current sweep x, with the id as a tie-break.

    NOTE: this key is *not stable* — it changes as SweepState.x advances. The
    active structure is only reliable as long as the relative vertical order of
    active segments does not change between updates (i.e. no crossings strictly
    inside the active set are skipped). Detecting the first intersection and
    stopping, as done here, keeps this within tolerance for well-separated
    inputs but is not a fully general Bentley–Ottmann implementation.
    """
    def __init__(self, segment):
        self.segment = segment

    def __lt__(self, other):
        x = SweepState.x
        y1 = self.segment.y_at_x(x)
        y2 = other.segment.y_at_x(x)
        if abs(y1 - y2) > 1e-9:
            return y1 < y2
        return self.segment.id < other.segment.id


def has_any_intersection(segments):
    """
    Detect whether ANY two of the given segments intersect, using a sweep line.

    Events are processed left-to-right: a segment start inserts it into the
    active set and checks it against its immediate vertical neighbors; a
    segment end removes it and checks the two neighbors that become adjacent;
    a vertical segment is handled as a single "flash" that scans the active
    segments crossing its vertical span.

    Parameters:
    segments (list[Segment]): The input segments.

    Returns:
    bool: True if at least one intersecting pair exists, else False.

    Assumptions / limitations:
        Robust for inputs where active segments keep a stable vertical order
        between events. Dense crossings, many coincident endpoints, or overlaps
        exactly at a vertical's x may not be handled fully generally (see
        SweepKey note). Neighbor lookups below are guarded so ordering drift
        degrades gracefully instead of raising.

    Time Complexity: O((n + k) log n) typical
        n start/end events plus per-event log-n tree work; vertical flashes add
        a scan over the crossing active segments. Worst case degrades toward
        O(n^2) if many segments span a vertical's range.

    Space Complexity: O(n)
        For the event queue and the active-segment structure.
    """
    event_queue = []
    active_segments = SortedList(key=SweepKey)
    active_map = {}

    def neighbors(wrapper):
        """Return (below, above) segments of a wrapper, or (None, None) on drift."""
        try:
            idx = active_segments.index(wrapper)
        except ValueError:
            return None, None
        above = active_segments[idx + 1].segment if idx + 1 < len(active_segments) else None
        below = active_segments[idx - 1].segment if idx - 1 >= 0 else None
        return below, above

    # 1. Build events: (x, type, seg) with type 0 = start, 1 = end, 2 = vertical.
    #    Start (0) sorts before end (1) at equal x, which is the desired order.
    for seg in segments:
        if seg.is_vertical:
            heapq.heappush(event_queue, (seg.p1.x, 2, seg))
        else:
            heapq.heappush(event_queue, (seg.p1.x, 0, seg))
            heapq.heappush(event_queue, (seg.p2.x, 1, seg))

    # 2. Sweep.
    while event_queue:
        x, typ, seg = heapq.heappop(event_queue)
        SweepState.x = x

        if typ == 0:  # START (non-vertical)
            wrapper = SweepKey(seg)
            active_map[seg.id] = wrapper
            active_segments.add(wrapper)

            below, above = neighbors(wrapper)
            if above and seg.intersects_with(above):
                return True
            if below and seg.intersects_with(below):
                return True

        elif typ == 1:  # END (non-vertical)
            wrapper = active_map.get(seg.id)
            if wrapper is not None:
                below, above = neighbors(wrapper)
                try:
                    active_segments.remove(wrapper)
                except ValueError:
                    pass
                active_map.pop(seg.id, None)
                # The two segments that become adjacent may now cross.
                if below and above and below.intersects_with(above):
                    return True

        elif typ == 2:  # VERTICAL "flash"
            # Locate where the vertical's bottom point sits among active segments.
            dummy_wrap = SweepKey(Segment("DUMMY", seg.p1, seg.p1))
            start_idx = active_segments.bisect_left(dummy_wrap)

            # Scan upward while active segments stay within the vertical's span.
            for i in range(start_idx, len(active_segments)):
                active_seg = active_segments[i].segment
                if active_seg.y_at_x(x) > seg.p2.y + 1e-9:
                    break
                if seg.intersects_with(active_seg):
                    return True

            # Defensive check of the segment just below the insertion slot.
            if start_idx > 0 and seg.intersects_with(active_segments[start_idx - 1].segment):
                return True

    return False


# ---------- Verification ----------
if __name__ == "__main__":
    test_lines = [
        Segment("Horizontal", Point(1.0, 3.0), Point(5.0, 3.0)),
        Segment("Vertical", Point(3.0, 1.0), Point(3.0, 5.0)),  # perpendicular cross
    ]
    print(f"Intersection Found? {has_any_intersection(test_lines)}")  # True
