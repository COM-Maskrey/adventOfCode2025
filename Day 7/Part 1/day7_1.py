try:
    beamLocations = []
    newBeamLocations = []
    beamSplits = 0
    rowIndex = -1
    with open('Day 7/Part 1/Day_7_1_input.csv', 'r') as inputFile:
        while True:
            fileRecord = inputFile.readline().strip("\n")
            if not fileRecord:
                break
            rowIndex += 1
            if rowIndex == 0:
                for index in range(len(fileRecord)):
                    if fileRecord[index] == 'S':
                        beamLocations.append(index)
                        break
            else:
                newBeamLocations = []
                for beamIndex in range(len(beamLocations)):
                    if fileRecord[beamLocations[beamIndex]] == '.':
                        # Beam continues straight down
                        continue
                    elif fileRecord[beamLocations[beamIndex]] == '^':
                        newBeamLocations.append(beamLocations[beamIndex] - 1)
                        newBeamLocations.append(beamLocations[beamIndex] + 1)
                        beamSplits += 1
                        beamLocations[beamIndex] = 'X'    # Mark this beam to be removed
                if newBeamLocations != []:
                    beamLocations = [beam for beam in beamLocations if beam != 'X'] # Remove marked beams
                    beamLocations.extend(newBeamLocations) # Add the new beam locations
                    beamLocations.sort() # Sort the beam locations for easier tracking
                    # Mark duplicates for deletion
                    for index in range(len(beamLocations)):
                        if index != 0:
                            if beamLocations[index] == beamLocations[index - 1]:
                                beamLocations[index - 1] = 'X'
                    # Remove duplicates
                    beamLocations = [beam for beam in beamLocations if beam != 'X'] # Remove marked beams
            print(f"After Row {rowIndex+1}: Beam Splits: {beamSplits}")
    print(f"Total Splits: {beamSplits}")

except Exception as e:
    print(f"Error reading input file. Error: {e}")