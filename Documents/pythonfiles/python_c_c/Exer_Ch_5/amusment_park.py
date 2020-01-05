"""
File: amusment_park.py (This file will contain a number of other examples from this chapter)
Original Author: C. D. Lima
"""

age = 45
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5

print("Your admission is $" + str(price) + ".")