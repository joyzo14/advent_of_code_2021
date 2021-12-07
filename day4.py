import numpy as np

def solve(input):
    listOfArrays = []
    lines = input.splitlines()
    helpArray = []
    firstBoardWin = False
    listOfBoardsWon = []

    # chosen numbers
    chosenNumbers = lines[0].split(",")

    # createing list of matrixes
    for i in range (2,len(lines)):
        if not lines[i].strip():
           listOfArrays.append(helpArray)
           helpArray = []
        else:
            helpArray.extend(lines[i].split())

            # for the last array
            if (i == len (lines) - 1):
                listOfArrays.append(helpArray)

    for i in range(len(chosenNumbers)):
        for array in listOfArrays:
            # checking range of chosen Numbers from
            if(checkIfBingo(chosenNumbers[:i], array)):
                set_difference = set(array) - set(chosenNumbers[:i])
                list_difference = list(map(int, set_difference))

                # only if first board won, print
                if not firstBoardWin:
                    print("Final score for first  part is: " + str(sum(list_difference)*int(chosenNumbers[:i][-1])))
                firstBoardWin = True

                # for 2nd part
                if array not in listOfBoardsWon:
                    listOfBoardsWon.append(array)
                if (len(listOfBoardsWon) == len(listOfArrays )):
                    print("Final score for second part is: " + str(sum(list_difference) * int(chosenNumbers[:i][-1])))
                    return

def checkIfBingo(chosenNumbers, array):
    npArray = np.array(array).reshape(5, 5)
    for line in npArray:
        flag = True
        for number in line:
            if number not in chosenNumbers:
                flag = False
        if (flag == True):
            #print(line)
            return True

    # because need to check colmumns
    npArray = np.rot90(npArray)
    for line in npArray:
        flag = True
        for number in line:
            if number not in chosenNumbers:
                flag = False
        if (flag == True):
            #print(line)
            return True

    return False


def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()