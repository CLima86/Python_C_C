"""
File: rollercoaster.py (also contains 'even_or_odd.py')
Original Author: C. D. Lima
"""

height = input("Hoew tall are you, in inches? ")
height = int(height)

if height >= 36:
	print("You are tall enough to ride!")
else:
	print("You'll be able to ride when you're a little older.")


## even_or_odd.py ##

number = input("Enter a number, an I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print(str(number) + " is even!")
else:
	print(str(number) + " is odd!")