def parseLists(lst):
    for elementti in lst:
        if isinstance(elementti, list): 
            parseLists(elementti)       
        else:
            print(elementti)           


listOfLists = [1, [2, 3], 4, 5, [6, 7, [8, 9]], 0]
parseLists(listOfLists)