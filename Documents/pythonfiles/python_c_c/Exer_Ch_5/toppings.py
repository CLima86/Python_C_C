"""
File: toppings.py
Original Author: C. D. Lima
"""

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we're out of " + requested_topping + " right now.")
	else:
		print("Adding " + requested_topping + "." )


print("\nFinished making your pizza!")


# Checking to see if a list is empty:

requested_toppings_again = []

if requested_toppings_again:
	for requested_topping_again in requested_toppings_again:
		print("Adding " + requested_topping_again + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

# On line 22 above, when the name of a list is used in an if statememnt, Python
# returns True if the list contains at least one item in it; an empty list evaluates
# as False. In this case the conditional test has failed becasue there is no items in
# the list and so Python moves on to the next condition.

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
more_requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for more_requested_topping in more_requested_toppings:
	if more_requested_topping in available_toppings:
		print("Adding " + more_requested_topping + ".")
	else:
		print("Sorry, we don't have any " + more_requested_topping + " right now.")

print("\nFinished making your pizza!")