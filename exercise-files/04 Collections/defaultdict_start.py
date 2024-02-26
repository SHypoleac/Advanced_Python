# Demonstrate the usage of defaultdict objects

def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    # if I try to access a key that doesn't exist,
    # create a default value for me using
    # `int` object as a constructor
    fruitCounter = {fruit:fruits.count(fruit) for fruit in fruits}

    # Count the elements in the list
    # for fruit in fruits:
    #     fruitCounter[fruit] += 1

    # # print the result
    #for (k, v) in fruitCounter.items():
        #print(k + ": " + str(v))
    print(*(f"{k} : {v}\n" for k, v in fruitCounter.items()))

#:P


if __name__ == "__main__":
    main()
