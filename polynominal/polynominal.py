def add_plus(x):  # returns plus to be written if needed
    if x >= 0:
        return "+"
    return ""


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
        self._powers = sorted(all_powers, key=lambda tup: tup[0], reverse=True)
        self.transformed = transform(self._powers)
        if min(self.transformed[0]) < 0:  # checks for negative degriee
            raise ValueError("given degriee was negative")
        if (0, "") in (self.transformed[1]):
            raise ValueError("given correct degree with 0 value")
        pass

    def _str_(self):
        name = ""
        for power in self._powers:
            if power[0] == 0:
                name += f"{add_plus(power[1])}{power[1]}"
            elif power[0] == 1:
                name += f"{add_plus(power[1])}{power[1]}x"
            else:
                name += f"{add_plus(power[1])}{power[1]}x^{power[0]}"
        if name == "":
            name = "0"
        return name.strip("+")  # returns str polynominal description

    def degree(self):
        max_degree = 0
        max_degree = max(0, (max(self.transformed[0])))
        # max_degree = max(0, max(self.transformed))
        return max_degree

    def coefficient(self, degre_to_find):
        pass  # returns coefficient standing by chosen degree

    def value(x):
        pass  # calculates value for chosen x

    def add():
        pass  # returns sum of 2 polynominals

    def subtract():
        pass  # returns diff of 2 polynominals


if __name__ == "__main__":
    # print(Polynominal([])._str_())
    # print(Polynominal([(0, -8)])._str_())
    # print(Polynominal([(0, -4), (1, -2)])._str_())
    # print(Polynominal([(1, 5), (3, 2), (5, -1)])._str_())
    # print(Polynominal([(4, 2), (6, 3), (2, 3), (0, 7)])._str_())
    # print(Polynominal([])._str_())
    # print(Polynominal([(4, 2), (6, 3), (2, 3), (0, 7)]).degree())
    # print(Polynominal([(4, 1), (6, 5), (2, 3), (11, 7)]).degree())
    # print(Polynominal([(0, 2)]).degree())
    pass
