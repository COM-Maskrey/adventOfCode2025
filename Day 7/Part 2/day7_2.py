try:
    beamLocations = []
    newBeamLocations = []
    beamCounts = 0
    rowIndex = -1
    with open('Day 7/Part 2/Day_7_2_input.csv', 'r') as inputFile:
        while True:
            fileRecord = inputFile.readline().strip("\n")
            if not fileRecord:
                break
            rowIndex += 1
            if rowIndex == 0:
                for index in range(len(fileRecord)):
                    if fileRecord[index] == 'S':
                        beamLocations.append([index, 1])
                        break
            else:
                newBeamLocations = []
                for beamIndex in range(len(beamLocations)):
                    if fileRecord[beamLocations[beamIndex][0]] == '.':
                        continue
                    elif fileRecord[beamLocations[beamIndex][0]] == '^':
                        newBeamLocations.append([beamLocations[beamIndex][0] - 1, beamLocations[beamIndex][1]])
                        newBeamLocations.append([beamLocations[beamIndex][0] + 1, beamLocations[beamIndex][1]])
                        beamLocations[beamIndex] = 'X'    # Mark this beam to be removed
                if newBeamLocations != []:
                    beamLocations = [beam for beam in beamLocations if beam != 'X'] # Remove marked beams
                    beamLocations.extend(newBeamLocations) # Add the new beam locations
                    beamLocations.sort() # Sort the beam locations for easier tracking
                    # Identify duplicates and sum them
                    for index in range(len(beamLocations)):
                        if index != 0:
                            if beamLocations[index][0] == beamLocations[index - 1][0]:
                                beamLocations[index][1] += beamLocations[index - 1][1]
                                beamLocations[index - 1][0] = 'X'
                    # Remove duplicates
                    beamLocations = [beam for beam in beamLocations if beam[0] != 'X'] # Remove marked beams
                    beamCounts = 0
                    for index in range(len(beamLocations)):
                        beamCounts += beamLocations[index][1]
            print(f"After Row {rowIndex+1}: Beam Counts = {beamCounts}")
    print(f"Total Beam Counts: {beamCounts}")

except Exception as e:
    print(f"Error reading input file. Error: {e}")