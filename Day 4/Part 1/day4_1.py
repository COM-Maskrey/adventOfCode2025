try:
    countOfAccessibleRolls = 0
    previousRow = ''
    currentRow = ''
    nextRow = ''
    rowNumber = 1
    with open('Day 4/Part 1/Day_4_1_input.csv', 'r') as inputFile:
        while True:
            rowOfRolls = inputFile.readline().strip("\n")
            if rowOfRolls == '':
                nextRow = '.' * len(currentRow)
            else:
                nextRow = rowOfRolls
            if currentRow == '':
                previousRow = '.' * len(rowOfRolls)
                currentRow = rowOfRolls
                continue
            for index in range(len(currentRow)):
                if currentRow[index] == '.':
                    continue
                countRollsAround = 0
                for count in range(8):
                    match count:
                        case 0: # Left
                            if index - 1 >= 0:
                                if currentRow[index - 1] == '@':
                                    countRollsAround += 1
                        case 1: # Top-Left
                            if index - 1 >= 0:
                                if previousRow[index - 1] == '@':
                                    countRollsAround += 1
                        case 2: # Top-centre
                            if previousRow[index] == '@':
                                countRollsAround += 1
                        case 3: # Top-Right
                            if index + 1 < len(currentRow):
                                if previousRow[index + 1] == '@':
                                    countRollsAround += 1
                        case 4: # Right
                            if index + 1 < len(currentRow):
                                if currentRow[index + 1] == '@':
                                    countRollsAround += 1
                        case 5: # Bottom-Right
                            if index + 1 < len(currentRow):
                                if nextRow[index + 1] == '@':
                                    countRollsAround += 1
                        case 6: # Bottom
                            if nextRow[index] == '@':
                                countRollsAround += 1
                        case 7: # Bottom-Left
                            if index - 1 >= 0:
                                if nextRow[index - 1] == '@':
                                    countRollsAround += 1
                if countRollsAround < 4:
                    countOfAccessibleRolls += 1
                #print(f"Index: {index}, RollsAround: {countRollsAround}, countOfAccessibleRolls: {countOfAccessibleRolls}")
            previousRow = currentRow
            currentRow = nextRow
            print(f"{rowNumber} - Accessible Rolls So Far: {countOfAccessibleRolls}  ")
            if rowOfRolls == '':
                break
            rowNumber += 1
    print(f"Count of Accessible Rolls: {countOfAccessibleRolls}")

except Exception as e:
    print(f"Error reading input file. Error: {e}")