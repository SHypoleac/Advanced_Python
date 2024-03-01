# give objects number-like behavior


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Point x:{self.x},y:{self.y}>"

    # TODO: implement addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # TODO: implement subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # TODO: implement in-place addition
    # modify the object itself, instead of returning a new one
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

def main():
    # Declare some points
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    # TODO: Add two points
    p3 = p1 + p2
    print(f"Point p1+p2 is : {p3}")

    # TODO: subtract two points
    p4 = p1-p2
    print(f"Point p1-p2 is : {p4}")

    # TODO: Perform in-place addition
    p1 += p4
    print(f"p1+p1-p2 is : {p1}")

if __name__ == "__main__":
    main()
