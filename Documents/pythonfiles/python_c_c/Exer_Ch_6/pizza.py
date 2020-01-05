"""
File: pizza.py
Original Author: C. D. Lima
"""

# Store information about a pizza being ordered.

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese']
	}

# Summarize the order
print("Your " + pizza['crust'] + "-crust pie comes with the follwing toppings: ")

for topping in pizza['toppings']:
	print("\t" + topping.title())