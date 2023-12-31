
CURRENT_YEAR = 2017
VINTAGE_AGE = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def __iter__(self):
        return iter([self.name, self.year, self.cost])

