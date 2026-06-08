# Week 7 Homework: Moonlight Festival Control Booth

## Summary

This assignment builds a priority queue system for a festival control booth using Python's `heapq` module. Alerts arrive with different urgency levels and must be handled in priority order, not arrival order. Four functions are implemented: basic priority ordering, stable ordering that preserves input order for ties, top-k selection, and a non-destructive peek at the next alert.

---

## Approach

### `order_festival_alerts`

Each alert tuple `(priority, title)` is pushed directly into a min-heap. Since `heapq` always pops the smallest item first, and smaller priority numbers mean higher urgency, popping repeatedly gives alerts in the correct handling order. The result list is built by collecting titles as they come off the heap.

### `order_festival_alerts_stable`

The heap item is extended to `(priority, index, title)` where `index` is the position of the alert in the original input list. When two alerts share the same priority, the heap compares on `index` next, which guarantees the one that arrived earlier is popped first. This makes the sort stable without any extra sorting step.

### `top_k_festival_alerts`

All alerts are pushed into a min-heap. Then exactly `min(k, len(alerts))` items are popped. Each pop gives the next most urgent alert in order, so the result is already sorted from most to least urgent. Edge cases — `k <= 0` and empty input — return `[]` immediately.

### `peek_next_festival_alert`

The original list is copied with `list(alerts)` before calling `heapq.heapify`. This means the original input is never modified. After heapifying the copy, `heap[0]` holds the smallest item — the most urgent alert — so the title is read directly without any pop.

---

## Complexity

### `order_festival_alerts`

- **Time:** O(n log n) — each of the n pushes costs O(log n); each of the n pops also costs O(log n).
- **Space:** O(n) — the heap holds all n alerts at once.
- **Why a heap fits:** A heap processes each item in O(log n) rather than re-sorting the whole list each time a new alert arrives. For a live system receiving alerts one at a time, this is much better than O(n log n) per insertion with a sorted list.

### `order_festival_alerts_stable`

- **Time:** O(n log n) — same reasoning as above; the extra index field does not change the cost.
- **Space:** O(n) — the heap stores a 3-tuple per alert instead of a 2-tuple, but it is still O(n).
- **Why:** Storing the insertion index is a standard trick to break ties in a heap without changing the underlying data structure.

### `top_k_festival_alerts`

- **Time:** O(n log n) to build the heap + O(k log n) to pop k times → O(n log n) overall.
- **Space:** O(n) for the heap.
- **Why:** `heapq.nsmallest(k, alerts)` would also work and is O(n log k), but building the full heap and popping k times is equally correct and clear for this assignment size.

### `peek_next_festival_alert`

- **Time:** O(n) — `heapq.heapify` on a copy of n items takes O(n).
- **Space:** O(n) — the copy of the list.
- **Why:** Heapifying in-place on a copy is simpler than pushing all items one by one. Reading `heap[0]` after heapify is O(1).

---

## Edge-case checklist

### `order_festival_alerts`

- [x] Empty input → returns `[]`
- [x] One alert → returns list with that one title
- [x] Multiple different priorities → sorted correctly

### `order_festival_alerts_stable`

- [x] Same-priority tie → earlier input item comes first
- [x] All same priority → full original order preserved
- [x] Empty input → returns `[]`

### `top_k_festival_alerts`

- [x] `k = 0` → returns `[]`
- [x] `k > len(alerts)` → returns all alerts in priority order
- [x] Duplicate priorities → both included when within top k
- [x] Empty input → returns `[]`

### `peek_next_festival_alert`

- [x] Empty input → returns `None`
- [x] Normal case → returns most urgent title
- [x] Original list is unchanged after the call

---

## Test notes

- `test_order_festival_alerts_handles_duplicate_priorities` uses `set` on the tied items because heap order among equal priorities is not guaranteed in the non-stable version.
- `test_top_k_festival_alerts_duplicate_priorities` also uses `set` for the same reason.
- `test_peek_next_festival_alert_does_not_modify_original_input` saves a copy before calling the function and asserts equality afterward.

---

## Assistance & Sources

- **AI used?** Yes
- **What it helped with:** Structuring the stable sort with index tuples and reviewing edge-case coverage.
- **Other sources:** [Python docs — heapq](https://docs.python.org/3/library/heapq.html)

---

## Reflection

**What was hardest?**

Making `order_festival_alerts_stable` truly stable. Simply pushing `(priority, title)` does not guarantee tie order because Python compares strings when priorities match, and alphabetical order is not the same as input order. Adding the index as a tiebreaker fixed this cleanly.

**What do you understand better now?**

Why a heap is better than repeatedly sorting a list. Sorting costs O(n log n) every time the list changes. A heap keeps items in a partially-ordered tree so each insert and remove is only O(log n), which matters when alerts arrive continuously in a real system.