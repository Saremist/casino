from ..polynominal_folder.polynominal import Polynominal
import pytest


def test_Polynominal_str_normal():
    assert (Polynominal([])._str_()) == "0"
    assert (Polynominal([(0, -8)])._str_()) == "-8"
    assert (Polynominal([(0, -4), (1, -2)])._str_()) == "-2x+4"
    assert (Polynominal([(1, 5), (3, 2), (5, -1)])._str_()) == "-x^5+2x^3+5x"
    assert (Polynominal([(4, 2), (7, 3), (2, 3), (0, 7)])._str_()) == "3x^7+2x^4+3x^2+7"


def test_Polynominal_errors():
    with pytest.raises(ValueError):
        Polynominal([(1, 5), (-3, 7), (5, -1)])
    with pytest.raises(ValueError):
        Polynominal([(1, 5), (3, 0), (5, -1)])
    # (Polynominal([])._str_())
    # (Polynominal([(4, 2), (6, 3), (2, 3), (0, 7)]).degree())
    # (Polynominal([(4, 1), (6, 5), (2, 3), (11, 7)]).degree())
    # (Polynominal([(0, 2)]).degree())
