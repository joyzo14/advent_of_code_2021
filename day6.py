def solve(input):
    stringOfNumbers = ''.join([(x) for x in input.split(",")])

    dictOfNumbers = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}

    for number in stringOfNumbers:
        dictOfNumbers[number] += 1

    for i in range(256):
        # count of 9's is helping key for keeping count of zeros before replacing
        dictOfNumbers["9"] = dictOfNumbers["0"]
        dictOfNumbers["0"] = dictOfNumbers["1"]
        dictOfNumbers["1"] = dictOfNumbers["2"]
        dictOfNumbers["2"] = dictOfNumbers["3"]
        dictOfNumbers["3"] = dictOfNumbers["4"]
        dictOfNumbers["4"] = dictOfNumbers["5"]
        dictOfNumbers["5"] = dictOfNumbers["6"]
        dictOfNumbers["6"] = dictOfNumbers["7"]
        dictOfNumbers["7"] = dictOfNumbers["8"]

        # count of 8's is count of zeros before them replacement
        dictOfNumbers["8"] = dictOfNumbers["9"]
        # every 0's before became now 6's
        dictOfNumbers["6"] += dictOfNumbers["9"]
        # reset item in 9's because if I keep it, result will be wrong
        dictOfNumbers["9"] = 0

        if (i == 79):
            result = 0
            for key in dictOfNumbers:
                    result += dictOfNumbers[key]
            print("Count of all fishes after 80 iteration is: " + str(result))
        if (i == 255):
            result = 0
            for key in dictOfNumbers:
                result += dictOfNumbers[key]
            print("Count of all fishes after 256 iteration is: " + str(result))

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()