from parkinguv.billing import calculate_fee


def test_first_30_minutes_are_free():
    assert calculate_fee(30, vip=False) == 0
