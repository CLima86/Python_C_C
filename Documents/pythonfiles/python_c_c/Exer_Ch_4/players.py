"""
File: players.py
Original Author: C. D. Lima
"""

# Specify what elements you would like by placing them in brackets and 
# seperating them by a colon. With the index on the right being an exlcuded value.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# One can also generate a subset of the list as follows. Again the index on the right
# is excluded.
print(players[1:4])

# python automatically will print starting from the beginning of the list if you exclude
# the index on the RHS.
print(players[:4])

# Similarly, if you need something to include the end of the list...
print(players[2:])

# We can also print the back end of a list by adding a minus sign to the LHS of the slicing
# method. [-3:]
print(players[-3:])

print("\n")
# Loopin Through a Slice #

print("Here are the names of the first three players on my team: ")
for player in players[:3]:
	print(player.title())
