# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

n=[k for k in range (1,6+1)]
def main():
    # TODO: pass different arguments
    print(addition(5, 10, 15, 20))
    print(addition(*n))

    # TODO: pass an existing list
    myNums = [21,*n]
    # the star operator here acts like a spread operator
    print(addition(*myNums))

if __name__ == "__main__":
    main()
