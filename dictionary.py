myDict = {'name':'Richard', 'age':21, 'yob':1969}
print(myDict)

myDict2 = {"name":'Richard', 'age':21, 'yob':1969}
print(myDict2)

print(myDict['age'])

print(myDict.keys())

for key in myDict.keys():
	print(myDict[key])

for key in myDict.keys():
	print(key)

print(myDict.values() )

for value in myDict.values():
	print(value)

print(myDict.items())

for key, value in myDict.items():
	print("key is ", key, "value is ", value)

# adding an item to dictionary

myDict["address"] = "21 Priory Avenue"

print(myDict)


myDict["address"] = "21 Priory Avenue, High Wycombe"

print(myDict["address"])

myDict.update({"email":"richard@iosolar.co.uk"})

print(myDict)

myDict.update({"email":"richard@blueharvest.co.uk"})

print(myDict)

myDict["email"] = "richardx14@icloud.com"

print(myDict)

del myDict["email"]

print(myDict)
