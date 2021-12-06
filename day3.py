def solve(input):
    lenOfBinaryNumbers = len(input.splitlines()[0])
    listOfZeros = [0] * lenOfBinaryNumbers
    listOfOnes = [0] * lenOfBinaryNumbers
    listOfBinaryNumbers = input.splitlines()

    for item in listOfBinaryNumbers:
        for i in range (len(item)):
            if (item[i] == "0"):
                listOfZeros[i] += 1
            if (item[i] == "1"):
                listOfOnes[i] += 1

    gammaRate = [""] * lenOfBinaryNumbers
    epsilonRate = [""] * lenOfBinaryNumbers

    for i in range(len(listOfZeros)):
        if (listOfOnes[i]>listOfZeros[i]):
            gammaRate[i] = "1"
            epsilonRate[i] = "0"
        else:
            gammaRate[i] = "0"
            epsilonRate[i] = "1"


    gammaRateDecimal = binaryToDecimal("".join(gammaRate))
    epsilonRateDecimal = binaryToDecimal("".join(epsilonRate))

    print("Power consumption of the submarine is: " + str(gammaRateDecimal*epsilonRateDecimal))

    # PART TWO

    listOfBinaryNumbersCopy = listOfBinaryNumbers.copy()
    index = 0

    while(True):
        zeros = sum(1 for item in listOfBinaryNumbersCopy if item[index] == "0")
        ones = sum(1 for item in listOfBinaryNumbersCopy if item[index] == "1")

        if ones >= zeros:
            listOfBinaryNumbersCopy = [x for x in listOfBinaryNumbersCopy if x[index] == "1"]
        else:
            listOfBinaryNumbersCopy = [x for x in listOfBinaryNumbersCopy if x[index] == "0"]

        if (len(listOfBinaryNumbersCopy) == 1):
            oxygenGeneratorRating = binaryToDecimal("".join(listOfBinaryNumbersCopy))
            break
        index += 1

    listOfBinaryNumbersCopy = listOfBinaryNumbers.copy()
    index = 0

    while (True):
        zeros = sum(1 for item in listOfBinaryNumbersCopy if item[index] == "1")
        ones = sum(1 for item in listOfBinaryNumbersCopy if item[index] == "0")

        if zeros >= ones:
            listOfBinaryNumbersCopy = [x for x in listOfBinaryNumbersCopy if x[index] == "0"]
        else:
            listOfBinaryNumbersCopy = [x for x in listOfBinaryNumbersCopy if x[index] == "1"]

        if (len(listOfBinaryNumbersCopy) == 1):
            co2ScrubberRrating = binaryToDecimal("".join(listOfBinaryNumbersCopy))
            break
        index += 1

    print("The life support rating of the submarine is: " + str(oxygenGeneratorRating * co2ScrubberRrating))


def binaryToDecimal(number):
    return int(number, 2)


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()