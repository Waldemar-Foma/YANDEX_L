class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
