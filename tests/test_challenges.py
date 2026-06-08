"""Pytest tests for Week 7: Moonlight Festival Control Booth."""

from src.challenges import (
    order_festival_alerts,
    order_festival_alerts_stable,
    peek_next_festival_alert,
    top_k_festival_alerts,
)


# -----------------------------
# order_festival_alerts
# -----------------------------

def test_order_festival_alerts_normal_case() -> None:
    alerts = [
        (2, "Food court power issue"),
        (1, "Main Stage microphone failed"),
        (3, "Lost umbrella report"),
    ]
    assert order_festival_alerts(alerts) == [
        "Main Stage microphone failed",
        "Food court power issue",
        "Lost umbrella report",
    ]


def test_order_festival_alerts_empty_input() -> None:
    assert order_festival_alerts([]) == []


def test_order_festival_alerts_one_alert() -> None:
    alerts = [(1, "Storm warning")]
    assert order_festival_alerts(alerts) == ["Storm warning"]


def test_order_festival_alerts_handles_duplicate_priorities() -> None:
    alerts = [
        (2, "Lighting check"),
        (2, "Backstage cleanup"),
        (1, "Security call"),
    ]
    result = order_festival_alerts(alerts)
    assert result[0] == "Security call"
    assert set(result[1:]) == {"Lighting check", "Backstage cleanup"}


# -----------------------------
# order_festival_alerts_stable
# -----------------------------

def test_order_festival_alerts_stable_normal_case() -> None:
    alerts = [
        (2, "Food truck restock"),
        (1, "North Gate security call"),
        (3, "Lost hat report"),
    ]
    assert order_festival_alerts_stable(alerts) == [
        "North Gate security call",
        "Food truck restock",
        "Lost hat report",
    ]


def test_order_festival_alerts_stable_keeps_input_order_for_ties() -> None:
    alerts = [
        (1, "Security check at North Gate"),
        (1, "Lighting issue at East Stage"),
        (2, "Performer arrived backstage"),
    ]
    assert order_festival_alerts_stable(alerts) == [
        "Security check at North Gate",
        "Lighting issue at East Stage",
        "Performer arrived backstage",
    ]


def test_order_festival_alerts_stable_all_same_priority() -> None:
    alerts = [
        (2, "Check generator"),
        (2, "Refill water station"),
        (2, "Move spare chairs"),
    ]
    assert order_festival_alerts_stable(alerts) == [
        "Check generator",
        "Refill water station",
        "Move spare chairs",
    ]


def test_order_festival_alerts_stable_empty_input() -> None:
    assert order_festival_alerts_stable([]) == []


# -----------------------------
# top_k_festival_alerts
# -----------------------------

def test_top_k_festival_alerts_normal_case() -> None:
    alerts = [
        (3, "Merch tent low stock"),
        (1, "Storm warning"),
        (2, "Ticket scanner issue"),
        (1, "Stage power failure"),
    ]
    assert top_k_festival_alerts(alerts, 3) == [
        "Storm warning",
        "Stage power failure",
        "Ticket scanner issue",
    ]


def test_top_k_festival_alerts_k_zero() -> None:
    alerts = [
        (1, "Stage power failure"),
        (2, "Ticket scanner issue"),
    ]
    assert top_k_festival_alerts(alerts, 0) == []


def test_top_k_festival_alerts_k_larger_than_input() -> None:
    alerts = [
        (2, "Food court power issue"),
        (1, "Main Stage microphone failed"),
    ]
    assert top_k_festival_alerts(alerts, 5) == [
        "Main Stage microphone failed",
        "Food court power issue",
    ]


def test_top_k_festival_alerts_empty_input() -> None:
    assert top_k_festival_alerts([], 3) == []


def test_top_k_festival_alerts_duplicate_priorities() -> None:
    alerts = [
        (1, "Storm warning"),
        (1, "Stage power failure"),
        (2, "Ticket scanner issue"),
        (2, "Backstage delay"),
    ]
    result = top_k_festival_alerts(alerts, 2)
    assert len(result) == 2
    assert set(result) == {"Storm warning", "Stage power failure"}


# -----------------------------
# peek_next_festival_alert
# -----------------------------

def test_peek_next_festival_alert_normal_case() -> None:
    alerts = [
        (2, "Food court power issue"),
        (1, "Main Stage microphone failed"),
        (3, "Lost umbrella report"),
    ]
    assert peek_next_festival_alert(alerts) == "Main Stage microphone failed"


def test_peek_next_festival_alert_empty_input() -> None:
    assert peek_next_festival_alert([]) is None


def test_peek_next_festival_alert_does_not_modify_original_input() -> None:
    alerts = [
        (2, "Lighting check"),
        (1, "Security call"),
        (3, "Lost scarf report"),
    ]
    original = alerts.copy()
    result = peek_next_festival_alert(alerts)
    assert result == "Security call"
    assert alerts == original