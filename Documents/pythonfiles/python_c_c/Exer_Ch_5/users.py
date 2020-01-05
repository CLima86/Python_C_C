"""
File: users.py
Original Author: C. D. Lima
"""

users = ['carlos', 'natalia', 'luis', 'jessica', 'camila', 'ricky', 'victor', 'maribel', 'francine', 'admin']

if users:
	for user in users:
		if user == 'admin':
			print("Hello " + user + ", would you like to see a status report?")
		else:
			print("Hello " + user.title() + ", thank you for loging in again.")
else:
	print("We need to find some users!!")

print("\n")
print("\n")

current_users = ['camila', 'ricky', 'victor', 'maribel', 'francine', 'John']
new_users = ['carlos', 'natalia', 'luis', 'jessica', 'elia', 'JOHN']

for new_user in new_users:
	if new_user.title() in current_users:
		print("Sorry, the user name " + new_user.title() + " is already taken.")
	else:
		print(new_user.title() + " is available to use as a user name.")