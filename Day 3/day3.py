try:
    sumOfJoltage = 0
    with open('Day 3/Day_3_input.csv', 'r') as inputLine:
        for battery in inputLine:
            battery = battery.strip("\n")
            firstBattery = 0
            secondBattery = 0
            for joltage in battery:
                joltage = int(joltage)
                if secondBattery > firstBattery:
                    firstBattery = secondBattery
                    secondBattery = joltage
                else:
                    if joltage > secondBattery:
                        secondBattery = joltage
            sumOfJoltage += (firstBattery * 10) + secondBattery

    print(f"Sum of joltage: {sumOfJoltage}")

except Exception as e:
    print(f"Error reading input file. Error: {e}")