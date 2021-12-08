import re
import numpy as np

def solve(input):
    listOfInstructions = []
    max = 0

    # method for filling nparray, where every occurence +1
    def fillDiagram(x1,y1,x2,y2, diagonalLines = False):
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        if ((x1 == x2)|(y1 == y2)):
            if y2 < y1:
                y1,y2 = y2,y1
            for i in range(x1,x2 + 1):
                for j in range (y1,y2 + 1):
                    if (diagram[j][i]>0):
                            diagram[j][i] = diagram[j][i]+1
                    else:
                            diagram[j][i] = 1

        # for diagonal lines
        elif (diagonalLines):
            if y2 > y1:
                for i in range(x2 - x1 + 1):
                    if (diagram[y1+i][x1+i] > 0):
                        diagram[y1+i][x1+i] = diagram[y1+i][x1+i]+1
                    else:
                        diagram[y1+i][x1+i]=1
            else:
                for i in range(x2 - x1 + 1):
                    if (diagram[y1-i][x1+i] > 0):
                        diagram[y1-i][x1+i] = diagram[y1-i][x1+i]+1
                    else:
                        diagram[y1-i][x1+i] = 1

    for line in input.splitlines():
        # using regular expression for parsing number values
        result = re.search(r'(\d*),(\d*) -> (\d*),(\d*)', line)
        # save x1, y1, x2, y2 coordinates to list
        listOfInstructions.append([int(result.group(1)), int(result.group(2)), int(result.group(3)), int(result.group(4))])

    for item in listOfInstructions:
        for number in item:
            if number > max:
                max = number

    # for 1st part
    diagram = np.full((max + 1,max + 1), -1)
    for instruction in listOfInstructions:
        fillDiagram(instruction[0],instruction[1],instruction[2],instruction[3], False)

    countOverlaps = np.count_nonzero(diagram >= 2)
    print("For part 1: " + str(countOverlaps) + " points do at least two lines overlap")

    # 2nd part
    diagram = np.full((max + 1, max + 1), -1)
    for instruction in listOfInstructions:
        fillDiagram(instruction[0], instruction[1], instruction[2], instruction[3], True)

    countOverlaps = np.count_nonzero(diagram >= 2)
    print("For part 2: " + str(countOverlaps) + " points do at least two lines overlap")

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()