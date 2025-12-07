try:
    sumOfInvalids = 0
    countofInvalids = 0
    with open('Day 2/Part 2/Day_2_2_input.csv', 'r') as inputLine:
        for line in inputLine:
            ranges = line.split(",")
            for range in ranges:
                print(f"Processing range: {range}")
                values = range.split("-")
                if len(values) != 2:
                    print("Invalid range in input file")
                    break
                start = int(values[0])
                end = int(values[1])
                if start > end:
                    print("Invalid range in input file: start is greater than end")
                    break
                value = start
                while value <= end:
                    strLength = len(str(value))
                    if strLength < 2:
                        value += 1
                        continue
                    strValue = str(value)
                    # First check for a double repeat e.g. 1212, 123123, 12341234, etc.
                    if strLength % 2 == 0:
                        if strValue[0:(strLength // 2)] == strValue[strLength // 2:]:
                            print(f"Invalid value found: {strValue}")
                            sumOfInvalids += value
                            countofInvalids += 1
                            value += 1
                            continue
                    # Check for an all digit repeat e.g. 11111, 222, etc.
                    allSame = True
                    for char in strValue:
                        if char != strValue[0]:
                            allSame = False
                            break
                    if allSame:
                        print(f"Invalid value found: {strValue}")
                        sumOfInvalids += value
                        countofInvalids += 1
                        value += 1
                        continue
                    # Check for repeating patterns e.g. 121212, 123123, 12341234, etc.
                    patternLength = 2
                    while strLength // patternLength >= 2:
                        if strLength % patternLength == 0:
                            patternValue = strValue[0:patternLength]
                            repeats = strLength // patternLength
                            count = 1
                            patternFound = True
                            while count < repeats:
                                if patternValue != strValue[patternLength * count:(patternLength * count) + patternLength]:
                                    patternLength += 1
                                    patternFound = False
                                    break
                                count += 1
                            if patternFound:
                                print(f"Invalid value found: {strValue}")
                                sumOfInvalids += value
                                countofInvalids += 1
                                break
                        patternLength += 1
                    value += 1

    print(f"Sum of invalid values: {sumOfInvalids}")
    print(f"Count of invalid values: {countofInvalids}")

except Exception as e:
    print(f"Error reading input file. Error: {e}")