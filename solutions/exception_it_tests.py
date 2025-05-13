import pytest
from contextlib import nullcontext as does_not_raise


def devision(x,y):
    return x / y


@pytest.mark.parametrize("x, y, res, exception", [
    (6, 3, 2, does_not_raise()),
    (-6, 1.5, -4, does_not_raise()),
    (0, 1, 0, does_not_raise()),
    (1, 0, 0, pytest.raises(ZeroDivisionError))
])
def test_devision(x, y, res, exception):
    with exception:
        assert devision(x, y) == res
