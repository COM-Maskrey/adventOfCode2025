try:
    freshIngredientsRanges = []
    uniqueIngredientRanges = []
    countOfFreshIngredients = 0
    with open('Day 5/Part 2/Day_5_2_input.csv', 'r') as inputFile:
        # Load all the ranges into an array
        while True:
            fileRecord = inputFile.readline().strip("\n")
            if fileRecord == '':
                break
            freshIngredientsRange = fileRecord.split('-')
            freshIngredientsRanges.append([int(x) for x in freshIngredientsRange])
        index = -1
        while index < len(freshIngredientsRanges) - 1:
            index += 1
            startRange = freshIngredientsRanges[index][0]
            endRange = freshIngredientsRanges[index][1]
            uniqueRange = True
            for uniqueIndex in range(len(uniqueIngredientRanges)):
                # 1 - Range is all less than the current unique range - keep checking
                if endRange < uniqueIngredientRanges[uniqueIndex][0]:
                    continue
                # 2 - Range is all greater than the current unique range - keep checking
                elif startRange > uniqueIngredientRanges[uniqueIndex][1]:
                    continue
                # 3 - Range is all within the current unique range - stop checking no need to add
                elif startRange >= uniqueIngredientRanges[uniqueIndex][0] and endRange <= uniqueIngredientRanges[uniqueIndex][1]:
                    uniqueRange = False
                    break
                # 4 - Range overlaps all of the current unique range - split the range, add the second half to the list to be checked and carry on checking the first half
                elif startRange < uniqueIngredientRanges[uniqueIndex][0] and endRange > uniqueIngredientRanges[uniqueIndex][1]:
                    # Add second half to the list to be checked
                    freshIngredientsRanges.append([uniqueIngredientRanges[uniqueIndex][1] + 1, endRange])
                    # Adjust endRange to check the first half
                    endRange = uniqueIngredientRanges[uniqueIndex][0] - 1
                    continue
                # 5 - Range overlaps the start of the current unique range - adjust the endRange and keep checking
                elif startRange < uniqueIngredientRanges[uniqueIndex][0] and endRange >= uniqueIngredientRanges[uniqueIndex][0] and endRange <= uniqueIngredientRanges[uniqueIndex][1]:
                    endRange = uniqueIngredientRanges[uniqueIndex][0] - 1
                    continue
                # 6 - Range overlaps the end of the current unique range - adjust the startRange and keep checking
                elif startRange >= uniqueIngredientRanges[uniqueIndex][0] and startRange <= uniqueIngredientRanges[uniqueIndex][1] and endRange > uniqueIngredientRanges[uniqueIndex][1]:
                    startRange = uniqueIngredientRanges[uniqueIndex][1] + 1
                    continue
                # If there is any range left to check then it's a unique range - add it to the list    
            if uniqueRange:
                uniqueIngredientRanges.append([startRange, endRange])
                countOfFreshIngredients += (endRange - startRange + 1)
            
    uniqueIngredientRanges.sort()
    print(f"Count of Fresh Ingredients: {countOfFreshIngredients}")

except Exception as e:
    print(f"Error reading input file. Error: {e}")