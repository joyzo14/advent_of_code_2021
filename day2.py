import re

def solve(input):

    listOfInstructions = []
    horizontalposition = 0
    depth = 0

    for item in input.splitlines():
        result = re.search(r'(\w*) (\d*)', item)
        listOfInstructions.append([result.group(1),int(result.group(2))])

    for instruction in listOfInstructions:
        if instruction[0]=="forward":
            horizontalposition += instruction[1]
        if instruction[0]=="up":
            depth -= instruction[1]
        if instruction[0]=="down":
            depth += instruction[1]

    print("If you multiply your final horizontal position " + str(horizontalposition) + " by your final depth " + str(depth) + " you get result " + str(horizontalposition*depth))

    # Part II

    aim = 0
    horizontalposition = 0
    depth = 0

    for instruction in listOfInstructions:
        if instruction[0]=="forward":
            horizontalposition += instruction[1]
            depth+= instruction[1] * aim
        if instruction[0]=="up":
            aim -= instruction[1]
        if instruction[0]=="down":
            aim += instruction[1]

    print("In Part II if you multiply your final horizontal position " + str(horizontalposition) + " by your final depth " + str(depth) + " you get result " + str(horizontalposition*depth))

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()