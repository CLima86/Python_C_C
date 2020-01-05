"""
File: rental_car.py
Original Author: C. D. Lima
"""

car_type = input("What kind of car are you looking to rent? ")
print("Let me see if I can find you a " + car_type.title() + "...")


# multiples of 10...

number = input("Give me a number: ")
number = int(number)

if number % 10 == 0:
	print("\nThe number " + str(number) + " is a multiple of 10!")
else:
	print("\nThe number " + str(number) + " is not a multiple of 10.")