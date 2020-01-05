"""
File: cars_2.py
Original Author: C. D. Lima
"""

# Working with conditional statements in this chapter.

cars = ['nissan', 'toyota', 'subaru', 'tesla']

for car in cars:
	if car == 'toyota':
		print(car.upper())
	else:
		print(car.title())


# Checking for equality #
# There is a difference between = and ==. Namely, = sets a value to a variable. 
# And == is chekcing to see if the variable has the value you have on the RHS.
# In Python checking for equality is case sensitive n strings.

print("\n")

# Ex:

car = 'bmw'
print(car == 'bmw')

car = 'Audi'
print(car == 'audi')

# But we can check without case sensitivity if the value is the same as follows:

car.lower() == 'audi'