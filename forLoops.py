print("End only\n")

for i in range(10):
	print(i)

print("Start stop\n")

for i in range(5,10):
	print(i)

print("Start, stop, end\n")

for i in range(0,10,2):
	print(i)

print("Going backwards\n")

for i in range (100,90,-1):
	print(i)

print("iterating through a list")

classOf92 = ["Beckham", "Giggs", "G Neville", "P Neville", "Butt", "Scholes"]

for player in classOf92:
	print(player)

print("build a list from scratch")

integers= []

for i in range(10):
	integers.append(i)

print(integers)

print("Looping through a string")

alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in alphabet:
	print(letter)

print("Looping through a dictionary")

wasps = { "14":"Daly", "2":"Johnson", "4":"Launchbury", "10":"Cipriani", "9":"Robson"}

for key in wasps:
	print("No " + key + " " + wasps[key] )

print("Nested loop")

for a in range(10):
	print("Loop", a)
	for b in range(5):
		print( a*b)


