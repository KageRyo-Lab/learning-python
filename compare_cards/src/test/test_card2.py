import pytest
from app.card import compare_cards

def tests_compare_cards():
    assert compare_cards('A', 'K') == 'A'
    assert compare_cards('5', '10') == '10'
    assert compare_cards('J', 'Q') == 'Q'
    assert compare_cards('2', '2') == 'Equal'
    
    with pytest.raises(ValueError):
        compare_cards('1', 'A')

    with pytest.raises(ValueError):
        compare_cards('A', 'B')  