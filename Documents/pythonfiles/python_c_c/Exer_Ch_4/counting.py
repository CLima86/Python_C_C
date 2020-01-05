"""
File: counting.py
Original Author: C. D. Lima
"""

for value in range(1, 21):
	print(value)

print("\n")

# List of numbers from 1 to 1,000,000

million = list(range(1, 1000001))
#for number in million:
#	print(number)

sum_mill = sum(million)
print(sum_mill)
print(min(million), max(million))

print("\n")

odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

print("\n")

# Printing numbers divisible by 3
threes = list(range(3, 31))
for num in threes:
	if num % 3 == 0:
		print(num)

print("\n")

# printing numbers cubed.
cubes = list(range(1, 11))
for number in cubes:
	number = number**3
	print(number)

cube_comp = [val ** 3 for val in range(1, 11)]

print(cube_comp)