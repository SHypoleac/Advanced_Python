# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]
    ftemps1 = [(t*9/5)+32 for t in ctemps]
    print("table :",ftemps1)

    # TODO: build a set of unique Fahrenheit temperatures
    ftemps2 = {(t*9/5)+32 for t in ctemps}
    print("set: ",ftemps2)
    
    ftemps3=[]
    for t in ftemps1:
        if t in ftemps3 and ftemps1.count(t)>1:
            pass
        else: ftemps3.append(t)

    print("table without duplicates :",ftemps3)

    # TODO: build a set from an input source
    sTemp = "The quick brown fox jumped over the lazy dog"
    # includes whitespace
    chars = {c.upper() for c in sTemp}
    print(chars)
    # excludes whitespace
    chars = {c.upper() for c in sTemp if not c.isspace()}
    #print(chars)

if __name__ == "__main__":
    main()
