import copy

def Evil_Function(toBeModified):
    toBeModified[0][0] = 20
    print(toBeModified)

myList = [[1, 7], [3, 8], [52, 13]]

Evil_Function(copy.deepcopy(myList))

print(myList)
