import itertools

try:
    totalButtonPresses = 0
    comboFound = False
    with open('Day 10/Part 1/Day_10_1_input.csv', 'r') as inputFile:
        # Loop through each line in the input file
        while True:
            # Read in the next line from the input file
            fileRecord = inputFile.readline().strip("\n")
            if not fileRecord:
                break
            # Get the light details from the record and create the mask as a binary string 1 = on, 0 = off
            lBracket = fileRecord.find('[')
            rBracket = fileRecord.find(']')
            lightsString = fileRecord[lBracket + 1:rBracket]
            lightMask = ''
            for light in lightsString:
                if light == '#':
                    lightMask = lightMask + '1'
                else:
                    lightMask = lightMask + '0'
            # Get all the button/light combinations from the record and save to an array. Ignore the last substring for the joltages
            buttonLightCombos = fileRecord[rBracket + 2:].split(' ')[:-1]
            # Remove all the parentheses from the button/light combinations
            buttonLightCombos = [s.replace('(', '').replace(')', '') for s in buttonLightCombos]
            allCombosArray = []
            for r in range(1, len(buttonLightCombos) + 1):
                allCombosArray.extend(itertools.combinations(buttonLightCombos, r))

            for buttonCombo in allCombosArray:
                lightStates = '0' * len(lightMask)
                for button in buttonCombo:
                    buttonDetails = button.split(',')
                    for light in buttonDetails:
                        if lightStates[int(light)] == '0':
                            lightStates = lightStates[:int(light)] + '1' + lightStates[int(light) + 1:]
                        else:
                            lightStates = lightStates[:int(light)] + '0' + lightStates[int(light) + 1:]
                    if lightStates == lightMask:
                        totalButtonPresses += len(buttonCombo)
                        comboFound = True
                        break
                if comboFound:
                    comboFound = False
                    break

        print(f"Total button presses: {totalButtonPresses}")

except Exception as e:
    print(f"Error reading input file. Error: {e}")