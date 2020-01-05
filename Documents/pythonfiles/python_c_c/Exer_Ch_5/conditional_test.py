"""
File: conditional_tests.py
Original Author: C. D. Lima
"""

data = 10000

print("Does the variable 'data' == 100000? I predict it to be False." )
print(data == 100000)

y = 'dog'

print("\nIs y == 'dog'? I predict it to be True.")
print(y == 'dog')

# Several conditional tests:

print("\n")

# Tests for strings.
string = 'hello'
print(string == 'hello')
print(string == 'Hello')
print(string.lower() == 'hello')

# Tests for numerical values.

print("\n")

print(1 == 2)
print(1 != 2)
print(3 < 5)
print(4 >= 1)
num = 1
print(num >= 5)

# Using the and/or operators.

print("\n")

if num >= 1 and num <= 10:
	print("Your number lies between the interval [1, 10].")
else:
	print("Your number falls outside of the required interval [1, 10]. Try again.")

print("\n")

if num > 5 or num not in range(1, 5):
	print("Your number must be smaller. Try another number.")
else:
	print("Great, your number is between the interval [1, 5]")

# Testing for whether an element in a list, or not.

print("\n")

word_list = ['hi', 'lo', 'yes', 'no']

word = 'maybe'
word_list.append(word)
if word not in word_list:
	print("The word " + word.title() + ", is not in your list.")
else:
	print("The word " + word.title() + ", is in your list.")
