# Demonstrate the use of keyword-only arguments
'''
you can separate positional arguments from arguments
which are keyword-only using an asterisk
'''

# use keyword-only arguments to help ensure code clarity

from itertools import count


def myFunction(arg1, arg2, *args, suppressExceptions=False):
    if suppressExceptions:
        return ((arg1*arg2)+sum([a for a in args]))
    else :
        return ((arg1*arg2)-sum([a for a in args]))


def main():
    # try to call the function without the keyword

    print(myFunction(1, 2,5,1, suppressExceptions=True))
    # use the keyword
    print(myFunction(2, 2,1, suppressExceptions=False))



if __name__ == "__main__":
    main()
