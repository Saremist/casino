def add_plus(x):  # returns plus to be written if needed
    if x >= 0:
        return "+"
    return ""


class Polynominal:
    def __init__(self, all_powers=[]):
        self.powers = sorted(all_powers, key=lambda tup: tup[0], reverse=True)
        if self.powers:
            degrees = list(zip(self.powers[0]))
            if 0 in (degrees[1]) or min(degrees[0]) < 0:  # checks for
                raise ValueError
        pass

    def _str_(self):
        name = ""
        for power in self.powers:
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
        if self.powers:
            degrees = list(zip(self.powers))
            max_degree = max(degrees)
        return max_degree

    def coefficient(degre_to_find):

        pass  # returns coefficient standing by chosen degree

    def value(x):
        pass  # calculates value for chosen x

    def add():
        pass  # returns sum of 2 polynominals

    def subtract():
        pass  # returns diff of 2 polynominals


if __name__ == "__main__":
    print(Polynominal([])._str_())
    print(Polynominal([(0, -8)])._str_())
    print(Polynominal([(0, -4), (1, -2)])._str_())
    print(Polynominal([(1, 5), (3, 2), (5, -1)])._str_())
    print(Polynominal([(4, 2), (6, 3), (2, 3), (0, 7)])._str_())
    print(Polynominal([])._str_())
