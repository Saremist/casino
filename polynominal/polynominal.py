class Polynominal:
    def __init__(self, all_powers=[]):
        self.powers = all_powers
        if self.powers:
            degrees = list(zip(self.powers))
            if 0 in degrees[1]:
                raise ValueError
        pass

    def _str_(self):
        for power in self.powers:
            pass
        pass  # returns str polynominal description

    def degree(self):
        max_degree = 0
        if self.powers:
            degrees = list(zip(self.powers))
            max_degree = max(degrees)
        # for degrees in self.powers:
        #     if degrees[0] > max_degree:
        #         max_degree = degrees[0]
        return max_degree

    def coefficient(degre_to_find):
        pass  # returns coefficient standing by chosen degree

    def value(x):
        pass  # calculates value for chosen x

    def add():
        pass  # returns sum of 2 polynominals

    def subtract():
        pass  # returns diff of 2 polynominals
