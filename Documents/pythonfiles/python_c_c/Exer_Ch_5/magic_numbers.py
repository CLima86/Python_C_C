"""
File: magic_numbers.py (This file also contains exercises apart from "magic_numbers")
Original Author: C. D. Lima
"""
answer = 17
if answer != 4:
	print("That is not hte correct answer. Please try again!")

""" The following is the "banned_users.py" example. """

# Checking whether a value is in a list or not.
# To do this we use the keyword 'not' to check if a value does not appear in a list.

print("\n")

banned_users = ['andrew', 'carolina', 'david']
user ='marie'

if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")

