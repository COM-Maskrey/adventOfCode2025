try:
    sumOfJoltage = 0
    inputLineNum = 1
    with open('Day 3/Part 2/Day_3_2_input.csv', 'r') as inputLine:
        firstPass = True
        for batteryBank in inputLine:
            batteryBank = batteryBank.strip("\n")

            optBattery = [0] * 12
            # 1 - Fill the slots with first 12 joltages
            for idx in range(12):
                optBattery[idx] = batteryBank[idx]
            # 2 - Check remaining joltages in the bank
            for idx in range(12, len(batteryBank)):
                # print(f"{inputLineNum} - Current batteries are: {''.join(optBattery)}. Next battery is: {batteryBank[idx]}")
                # 3 - Loop through current optimal battery list and compare adjacent joltages
                for jdx in range(11):
                    if optBattery[jdx] < optBattery[jdx + 1]:
                     # 4 - If the next joltage is higher than the current joltage then shuffle all the next joltages up one slot
                        for kdx in range(jdx, 11):
                            optBattery[kdx] = optBattery[kdx + 1]
                        optBattery[11] = batteryBank[idx]
                        break
                # 5 - After checking all adjacent joltages, check if the new joltage is higher than the last optimal joltage
                if batteryBank[idx] > optBattery[11]:
                    optBattery[11] = batteryBank[idx]
            optBatteryInt = int(''.join(optBattery))
            print(f"{inputLineNum} - Optimal batteries are: {optBatteryInt}")
            sumOfJoltage += optBatteryInt
            inputLineNum += 1
    print(f"Sum of joltage: {sumOfJoltage}")

except Exception as e:
    print(f"Error reading input file. Error: {e}")