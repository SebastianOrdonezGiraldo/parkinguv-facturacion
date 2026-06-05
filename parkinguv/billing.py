def calculate_fee(minutes: int, vip: bool = False) -> int:
    if minutes <= 30:
        return 0
    return 500
