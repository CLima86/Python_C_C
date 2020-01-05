"""
File: dimensions.py
Original Author: C. D. Lima
"""

# In Python a 'tuple' is an immutable object. The difference between a list and
# tuple is the brackets. For a tuple one uses parentheses instead of sqaure brackets.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Now let's try changing the value of the first element of our tuple.
# dimensions[0]= 250
# We get an error w/o even trying to print anything, because we CANNOT
# change the value of the elements of the tuple.

# Although we cannot modify a tuple, we can assign a new value to a variable
# that holds the tuple. See below:

print("Original dimensions: ")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
	print(dimension)