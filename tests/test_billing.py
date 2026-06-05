from parkinguv.billing import calculate_fee


def test_first_30_minutes_are_free():
    assert calculate_fee(30, vip=False) == 0


def test_minute_31_charges_one_hour_fraction():
    assert calculate_fee(31, vip=False) == 500


def test_charges_each_started_hour_after_grace_period():
    assert calculate_fee(90, vip=False) == 500
    assert calculate_fee(91, vip=False) == 1000


def test_applies_daily_cap_for_24_hours():
    assert calculate_fee(24 * 60, vip=False) == 12000


def test_applies_daily_cap_per_started_day():
    assert calculate_fee((24 * 60) + 31, vip=False) == 12500


def test_vip_discount_is_applied_before_daily_cap():
    assert calculate_fee(24 * 60, vip=True) == 9600


def test_vip_discount_applies_to_short_stays():
    assert calculate_fee(91, vip=True) == 800
