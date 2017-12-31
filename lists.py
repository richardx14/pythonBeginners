myList = []
print(myList)

myList=[1,2,3]
print(myList)
print(myList[1])

myList=["richard",1969,"Sept"]
print(myList)
print(myList[2])
print(myList[-3])
myList[0]="holloway"
print(myList)
myList.append("richard")
print(myList)

myList=[[1,2,3],[4,5,6],[7,8,9]]
print(myList)
print(myList[1][2])

myList=[0,1,2,3,4,5,6,7,8,9]
print(myList[0:2])

myList.extend([10,11,12])
print(myList)

myOtherList = [13,14,15]

myCombinedList = myList + myOtherList

print(myCombinedList)

myCombinedList.insert(7,"X")
print(myCombinedList)

myList = ["yeah " * 3]
print(myList)

myList.insert(2,"no ")

print(myList)

emptyList = []
#emptyList.insert(0,[1,2,3])
print(emptyList)

popDelRemove = [10,20,30,40,50]
print(popDelRemove)

popDelRemove.remove(20)
print(popDelRemove)

del popDelRemove[3]
print(popDelRemove)

popVar=popDelRemove.pop(1)
print(popVar)

print(popDelRemove)

fullList = ["a","ab", "ABC"]
print(fullList)

fullList.clear()
print(fullList)

compList = [ x*3 for x in range(10)]
print(compList)

compList = [ x*2 for x in range(5) if x != 3 ]
print(compList)

compList = [ x-y for x in range(10) for y in range(5)]
print(compList)


