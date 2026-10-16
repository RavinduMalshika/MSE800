import pytest

def test_three_days():
    assert fee(3, 50) == 150
    
def test_eight_days():
    assert fee(8, 50) == pytest.approx(360)
    
def test_less_than_one_day():
    with pytest.raises(ValueError, match="days cannot be less than one"):
        fee(0, 50)
 
def fee(days, rate):
    if days < 1:
        raise ValueError("days cannot be less than one")
    elif days > 7 :
        return days * rate * 0.9
    else:
        return days * rate


