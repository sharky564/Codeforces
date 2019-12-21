# Registration System
a = int(input())
entered_usernames = [input() for i in range(a)]
database = {}
for username in entered_usernames:
	if username in database:
		print(username + str(database[username]))
		database[username] += 1
	else:
		print("OK")
		database[username] = 1
