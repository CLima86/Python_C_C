"""
File: even_numbers.py
Original Author: C. D. Lima
"""
numbers = list(range(1, 6))
print(numbers)

# Let's generate a list of even numbers using the range function.
# We do this adding a parameter to the argument, namely, in the range
# generate only every other number.

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# If we started the list of at one, it would print out odd numbers...
odd_numbers = list(range(1, 11, 2))
print(odd_numbers)

