from shapely.geometry import Point, Polygon, box

try:

    redTilesArray = []
    rectangleSizesArray = []
    # Use test input if available, else real input
    import os
    test_input = 'Day 9/Part 2/Day_9_2T_Input.csv'
    real_input = 'Day 9/Part 2/Day_9_2_input.csv'
    input_file = test_input if os.path.exists(test_input) else real_input
    with open(input_file, 'r') as inputFile:
        for fileRecord in inputFile:
            fileRecord = fileRecord.strip("\n")
            if fileRecord:
                redTilesArray.append([int(x) for x in fileRecord.split(',')])

    # The polygon boundary is the ordered list of red tiles
    polygon = Polygon(redTilesArray)

    # Bounding box (if needed)
    xs = [tile[0] for tile in allTilesArray]
    ys = [tile[1] for tile in allTilesArray]
    xMin, xMax = min(xs) - 1, max(xs) + 1
    yMin, yMax = min(ys) - 1, max(ys) + 1



    # Find all possible rectangles and add to array
    for i, tile1 in enumerate(redTilesArray):
        print(f"Processing tile {i + 1} of {len(redTilesArray)}")
        for j in range(i + 1, len(redTilesArray)):
            tile2 = redTilesArray[j]
            min_x, max_x = min(tile1[0], tile2[0]), max(tile1[0], tile2[0])
            min_y, max_y = min(tile1[1], tile2[1]), max(tile1[1], tile2[1])
            area = (max_x - min_x + 1) * (max_y - min_y + 1)
            rectangleSizesArray.append([i, j, min_x, min_y, max_x, max_y, area])

    # Sort rectangles by area descending
    rectangleSizesArray.sort(key=lambda x: -x[6])

    # Check for the first rectangle whose four corners and all points inside are within or on the edge of the polygon
    biggest_rectangle = None
    for rect in rectangleSizesArray:
        min_x, min_y, max_x, max_y = rect[2], rect[3], rect[4], rect[5]
        corners = [
            Point(min_x, min_y),
            Point(min_x, max_y),
            Point(max_x, min_y),
            Point(max_x, max_y)
        ]
        if all(polygon.covers(corner) for corner in corners):
            # Check all points within the rectangle
            all_inside = True
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    pt = Point(x, y)
                    if not polygon.covers(pt):
                        all_inside = False
                        break
                if not all_inside:
                    break
            if all_inside:
                biggest_rectangle = rect
                break

    if biggest_rectangle:
        print(f"Biggest rectangle is: area={biggest_rectangle[6]}, corners=({biggest_rectangle[2]}, {biggest_rectangle[3]}) to ({biggest_rectangle[4]}, {biggest_rectangle[5]})")
    else:
        print("No valid rectangles found.")

except Exception as e:
    print(f"Error reading input file. Error: {e}")