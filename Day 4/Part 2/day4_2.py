try:
    countOfAccessibleRolls = 0
    totalPasses = 0
    rowNumber = 1
    allTheRolls = []
    with open('Day 4/Part 2/Day_4_2_Input.csv', 'r') as inputFile:
        # 1 - Load all rolls locations into an array
        while True:
            rowOfRolls = inputFile.readline().strip("\n")
            if rowNumber == 1:
                allTheRolls.append('.' * (len(rowOfRolls)))
                rowNumber += 1
            if rowOfRolls == '':
                allTheRolls.append('.' * lengthOfRow)
                break
            else:
                allTheRolls.append(rowOfRolls)
            lengthOfRow = len(rowOfRolls)
            rowNumber += 1
        totalRows = rowNumber
        # 2 - Loop until no more accessible rolls found
        while True:
            accessibleRollsFoundThisPass = 0
            # 3 - Process each row of rolls
            for rowOfRolls in range(len(allTheRolls) - 1):
                if rowOfRolls == 0:
                    continue # Skip first row as it is all '.'
                # 4 - For each column in the row
                for colOfRolls in range(len(allTheRolls[rowOfRolls])): 
                    if allTheRolls[rowOfRolls][colOfRolls] == '.': # Empty slot so skip to next slot
                        continue
                    countRollsAround = 0
                    for count in range(8):
                        match count:
                            case 0: # Left
                                if colOfRolls - 1 >= 0:
                                    if allTheRolls[rowOfRolls][colOfRolls - 1] in ['@', 'x']:
                                        countRollsAround += 1
                            case 1: # Top-Left
                                if colOfRolls - 1 >= 0:
                                    if allTheRolls[rowOfRolls - 1][colOfRolls - 1] in ['@', 'x']:
                                        countRollsAround += 1
                            case 2: # Top-centre
                                if allTheRolls[rowOfRolls - 1][colOfRolls] in ['@', 'x']:
                                    countRollsAround += 1
                            case 3: # Top-Right
                                if colOfRolls + 1 < len(allTheRolls[rowOfRolls - 1]):
                                    if allTheRolls[rowOfRolls - 1][colOfRolls + 1] in ['@', 'x']:
                                        countRollsAround += 1
                            case 4: # Right
                                if colOfRolls + 1 < len(allTheRolls[rowOfRolls - 1]):
                                    if allTheRolls[rowOfRolls][colOfRolls + 1] in ['@', 'x']:
                                        countRollsAround += 1
                            case 5: # Bottom-Right
                                if colOfRolls + 1 < len(allTheRolls[rowOfRolls - 1]):
                                    if allTheRolls[rowOfRolls + 1][colOfRolls + 1] in ['@', 'x']:
                                        countRollsAround += 1
                            case 6: # Bottom
                                if allTheRolls[rowOfRolls + 1][colOfRolls] in ['@', 'x']:
                                    countRollsAround += 1
                            case 7: # Bottom-Left
                                if colOfRolls - 1 >= 0:
                                    if allTheRolls[rowOfRolls + 1][colOfRolls - 1] in ['@', 'x']:
                                        countRollsAround += 1
                    # If the roll is accessible, mark it as an 'x' and increase the count
                    if countRollsAround < 4:
                        accessibleRollsFoundThisPass += 1
                        if colOfRolls == 0:
                            allTheRolls[rowOfRolls] = 'x' + allTheRolls[rowOfRolls][1:]
                        elif colOfRolls == len(allTheRolls[rowOfRolls]) - 1:
                            allTheRolls[rowOfRolls] = allTheRolls[rowOfRolls][0:len(allTheRolls[rowOfRolls]) - 1] + 'x'
                        else:
                            allTheRolls[rowOfRolls] = allTheRolls[rowOfRolls][0:colOfRolls] + 'x' + allTheRolls[rowOfRolls][colOfRolls + 1:]
            totalPasses += 1
            if accessibleRollsFoundThisPass == 0:
                break
            else:
                countOfAccessibleRolls += accessibleRollsFoundThisPass
            # Change all the x to . for next pass
            for rowOfRolls in range(len(allTheRolls) - 1):
                allTheRolls[rowOfRolls] = allTheRolls[rowOfRolls].replace('x', '.')
            print(f"Pass {totalPasses} complete. Accessible Rolls found this pass: {accessibleRollsFoundThisPass}. Total so far: {countOfAccessibleRolls}.")

    print(f"Count of Accessible Rolls: {countOfAccessibleRolls} after {totalPasses} passes.")

except Exception as e:
    print(f"Error reading input file. Error: {e}")