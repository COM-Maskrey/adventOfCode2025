try:
    sumOfInvalids = 0
    with open('Day 2/Day_2_input.csv', 'r') as inputLine:
        for line in inputLine:
            ranges = line.split(",")
            for range in ranges:
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
                    strValue = str(value)
                    if strLength % 2 == 0:
                        if strValue[0:(strLength // 2)] == strValue[strLength // 2:]:
                            print(f"Invalid value found: {strValue}")
                            sumOfInvalids += value
                    value += 1
    print(f"Sum of invalid values: {sumOfInvalids}")

except Exception as e:
    print(f"Error reading input file. Error: {e}")