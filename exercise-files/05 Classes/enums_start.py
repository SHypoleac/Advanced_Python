# define enumerations using the Enum base class
"""
Advanced Classes and Objects: Defining enumerations
- Duplicate names (keys) are not allowed
- Duplicate values *are* allowed,
  unless using the `unique` decorator, applied to the class
- the `auto` function automatically assigns values to enums
- you can use enums as hash values
"""

from enum import Enum, unique, auto

@unique
class Fruit(Enum):
    APPLE = 17
    BANANA = 26
    ORANGE = 35
    TOMATO = 44
    PEAR = auto()

def main():
    pass
    # TODO: enums have human-readable values and types
    print(type(Fruit.APPLE)) # class type
    print(repr(Fruit.APPLE)) # string containing a printable representation of an object

    # TODO: enums have name and value properties
    print(Fruit.APPLE.name,"=", Fruit.APPLE.value)

    # TODO: print the auto-generated value
    print(Fruit.PEAR.name,"=",Fruit.PEAR.value)

    # TODO: enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "I want the power of fire"
    print(myFruits[Fruit.BANANA])


if __name__ == "__main__":
    main()
