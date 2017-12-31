usernames = {}

while True:
	print(usernames) 
	print("Enter username:")

	username = input()

	if username in usernames.keys():
		print(username + " is the username of " + usernames[username])

	else:
		print("Enter name:")
		name = input()
		usernames[username] = name
		print(usernames[username])

  
