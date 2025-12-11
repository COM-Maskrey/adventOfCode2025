try:
    tilesArray = []
    nextCircuitID = 1
    with open('Day 9/Part 1/Day_9_1_input.csv', 'r') as inputFile:
        # Load all the tile locations into an array
        while True:
            fileRecord = inputFile.readline().strip("\n")
            if not fileRecord:
                break
            tilesArray.append([int(x) for x in fileRecord.split(',')])
        # Loop through each tile location and calculate the size of a rectangle to all other tile locations
        rectangleSizesArray = []
        for index, tile in enumerate(tilesArray):
            for index2, tile2 in enumerate(tilesArray):
                if index2 > index:
                    length = abs(tile[0] - tile2[0]) + 1
                    width = abs(tile[1] - tile2[1]) + 1
                    rectangleSizesArray.append([index, index2, length * width])
        rectangleSizesArray.sort(key=lambda x: -x[2])

    print(f"Biggest rectangle is: {rectangleSizesArray[0][2]}.")

except Exception as e:
    print(f"Error reading input file. Error: {e}")