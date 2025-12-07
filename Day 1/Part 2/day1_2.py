def turnDial(currentLocation, distance, direction):
    numZeroes = 0
    if direction == 'L':
        if currentLocation - distance >= 0:
            newLocation = currentLocation - distance
        else:
            newLocation = 99 - (distance - currentLocation - 1)
            if currentLocation != 0:
                numZeroes = 1
    elif direction == 'R':
        if currentLocation + distance <= 99:
            newLocation = currentLocation + distance
        else:
            newLocation = (currentLocation + distance) - 100
            if currentLocation != 0:
                numZeroes = 1
    if newLocation == 0:
        numZeroes =0
    return newLocation, numZeroes

try:
    location = 50
    countOfZeroes = 0
    countofSteps = 1
    rotations = 0
    print(f"Starting Location: {location}")
    with open('Day 1/Part 2/Day_1_2_input.csv', 'r') as inputFile:
        for line in inputFile:
            
            direction = line[0]
            fullDistance = int(line[1:len(line)])
            if fullDistance >= 100:
                rotations = fullDistance // 100
                distance = fullDistance % 100
            else:
                distance = fullDistance
            if direction == 'L':
                newLocation, numZeroes = turnDial(location, distance, 'L')
                if isinstance(newLocation, int):
                    location = newLocation
            elif direction == 'R':
                newLocation, numZeroes = turnDial(location, distance, 'R')
                if isinstance(newLocation, int):
                    location = newLocation
            else:
                print("Invalid direction in input file")
                break
            if location == 0:
                countOfZeroes += 1
            countOfZeroes = countOfZeroes + rotations + numZeroes
            print(f"{countofSteps}: {direction}{fullDistance}, Rotations: {rotations}, Num Zeroes: {numZeroes}, Location: {location}, Count of Zeroes: {countOfZeroes}")
            rotations = 0
            countofSteps += 1
            if countofSteps == 4387:
                print("Breakpoint")
    print(f"Final Location: {location}")
    print(f"Number of times dial touches 0: {countOfZeroes}")
    print(f"Total number of steps from input file: {countofSteps}")
                
except Exception as e:
    print(f"Error reading input file. Error: {e}")