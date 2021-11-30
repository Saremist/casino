from polynominal_folder.polynominal import Polynominal
import pytest


def test_Polynominal_str_normal1():
    assert (Polynominal([])._str_()) == "0"


def test_Polynominal_str_normal2():
    assert (Polynominal([(0, -8)])._str_()) == "-8"


def test_Polynominal_str_normal3():
    assert (Polynominal([(0, -4), (1, -2)])._str_()) == "-2x-4"


def test_Polynominal_str_normal4():
    assert (Polynominal([(1, 5), (3, 2), (5, -1)])._str_()) == "-x^5+2x^3+5x"


def test_Polynominal_str_normal5():
    assert (Polynominal([(4, 2), (7, 3), (2, 3), (0, 7)])._str_()) == "3x^7+2x^4+3x^2+7"


def test_Polynominal_errors1():
    with pytest.raises(ValueError):
        Polynominal([(1, 5), (-3, 7), (5, -1)])


def test_Polynominal_errors2():
    with pytest.raises(ValueError):
        Polynominal([(1, 5), (3, 0), (5, -1)])


def test_Polynominal_errors_letters():
    with pytest.raises(TypeError):
        Polynominal([("error?", 5), (3, 0), (5, -1)])
    with pytest.raises(TypeError):
        Polynominal([(1, 5), (3, "errors!"), (5, -1)])
    with pytest.raises(TypeError):
        Polynominal([("error?", 5), (3, 0), (5, "errors")])


def test_Polynominal_deg_normal1():
    assert (Polynominal([(4, 2), (6, 3), (2, 3), (0, 7)]).degree()) == 6


def test_Polynominal_deg_normal2():
    assert (Polynominal([(4, 1), (6, 5), (2, 3), (11, 7)]).degree()) == 11


def test_Polynominal_deg_normal_3():
    assert (Polynominal([(0, 2)]).degree()) == 0


def test_Polynominal_value():
    assert (Polynominal([(0, 2), (5, 2), (4, 3)]).value(10)) == 30502
    assert (Polynominal([(0, 2), (5, 2), (4, 3)]).value(5)) == 2002
    assert (Polynominal([(0, 2), (5, 2), (4, 3)]).value(2)) == 70
    assert (Polynominal([(0, 2), (5, 2), (4, 3)]).value(1)) == 10
    assert (Polynominal([(0, 2), (5, 2), (4, 3)]).value(0)) == 2
    assert (Polynominal([(0, 2), (5, 2), (4, 3)]).value(-1)) == 10
    assert (Polynominal([(0, 2), (2, 5), (4, 3)]).value(-5)) == 2002
    assert (Polynominal([(0, 2), (3, 5), (6, 3)]).value(5)) == 47502
    assert (Polynominal([(0, 2), (3, 5), (6, 3)]).value(-5)) == 46252
