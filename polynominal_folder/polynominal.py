def add_sign(x):
    """
    returns plus to be written if needed
    used in _str_
    """
    if x >= 0:
        return "+"
    return "-"


def validate_for_add(polynom):
    if not isinstance(polynom, Polynominal):
        raise TypeError("trying to add not polynominal")


def abs_not_one(x):
    """
    used in turning polynominal into _str_
    """
    a_x = abs(x)  # abs value of x
    if a_x == 1:
        return ""
    else:
        return a_x


def validate_input(list_to_be_checked):
    for single_power in list_to_be_checked:
        val = single_power[1]
        degree = single_power[0]
        if not isinstance(val, (int, float)):
            raise TypeError("input for value is not int or float type")
        if not isinstance(degree, int):
            raise TypeError("input for degree is not int type")
    if list_to_be_checked:
        transf = transform(list_to_be_checked)
        if min(transf[0]) < 0:  # checks for negative degriee
            raise ValueError("given degriee was negative")
        if 0 in (transf[1]):
            raise ValueError("given correct degree with 0 value")


def transform(terms):
    """
    returns transformed list in top down organization
    """
    if not terms:
        return [[], []]  # protects from empty input polynominal
    return list(map(list, zip(*terms)))


class Polynominal:
    """
    Polynominal object described by ax^n + bx^m + [...] + c
    a is float and n is int type

    __init__(self, all_powers) all_powers is formated as follows:
            [(n,a), (m,b), ..., (0, c)]

    Methods included:
        degree(self)
        coefficient(self, degre_to_find)
        value(self, x)
        add(self, polynom)
        subtract(self, polynom)
    """

    def __init__(self, all_powers=None):
        if not all_powers:
            all_powers = []
        validate_input(all_powers)
        self._powers = []
        for element in sorted(all_powers, key=lambda tup: tup[0], reverse=True):
            self._powers.append(list(element))
        self._transformed = transform(self._powers)

    def __eq__(self, other):
        """
        polynominals are equal if all coefficients and values are equal
        """
        if self._powers == other._powers:
            return True
        return False

    def __str__(self):
        """
        creates matematical string of polynominal
        """
        name = ""
        for power in self._powers:
            if abs(power[0]) == 0:
                name += f"{add_sign(power[1])}{abs_not_one(power[1])}"
            elif power[0] == 1:
                name += f"{add_sign(power[1])}{abs_not_one(power[1])}x"
            else:
                name += f"{add_sign(power[1])}{abs_not_one(power[1])}x^{power[0]}"
        if name == "":
            name = "0"
        return str(name.strip("+"))  # returns str polynominal description

    def degree(self):
        """
        returns max degree (degree of whole polyniminal)
        """
        max_degree = 0
        if not self._transformed[0] == []:
            max_degree = max(0, (max(self._transformed[0])))
            return max_degree
        else:
            return 0

    def coefficient(self, degre_to_find):
        """
        returns value of coefficient standing next to chosen degre
        """
        try:
            index = self._transformed[0].index(degre_to_find)
        except ValueError:
            return 0
        return self._transformed[1][index]
        # returns coefficient standing by chosen degree

    def value(self, x):
        """
        returns calculatef value of polynom for chosen X
        """
        sum_value = 0
        for power in self._powers:
            sum_value += (x ** power[0]) * power[1]  # calculates value for chosen x
        return sum_value

    def add(self, polynom):
        """
        ads in place 2 polynominals
        """
        validate_for_add(polynom)
        for element in polynom._powers:
            power, val = element
            # if element power is already in our polynominal
            if power in self._transformed[0]:
                index = self._transformed[0].index(power)
                self._powers[index][1] += val
            else:
                self._powers.append([power, val])
                self._powers.sort(reverse=True)
            # remakes transformed list including new values
            for id, power in enumerate(self._powers):
                if power[1] == 0:
                    self._powers.pop(id)
            self._transformed = transform(self._powers)

    def subtract(self, polynom):
        """
        subtracts in place 2 polynominals
        uses negation of polynom and .add()
        """
        validate_for_add(polynom)
        negated_polynom = []
        if polynom:
            for element in polynom._powers:
                negated_polynom.append((element[0], -1 * element[1]))
        polynom._powers = negated_polynom
        self.add(polynom)


if __name__ == "__main__":
    my_poly = Polynominal([(0, 2), (5, 2), (4, 3)])
    to_add = Polynominal()
    my_poly.subtract(to_add)
    print(str(my_poly))
    print(my_poly == Polynominal([(0, 2), (5, 2), (4, 3)]))
    pass
