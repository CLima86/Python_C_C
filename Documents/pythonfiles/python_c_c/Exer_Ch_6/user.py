"""
File: user.py
Original Author: C. D. Lima
"""

# Looping Through a Dictionary #

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi'
	}

for key, value in user_0.items():
	print("\nKey: " + key)
	print("\nValue: " + value)

# The .items() method returns a list of key-value pairs. The for-loop that follows
# then stores each key-value pair in the two variables you choose to use.

