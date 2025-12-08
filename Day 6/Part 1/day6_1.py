try:
    countOfFreshIngredients = 0
    arrayOfNumbers = []
    rowOfSigns= []
    rowOfTotals = []
    rowIndex = 0
    with open('Day 6/Part 1/Day_6_1_input.csv', 'r') as inputFile:
        # Load all the numbers and signs into arrays
        while True:
            fileRecord = inputFile.readline().strip("\n")
            if fileRecord == '':
                break
            while '  ' in fileRecord:
                fileRecord = fileRecord.replace('  ', ' ')
            if fileRecord[0] == ' ':
                fileRecord = fileRecord[1:]
            lineOfNumbers = fileRecord.split(' ')
            if not lineOfNumbers[0].isdigit():
                rowOfSigns = lineOfNumbers
            else:
                arrayOfNumbers.append([int(x) for x in lineOfNumbers])
        
        # Carry out the equations and store the totals
        for columnIndex in range(len(rowOfSigns)):
            answer = 0
            if rowOfSigns[columnIndex] == '+':
                for rowIndex in range(len(arrayOfNumbers)):
                    if answer == 0:
                        answer = arrayOfNumbers[rowIndex][columnIndex]
                    else:
                        answer += arrayOfNumbers[rowIndex][columnIndex]
            elif rowOfSigns[columnIndex] == '*':
                for rowIndex in range(len(arrayOfNumbers)):
                    if answer == 0:
                        answer = arrayOfNumbers[rowIndex][columnIndex]
                    else:
                        answer *= arrayOfNumbers[rowIndex][columnIndex]
            elif rowOfSigns[columnIndex] == '-':
                for rowIndex in range(len(arrayOfNumbers)):
                    if answer == 0:
                        answer = arrayOfNumbers[rowIndex][columnIndex]
                    else:
                        answer -= arrayOfNumbers[rowIndex][columnIndex]
            elif rowOfSigns[columnIndex] == '/':
                for rowIndex in range(len(arrayOfNumbers)):
                    if answer == 0:
                        answer = arrayOfNumbers[rowIndex][columnIndex]
                    else:
                        answer /= arrayOfNumbers[rowIndex][columnIndex]
            else:
                answer = 0
            rowOfTotals.append(answer)

        # Sum all the totals
        grandTotalCheck = 0
        for total in rowOfTotals:
            grandTotalCheck += total

    print(f"Grand Total Check: {grandTotalCheck}")

except Exception as e:
    print(f"Error reading input file. Error: {e}")