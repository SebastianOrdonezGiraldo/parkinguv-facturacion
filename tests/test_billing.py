from parkinguv.billing import calculate_fee


def test_first_30_minutes_are_free():
    assert calculate_fee(30, vip=False) == 0


def test_minute_31_charges_one_hour_fraction():
    assert calculate_fee(31, vip=False) == 500


def test_charges_each_started_hour_after_grace_period():
    assert calculate_fee(90, vip=False) == 500
    assert calculate_fee(91, vip=False) == 1000
