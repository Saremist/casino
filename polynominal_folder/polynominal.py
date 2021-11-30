from _typeshed import Self


def add_sign(x):  # returns plus to be written if needed
    if x >= 0:
        return "+"
    return "-"


def abs_not_one(x):
    a_x = abs(x)  # abs value of x
    if a_x == 1:
        return ""
    else:
        return a_x


def validate_input(list_to_be_checked):
    for single_power in list_to_be_checked:
        for element in single_power:
            if not isinstance(element, int):
                raise TypeError("input value is not int type")


def transform(powers):
    # returns transformed list in top down organization
    degrees = []
    values = []
    for pair in powers:
        degrees.append(pair[0])
        values.append(pair[1])
    return (degrees, values)


class Polynominal:
    def __init__(self, all_powers=[]):
        validate_input(all_powers)
        self._powers = sorted(all_powers, key=lambda tup: tup[0], reverse=True)
        self.transformed = transform(self._powers)
        if self._powers:
            if min(self.transformed[0]) < 0:  # checks for negative degriee
                raise ValueError("given degriee was negative")
            if 0 in (self.transformed[1]):
                raise ValueError("given correct degree with 0 value")

    def _str_(self):
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
        return name.strip("+")  # returns str polynominal description

    def degree(self):
        max_degree = 0
        max_degree = max(0, (max(self.transformed[0])))
        # max_degree = max(0, max(self.transformed))
        return max_degree

    def coefficient(self, degre_to_find):
        index = self.transformed[0].index(degre_to_find)
        return self.transformed[1][index]
        # returns coefficient standing by chosen degree

    def value(self, x):
        sum_value = 0
        for degree, value in self.transformed:
            sum_value += x ^ degree * value  # calculates value for chosen x
        return sum_value

    def add(self):
        pass  # returns sum of 2 polynominals

    def subtract(self):
        pass  # returns diff of 2 polynominals


if __name__ == "__main__":
    print(Polynominal([(1, 5), (3, 2), (5, -1)])._str_())
    pass
