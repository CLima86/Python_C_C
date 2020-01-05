"""
File: slices.py
Original Author: C. D. Lima
"""
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print("The first three items in the list are: ")
print(my_foods[:3])

print("\nThe middle three items in the list are:")
print(my_foods[1:4])

print("\nThe last three items in the list are:")
print(my_foods[2:])


# Pizza Slicing #

pizzas = ['cheese', 'veggie', 'pepperoni']
friend_pizzas = pizzas[:]
pizzas.append('meat lovers')
friend_pizzas.append('vegan')

print("\nMy favorite pizzas are: ")
for pizza in pizzas:
	print(pizza.title())

print("\nMy friends favorite pizzas are: ")
for friends_pizza in friend_pizzas:
	print(friends_pizza.title())