from cmath import sqrt
MAX_CONNECTIONS = 10000
countConnections = 0
try:
    junctionBoxesArray = []
    nextCircuitID = 1
    with open('Day 8/Part 2/Day_8_2_input.csv', 'r') as inputFile:
        # Load all the junction box locations into an array and add extra fields for CircuitID and CountInCircuit
        # [X, Y, Z, CircuitID, CountInCircuit]
        while True:
            fileRecord = inputFile.readline().strip("\n")
            if not fileRecord:
                break
            junctionBoxesArray.append([int(x) for x in fileRecord.split(',')] + [0,0])
        # Loop through each junction box and calculate the distances to all other junction boxes
        distancesArray = []
        for index, row in enumerate(junctionBoxesArray):
            for index2, row2 in enumerate(junctionBoxesArray):
                if index2 > index:
                    distance = round(sqrt(((row[0] - row2[0]) ** 2) + ((row[1] - row2[1]) ** 2) + ((row[2] - row2[2]) ** 2)).real, 5)
                    distancesArray.append([index, index2, distance])
        # Sort the distances array by distance ascending
        distancesArray.sort(key=lambda x: x[2])

        # Loop through the distances array to connect those junction boxes, until the max number of connections is reached
        for distanceRecord in distancesArray:
            if countConnections >= MAX_CONNECTIONS:
                break
            else:
                countConnections += 1
                if junctionBoxesArray[distanceRecord[0]][3] == 0 and junctionBoxesArray[distanceRecord[1]][3] == 0:
                    # Neither junction box is in a circuit, so create a new circuit for both
                    junctionBoxesArray[distanceRecord[0]][3] = nextCircuitID
                    junctionBoxesArray[distanceRecord[0]][4] = 2
                    junctionBoxesArray[distanceRecord[1]][3] = nextCircuitID
                    junctionBoxesArray[distanceRecord[1]][4] = 2
                    nextCircuitID += 1
                elif junctionBoxesArray[distanceRecord[1]][3] == 0:
                    # First junction box is in a circuit, but the second is not, so add the second to the first's circuit
                    circuitIDToKeep = junctionBoxesArray[distanceRecord[0]][3]
                    junctionBoxesArray[distanceRecord[1]][3] = circuitIDToKeep
                    junctionBoxesArray[distanceRecord[1]][4] = junctionBoxesArray[distanceRecord[0]][4]
                    for row in junctionBoxesArray:
                        if row[3] == circuitIDToKeep:
                            row[4] += 1
                elif junctionBoxesArray[distanceRecord[0]][3] == 0:
                    # Second junction box is in a circuit, but the first is not, so add the first to the second's circuit
                    circuitIDToKeep = junctionBoxesArray[distanceRecord[1]][3]
                    junctionBoxesArray[distanceRecord[0]][3] = circuitIDToKeep
                    junctionBoxesArray[distanceRecord[0]][4] = junctionBoxesArray[distanceRecord[1]][4]
                    for row in junctionBoxesArray:
                        if row[3] == circuitIDToKeep:
                            row[4] += 1
                elif junctionBoxesArray[distanceRecord[0]][3] != 0 and junctionBoxesArray[distanceRecord[1]][3] != 0:
                    # Both junction boxes are already in circuits so combine the circuits if they are different
                    if junctionBoxesArray[distanceRecord[0]][3] != junctionBoxesArray[distanceRecord[1]][3]:
                        circuitIDToKeep = junctionBoxesArray[distanceRecord[0]][3]
                        circuitIDToChange = junctionBoxesArray[distanceRecord[1]][3]
                        sizeOfCombinedCircuits = junctionBoxesArray[distanceRecord[0]][4] + junctionBoxesArray[distanceRecord[1]][4]
                        for row in junctionBoxesArray:
                            if row[3] == circuitIDToChange:
                                row[3] = circuitIDToKeep
                                row[4] = sizeOfCombinedCircuits
                            elif row[3] == circuitIDToKeep:
                                row[4] = sizeOfCombinedCircuits
                else:
                    continue
                print(f"Connection {countConnections} : {junctionBoxesArray[distanceRecord[0]][0:3]} to {junctionBoxesArray[distanceRecord[1]][0:3]}. Distance = {distanceRecord[2]}.")
            if countConnections > len(junctionBoxesArray):
                # Once the number of connections exceeds the number of junction boxes, we can then start to test if we have created one full circuit
                # Before then, it's impossible to have a full circuit
                firstCircuitID = junctionBoxesArray[0][3]
                allInOneCircuit = True
                for row in junctionBoxesArray:
                    if row[3] != firstCircuitID:
                        allInOneCircuit = False
                        break
                if allInOneCircuit:
                    break

    answer = junctionBoxesArray[distanceRecord[0]][0] * junctionBoxesArray[distanceRecord[1]][0]
    print(f"Answer: {answer}.")

except Exception as e:
    print(f"Error reading input file. Error: {e}")