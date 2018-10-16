def printName(nameList):
    for name in nameList:
        print name

def makeGreat(nameList):
    for i in range(len(nameList)):
        nameList[i] = 'my name is ' + nameList[i]
    printName(nameList)

list1 = ['a', 'b', 'c', 'd']
makeGreat(list1[:])
printName(list1)
