import random

# generate a random number

number = random.randint(1,10)

# init guess

guess = "-1"

tries = 0

# while guess != number, get guess

while ( int(guess) != number ) :

	tries = tries + 1
	print("Try no", tries)

	print("Enter guess:")
	guess = input()

	if (int(guess) == number):
		print("Correct!")
		break
	else:
		if (int(guess) > number):
			print("Lower")
		else:
			print("Higher")


