def turnDial(currentLocation, distance, direction):
    if direction == 'L':
        if currentLocation - distance >= 0:
            newLocation = currentLocation - distance
        else:
            newLocation = 99 - (distance - currentLocation - 1)
    elif direction == 'R':
        if currentLocation + distance <= 99:
            newLocation = currentLocation + distance
        else:
            newLocation = (currentLocation + distance) - 100
    return newLocation

try:
    location = 50
    countOfZeroes = 0
    countofSteps = 0
    print(f"Starting Location: {location}")
    with open('Day 1/Day 1 input.csv', 'r') as inputFile:
        for line in inputFile:
            
            direction = line[0]
            distance = int(line[1:len(line)-1])
            if distance >= 100:
                distance = distance % 100
            # if distance == 21:
            #     print("Paused")
            if direction == 'L':
                newLocation = turnDial(location, distance, 'L')
                if isinstance(newLocation, int):
                    location = newLocation
            elif direction == 'R':
                newLocation = turnDial(location, distance, 'R')
                if isinstance(newLocation, int):
                    location = newLocation
            else:
                print("Invalid direction in input file")
                break
            print(f"{countofSteps}: Direction: {direction}, Distance: {distance}, New Location: {newLocation}")
            if location == 0:
                countOfZeroes += 1
            countofSteps += 1
    print(f"Final Location: {location}")
    print(f"Number of times dial returned to 0: {countOfZeroes}")
    print(f"Total number of steps from input file: {countofSteps}")
                
except Exception as e:
    print(f"Error reading input file. Error: {e}")