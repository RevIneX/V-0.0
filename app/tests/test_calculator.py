import pytest
from app.core.calculator import calculate


def test_calculate():
    assert calculate(2, 3, '+') == 5


@pytest.mark.parametrize("a,b,op,expected", [
    (6, 3, 'divmod', 2),
    (5, 3, '**', 125),
    (-2, -3, '*', 6),
    (2, 3, '*', 6),
    (0, 5, '*', 0),
    (6, 3, '/', 2.0),
    (5, 2, '/', 2.5),
    (5, 2, '//', 2),
    (6, 4, '%', 2),
    (2, 3, '?', 5),
    (-2, 3, '+', 1),
    (2, 3, '+', 5),
    (0, 5, '+', 5),
    (2, 3, '-', -1),
    (5, 3, '-', 2),
])
def test_all_operations(a, b, op, expected):
    if op is None:
        assert calculate(a, b) == expected
    else:
        assert calculate(a, b, op) == expected


@pytest.mark.parametrize("a,b,op", [
    (1, 0, 'divmod'),
    (1, 0, '//'),
    (1, 0, '/'),
    (1, 0, '%'),
])
def test_division_by_zero(a, b, op):
    with pytest.raises(ValueError, match="DIVISION BY ZERO"):
        calculate(a, b, op)
