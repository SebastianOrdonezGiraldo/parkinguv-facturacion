from math import ceil

FREE_MINUTES = 30
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = 24 * MINUTES_PER_HOUR
HOURLY_RATE = 500
DAILY_CAP = 12000
VIP_DISCOUNT = 0.20


def _charge_day(minutes: int, has_initial_grace: bool) -> int:
    free_minutes = FREE_MINUTES if has_initial_grace else 0
    if minutes <= free_minutes:
        return 0
    billable_hours = ceil((minutes - free_minutes) / MINUTES_PER_HOUR)
    return min(billable_hours * HOURLY_RATE, DAILY_CAP)


def calculate_fee(minutes: int, vip: bool = False) -> int:
    if minutes < 0:
        raise ValueError("minutes must be greater than or equal to zero")

    full_days, remaining_minutes = divmod(minutes, MINUTES_PER_DAY)
    total = 0

    if full_days:
        total += _charge_day(MINUTES_PER_DAY, has_initial_grace=True)
        total += (full_days - 1) * DAILY_CAP
        total += _charge_day(remaining_minutes, has_initial_grace=False)
        return _apply_vip_discount(total, vip)

    return _apply_vip_discount(_charge_day(remaining_minutes, has_initial_grace=True), vip)


def _apply_vip_discount(total: int, vip: bool) -> int:
    if not vip:
        return total
    return int(total * (1 - VIP_DISCOUNT))
