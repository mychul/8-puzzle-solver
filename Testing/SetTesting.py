import copy
mySet={}
myList = [[1,2,3],[4,5,6],[7,8,0]]
flatList=[]
for r in myList:
    for c in r:
        flatList.append(c)
mySet = {tuple(flatList)}
duplicate = copy.deepcopy(flatList)
mySet.add(tuple(duplicate))
if tuple(duplicate) in mySet:
    print("Happy")
print (mySet)