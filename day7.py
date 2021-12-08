import sys

def solve(input):
    listOfNumbers = [int(x) for x in input.split(",")]

    minHorizontal = min(listOfNumbers)
    maxHorizontal = max(listOfNumbers)

    sum = 0
    minSum = sys.maxsize
    for i in range (minHorizontal, maxHorizontal+1):
        for number in listOfNumbers:
            sum += abs(number - i)
        if (sum < minSum):
            minSum = sum
        sum = 0

    print("For part 1: " + str(minSum) + " fuel must they spend to align position.")

    # PART 2
    sum = 0
    minSum = sys.maxsize
    for i in range(minHorizontal, maxHorizontal + 1):
        for number in listOfNumbers:
            sum += fuelSum(abs(number - i))
        if (sum < minSum):
            minSum = sum
        sum = 0

    print("For part 2: " + str(minSum) + " fuel must they spend to align position.")

def fuelSum (number):
    sum = 0
    for i in range(1, number+1):
        sum+=i

    return sum

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)

if __name__ == '__main__':
    main()