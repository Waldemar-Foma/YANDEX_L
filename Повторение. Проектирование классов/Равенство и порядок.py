class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.name, self.x, self.y) == (other.name, other.x, other.y)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.name, self.x, self.y) < (other.name, other.x, other.y)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
