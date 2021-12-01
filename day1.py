def solve(input):

    measurements = input.splitlines()

    count = 0
    for i in range(len(measurements)-1):
        if(int(measurements[i]) < int(measurements[i+1])):
            count +=1

    print(str(count) + " measurements are larger than the previous measurement")

    # 2nd part
    listOfSums=[] #list of triples
    for i in range(len(measurements)-2):
        listOfSums.append(int(measurements[i]) + int(measurements[i+1]) + int(measurements[i+2]))

    count = 0
    for i in range(len(listOfSums) - 1):
        if (int(listOfSums[i]) < int(listOfSums[i + 1])):
            count += 1

    print(str(count) + " sums are larger than the previous sum")

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()