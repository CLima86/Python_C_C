"""
File: alien.py
Original Author: C. D. Lima
"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# You can have an unlimited number of key-value pairs in a dictionary.

# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")


# Dictionaries are dynamic structures, and you can add new key-value
# pairs to a dictionary at any time.
# Let's add two pieces of information to the alien_0 dictionary.

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# You can see the new key_value pairs were added to the dictionary.

print("\n")

# Starting with an empty dictionary....
alien_1 = {}

alien_1['color'] = 'blue'
alien_1['points'] = 10

print(alien_1)
print("\n")
# Modifying Values in a Dictionary #
# Simply call the key in the dictionary you want to change and
# assign it the new value you would like associated with it.

print("The 0th alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The 0th alien is now " + alien_0['color'] + ".")
print("\n")

# Let's work with a more interesting example of using dictionaries.
alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_2['x_position']))
print("\n")
alien_2['speed'] = 'fast'
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_2['speed'] == 'slow':
	x_increment = 1
elif alien_2['speed'] == 'medium':
	x_increment = 2
else:
	# this must be the fast alien
	x_increment = 3

# The new position is the old position plus the increment.
alien_2['x_position'] = alien_2['x_position'] + x_increment

print("New position: " + str(alien_2['x_position']))
print("\n")

# Removing key-value pairs #

# Using the 'del' statement will completely remove the key-value pair from
# the dictionary. AND IT IS DELETED PERMANENTLY!!

del alien_0['points']
print(alien_0)
# Now alien_0 has only 3 key-value pairs.