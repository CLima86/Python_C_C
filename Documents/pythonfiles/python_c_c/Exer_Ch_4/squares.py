"""
File: squares.py
Original Author: C. D. Lima
"""

squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)

print(squares)

# We can perform simple statistics with the elements in a list. For example,
# we can look at the max value, min value, and the sum of the elements.

print(sum(squares))

# Another option of writing out a simple for loop is a 'list comprehension'.

squares2 = [i ** 2 for i in range(1, 20)]
print(squares2)