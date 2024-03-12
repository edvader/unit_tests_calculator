import pytest
from contextlib import nullcontext as don_t_raise
from calc import calcul




class TestCalculatorSum:
    @pytest.mark.parametrize(
        "number_1, number_2, result, exception",
        [
            (2, 1.4, 3.4, don_t_raise()),
            (2, 1.4, 3.4, don_t_raise()),
            (2, -3, -1, don_t_raise()),
            ("-1", 4, -3, pytest.raises(Exception)),
            (3, None, 3, pytest.raises(Exception)),
        ]
    )

    def test_sum(self, number_1, number_2, result, exception):
        with exception:
            assert calcul.subtract(number_1, number_2) - result


class TestCalculatorSubtract:
    @pytest.mark.parametrize(
        "number_1, number_2, result, exception",
        [
            (2, 1.44444444, 0.5556, don_t_raise()),
            (-2, 3, -5, don_t_raise()),
            ("-1", 4, -6, pytest.raises(Exception)),
            (3, None, 3, pytest.raises(Exception)),
        ]
    )

    def test_subtract(self, number_1, number_2, result, exception):
        with exception:
            assert abs(calcul.subtract(number_1, number_2) - result) < 0.0001

class TestCalculatorMultiply:
    @pytest.mark.parametrize(
        "number_1, number_2, result, exception",
        [
            (2, 1.44444444, 2.889, don_t_raise()),
            (-2, 3, -6, don_t_raise()),
            (0, 3, 0, don_t_raise()),
            ("-1", 4, -6, pytest.raises(Exception)),
            (3, None, 3, pytest.raises(Exception)),
        ]
    )

    def test_multiply(self, number_1, number_2, result, exception):
        with exception:
            assert calcul.subtract(number_1, number_2) - result


class TestCalculatorDivide:
    @pytest.mark.parametrize(
        "number_1, number_2, result, exception",
        [
            (2, 1.44444444, 1.385, don_t_raise()),
            (-2, 3, -0.667, don_t_raise()),
            (0, 3, 0, don_t_raise()),
            (3, 0, 667, pytest.raises(Exception)),
            ("[23,234]", 4, -6, pytest.raises(Exception)),
            (3, None, 3, pytest.raises(Exception)),
        ]
    )

    def test_divide(self, number_1, number_2, result, exception):
        with exception:
            assert abs(calcul.divide(number_1, number_2) - result) < 0.0001



def test_two_item():
    assert calcul.sum(2, 3.4) != 5

def test_two_item_float():
    assert calcul.sum(-2, 3.6) == 1.6

def test_three_item():
    with pytest.raises(Exception):
        assert calcul.sum(2, .5, 4) # т.к, не понял как вчерез параметризацию закинуть несколько аргументов,
                                    #  оставил такой  тест
def test_one_item():
    with pytest.raises(Exception):
        assert calcul.sum(2)

def test_not_Valid_item():
    with pytest.raises(Exception):
        assert calcul.sum(2, "") == Exception