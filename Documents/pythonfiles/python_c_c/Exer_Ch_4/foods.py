"""
File: foods.py
Original Author: C. D. Lima
"""

# Copying a List #

# One can copy an entire list to a new variable by just using the slicing method w/o
# indicating an index to range from. And they are two seperate lists!!
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)
print("\nMy friends favorite foods are: ")
print(friend_foods)

# To show that they are two seperate lists we will add a different foods to each list seperately.
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are: ")
print(my_foods)
print("\nMy friends favorite foods are: ")
print(friend_foods)
