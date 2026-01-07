from app import calculate_final_amount

def test_gold_member():
    # 20% discount on any amount
    assert calculate_final_amount(1000, "Gold") == 944.0
    assert calculate_final_amount(2000, "gold") == 1888.0

def test_silver_member_above_1000():
    # 10% discount
    assert calculate_final_amount(1500, "Silver") == 1593.0

def test_silver_member_below_1000():
    # 5% discount
    assert calculate_final_amount(800, "Silver") == 896.8

def test_regular_member_above_2000():
    # 5% discount
    assert calculate_final_amount(2500, "Regular") == 2807.5

def test_regular_member_below_2000():
    # No discount
    assert calculate_final_amount(1500, "Regular") == 1770.0
