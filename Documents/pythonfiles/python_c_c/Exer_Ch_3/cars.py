"""
File: cars.py
Original author: C. D. Lima
"""

# Using the .sort() methoed to organize lists.
# in the simple case, we will have lower case values for the cars. the .sort()
# method will organize these alphabetically, and it changes the order of the list
# PERMANENTLY. Until you decice to change it of course

cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# the list can also be sorted in reverse order by passin gin the argument 'reverse=True'
# into the method.

# cars.sort(reverse=True)
# print(cars)

# If the aim is to only present an ordered list but keep the original order stored, then
# one can use the 'sorted()' function to print the desired order.

print("\nHere's the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere's the original list again: ")
print(cars)
print("\n")

# As you can see the sorted() function temporarily changes the order of the list, keeping
# the original order stored.

# We can also print a list in reverse order without sorting alphabetically.

cars.reverse()
print(cars)

# And then we can reverse it back, since the method changes the order permanently.

cars.reverse()
print(cars)

#length of thhe list.
print(len(cars))
