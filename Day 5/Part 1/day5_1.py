try:
    countOfFreshIngredients = 0
    freshIngredientsRanges = []

    with open('Day 5/Part 1/Day_5_1_input.csv', 'r') as inputFile:
        # Load all the ranges into an array
        while True:
            fileRecord = inputFile.readline().strip("\n")
            if fileRecord == '':
                break
            freshIngredientsRange = fileRecord.split('-')
            freshIngredientsRanges.append([int(x) for x in freshIngredientsRange])
        
        # Get each ingredient and test against the ranges
        while True:
            fileRecord = inputFile.readline().strip("\n")
            if fileRecord == '':
                break
            ingredientToTest = int(fileRecord)
            for idx in range(len(freshIngredientsRanges)):
                if freshIngredientsRanges[idx][0] <= ingredientToTest <= freshIngredientsRanges[idx][1]:
                    countOfFreshIngredients += 1
                    break
            
    print(f"Count of Fresh Ingredients: {countOfFreshIngredients}")

except Exception as e:
    print(f"Error reading input file. Error: {e}")