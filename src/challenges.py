"""
Week 7: Moonlight Festival Control Booth

Use Python's heapq module to solve priority queue problems.
"""

from __future__ import annotations

import heapq


def order_festival_alerts(alerts: list[tuple[int, str]]) -> list[str]:
    """
    Return alert titles in the order they should be handled.

    Each alert is a tuple (priority, title).
    Smaller priority numbers are handled first.
    Uses heapq to pop items in priority order.
    """
    heap: list[tuple[int, str]] = []
    for priority, title in alerts:
        heapq.heappush(heap, (priority, title))

    result: list[str] = []
    while heap:
        _, title = heapq.heappop(heap)
        result.append(title)
    return result


def order_festival_alerts_stable(alerts: list[tuple[int, str]]) -> list[str]:
    """
    Return alert titles in priority order.

    If two alerts share the same priority, the one that appeared
    earlier in the input list is handled first (stable sort).
    Stores (priority, index, title) so index breaks ties.
    """
    heap: list[tuple[int, int, str]] = []
    for i, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, i, title))

    result: list[str] = []
    while heap:
        _, _, title = heapq.heappop(heap)
        result.append(title)
    return result


def top_k_festival_alerts(alerts: list[tuple[int, str]], k: int) -> list[str]:
    """
    Return the titles of the k most urgent alerts, most urgent first.

    If k <= 0, return [].
    If k > len(alerts), return all alerts in priority order.
    """
    if k <= 0:
        return []

    heap: list[tuple[int, int, str]] = []
    for i, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, i, title))

    result: list[str] = []
    for _ in range(min(k, len(heap))):
        _, _, title = heapq.heappop(heap)
        result.append(title)
    return result


def peek_next_festival_alert(alerts: list[tuple[int, str]]) -> str | None:
    """
    Return the title of the next alert to handle without modifying the input.

    Returns None if alerts is empty.
    Copies the list before heapifying so the original is never changed.
    """
    if not alerts:
        return None

    heap = list(alerts)
    heapq.heapify(heap)
    _, title = heap[0]
    return title