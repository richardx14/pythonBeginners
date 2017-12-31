myString = "Richard Holloway"

firstName = myString[0:7]

print(firstName)

lastName = myString[8:-1]

print(lastName)

myString = "King Eric"

print( myString[0:5])

str1 = "Manchester"
str2 = "United"

print( (str1 + " " + str2 +" ")*2 )

count = 0

for letter in myString:
	if(letter=="K"):
		print("Found K")
	count += 1

print("No of chars ",count)

if("E" in myString):
	print("E True")

if("Z" in myString):
	print("Z True")


str3 = "three"

print("Length str3 = ", len(str3))

str3_enumerate = list(enumerate(str3))
print(str3_enumerate)

print("He said \"How do I print quotes?\"") # add \ before special characters

print(r"Use r before quotes to show \ ")
