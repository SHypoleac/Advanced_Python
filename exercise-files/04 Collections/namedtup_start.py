# Demonstrate the usage of namdtuple objects

from collections import namedtuple


def main():
    # TODO: create a Point namedtuple
    Point = namedtuple("Point", "wartosc nazwa bool")
    p1 = Point(365,"dni_roku",False)
    p2 = Point(1,"tak",True)
    print(p1, p2)
    # use descriptive names to access the data
    print(type(p1.nazwa),p1.nazwa,type(p1.bool),p1.bool)

    # TODO: use _replace to create a new instance (a helper function)
    p1 = p1._replace(nazwa=str(100))
    print(type(p1.nazwa),p1.nazwa)


if __name__ == "__main__":
    main()
