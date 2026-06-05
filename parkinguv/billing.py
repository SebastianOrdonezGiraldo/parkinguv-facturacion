from math import ceil


def calculate_fee(minutes: int, vip: bool = False) -> int:
    if minutes <= 30:
        return 0
    billable_hours = ceil((minutes - 30) / 60)
    return billable_hours * 500
