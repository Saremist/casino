from polynominal_folder.polynominal import Polynominal
import pytest


def test_Polynominal_str_normal1():
    assert str(Polynominal([])) == "0"


def test_Polynominal_str_normal_empty():
    assert str(Polynominal()) == "0"


def test_Polynominal_str_normal2():
    assert str(Polynominal([(0, -8)])) == "-8"


def test_Polynominal_str_normal3():
    assert str(Polynominal([(0, -4), (1, -2)])) == "-2x-4"


def test_Polynominal_str_normal4():
    assert str(Polynominal([(1, 5), (3, 2), (5, -1)])) == "-x^5+2x^3+5x"


def test_Polynominal_str_normal5():
    assert str(Polynominal([(4, 2), (7, 3), (2, 3), (0, 7)])) == "3x^7+2x^4+3x^2+7"


def test_Polynominal_errors1():
    with pytest.raises(ValueError):  # negative degree
        Polynominal([(1, 5), (-3, 7), (5, -1)])


def test_Polynominal_errors2():
    with pytest.raises(ValueError):  # zero value
        Polynominal([(1, 5), (3, 0), (5, -1)])


def test_Polynominal_errors_letters():  # letters in input
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


def test_Polynominal_value1():
    assert (Polynominal([(0, 2), (5, 2), (4, 3)]).value(10)) == 230002
    assert (Polynominal([(0, 2), (5, 2), (4, 3)]).value(5)) == 8127
    assert (Polynominal([(0, 2), (5, 2), (4, 3)]).value(2)) == 114
    assert (Polynominal([(0, 2), (5, 2), (4, 3)]).value(1)) == 7
    assert (Polynominal([(0, 2), (5, 2), (4, 3)]).value(0)) == 2


def test_Polynominal_value2():
    assert (Polynominal([(0, 2), (5, 2), (4, 3)]).value(-1)) == 3
    assert (Polynominal([(0, 2), (2, 5), (4, 3)]).value(-5)) == 2002
    assert (Polynominal([(0, 2), (3, 5), (6, 3)]).value(5)) == 47502
    assert (Polynominal([(0, 2), (3, 5), (6, 3)]).value(-5)) == 46252


def test_Polynominal_addition_error1():
    poli1 = Polynominal([(0, 2), (5, 2), (4, 3)])
    poli2 = "polynom additon error maker"
    with pytest.raises(TypeError):
        poli1.add(poli2)


def test_Polynominal_subtraction_error1():
    poli1 = Polynominal([(0, 2), (5, 2), (4, 3)])
    poli2 = "polynom additon error maker"
    with pytest.raises(TypeError):
        poli1.subtract(poli2)


def test_Polynom_sum0():
    poli1 = Polynominal([(0, 2), (5, 2), (4, 3)])
    poli2 = Polynominal([(0, 7), (7, 6), (4, 3)])
    poli1.subtract(poli2)
    assert poli1 == Polynominal([(0, -5), (7, -6), (5, 2)])


def test_Polynom_sum1():
    poli1 = Polynominal([(0, 2), (5, 2), (4, 3)])
    poli2 = Polynominal([(0, 7), (7, 6), (4, 3)])
    poli1.add(poli2)
    assert poli1 == Polynominal([(0, 9), (7, 6), (5, 2), (4, 6)])


def test_Polynom_sub1():
    poli1 = Polynominal()
    poli2 = Polynominal([(0, 7), (7, 6), (4, 3)])
    poli1.subtract(poli2)
    assert poli1 == Polynominal([(0, -7), (7, -6), (4, -3)])


def test_Polynom_sum20():
    poli1 = Polynominal()
    poli2 = Polynominal([(0, 7), (7, 6), (4, 3)])
    poli1.add(poli2)
    assert poli1 == Polynominal([(0, 7), (7, 6), (4, 3)])


def test_Polynom_sum21():
    poli1 = Polynominal([])
    poli2 = Polynominal([(0, 7), (7, 6), (4, 3)])
    poli1.add(poli2)
    assert poli1 == Polynominal([(0, 7), (7, 6), (4, 3)])


def test_Polynom_sub2():
    poli1 = Polynominal([(0, 2), (5, 2), (4, 3)])
    poli2 = Polynominal()
    # adding and subtracting zero equals itself
    poli1.subtract(poli2)
    assert poli1 == Polynominal([(0, 2), (5, 2), (4, 3)])


def test_Polynom_sub21():
    poli1 = Polynominal([(0, 2), (5, 2), (4, 3)])
    poli2 = Polynominal([])
    # adding and subtracting zero equals itself
    poli1.subtract(poli2)
    assert poli1 == Polynominal([(0, 2), (5, 2), (4, 3)])


def test_Polynom_sum3():
    poli1 = Polynominal([(0, 2), (5, 2), (4, 3)])
    poli2 = Polynominal()
    poli1.add(poli2)
    assert poli1 == Polynominal([(0, 2), (5, 2), (4, 3)])


def test_Polynom_coeff1():
    poli1 = Polynominal([(0, 2), (5, 2), (4, 3)])
    assert poli1.coefficient(5) == 2


def test_Polynom_coeff2():
    poli1 = Polynominal([(0, 2), (5, 2), (4, 3)])
    assert poli1.coefficient(0) == 2


def test_Polynom_degree1():
    poli1 = Polynominal([(0, 2), (7, 2), (11, 3)])
    assert poli1.degree() == 11


def test_Polynom_degree2():
    poli1 = Polynominal([(0, 2)])
    assert poli1.degree() == 0


def test_Polynom_degree3():
    poli1 = Polynominal([])
    assert poli1.degree() == 0


def test_Polynom_degree4():
    poli1 = Polynominal()
    assert poli1.degree() == 0


def test_Polynom_coeff_empty():
    poli1 = Polynominal([(0, 2), (5, 2), (4, 3)])
    assert poli1.coefficient(3) == 0
