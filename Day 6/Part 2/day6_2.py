try:
    arrayOfNumbers = []
    rowOfSigns= []
    rowOfTotals = []
    rowIndex = 0
    totalCount = 0
    signNumber = 0
    with open('Day 6/Part 2/Day_6_2_input.csv', 'r') as inputFile:
        # Load all the numbers and signs into arrays
        while True:
            fileRecord = inputFile.readline().strip("\n")
            if fileRecord == '':
                break

            if ['+', '*'].__contains__(fileRecord[0]):
                rowOfSigns = fileRecord
                break

            else:
                arrayOfNumbers.append(fileRecord)
        signIndex = 0
        signLocation = 0
        while signIndex < len(rowOfSigns):
            # Get the next equation sign from rowOfSigns
            sign = rowOfSigns[signIndex]
            signLocation = signIndex
            signIndex += 1
            lengthOfNumbersColumn = 0
            while rowOfSigns[signIndex] == ' ':
                lengthOfNumbersColumn += 1
                signIndex += 1
                if signIndex == len(rowOfSigns):
                    lengthOfNumbersColumn += 1
                    break
            signNumber +=1
            equationNumbers = []
            for colIndex in range(lengthOfNumbersColumn):
                equationNumber = ''
                for rowIndex in range(4):
                    equationNumber += arrayOfNumbers[rowIndex][signLocation + colIndex]
                equationNumbers.append(equationNumber)
    
            answer = 0
            if sign == '+':
                for rowIndex in range(len(equationNumbers)):
                    answer += int(equationNumbers[rowIndex])
            elif sign == '*':
                for rowIndex in range(len(equationNumbers)):
                    if answer == 0:
                        answer = int(equationNumbers[rowIndex])
                    else:
                        answer *= int(equationNumbers[rowIndex])

            totalCount += answer
            equation = ''
            for numIndex in range(len(equationNumbers)):
                if numIndex == 0:
                    equation += equationNumbers[numIndex].strip(' ')
                else:
                    equation += f" {sign} {equationNumbers[numIndex].strip(' ')}"
            print(f"{signNumber}: {equation} = {answer}. Total so far: {totalCount}")

    print(f"Grand Total: {totalCount}. Total number of signs processed: {signNumber}. Total number of signs in input: {len(rowOfSigns.replace(' ',''))}")

except Exception as e:
    print(f"Error reading input file. Error: {e}")