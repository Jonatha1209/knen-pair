class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f"Pair({self.first}, {self.second})"

    def __eq__(self, other):
        if isinstance(other, Pair):
            return self.first == other.first and self.second == other.second
        return False

    def __add__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first + other.first, self.second + other.second)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first - other.first, self.second - other.second)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first * other.first, self.second * other.second)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first / other.first, self.second / other.second)
        return NotImplemented
