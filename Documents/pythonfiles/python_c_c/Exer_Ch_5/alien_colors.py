"""
File: alien_colors.py
Original Author: C. D. Lima
"""

alien_color = 'yellow'

if alien_color == 'green':
	print("\nPlayer One, you just earned 5 points.")
else:
	print(None)

alien_color2 = 'green'

if alien_color2 == 'green':
	print("\nPlayer One, you just earned 5 points.")


alien_color3 = 'yellow'

if alien_color3 == 'green':
	print("\nPlayer One, you just earned 5 points.")
else:
	print("\nPlayer One, you just earned 10 points!")

alien_color4 = 'yellow'

if alien_color4 == 'green':
	print("\nPlayer One, you just earned 5 points.")
elif alien_color4 == 'yellow':
	print("\nPlayer One, you just earned 10 points!")
else:
	print("\nPlayer One, you just earned 15 points!!")


alien_color4 = 'green'

if alien_color4 == 'green':
	print("\nPlayer One, you just earned 5 points.")
elif alien_color4 == 'yellow':
	print("\nPlayer One, you just earned 10 points!")
else:
	print("\nPlayer One, you just earned 15 points!!")


alien_color4 = 'red'

if alien_color4 == 'green':
	print("\nPlayer One, you just earned 5 points.")
elif alien_color4 == 'yellow':
	print("\nPlayer One, you just earned 10 points!")
else:
	print("\nPlayer One, you just earned 15 points!!")

# Stages of Life #

age = 1000

if age < 2:
	print("\nThis person is a baby.")
elif age >= 2 and age < 4:
	print("\nThis person is a toddler.")
elif age >= 4 and age < 13:
	print("\nThis person is a kid.")
elif age >= 13 and age < 20:
	print("\nThis person is a teenager.")
elif age >= 20 and age < 65:
	print("\nThis person is an adult.")
else:
	print("\nThis person is an elder.")


# Favorite Fruits #

favorite_fruits = ['bananas', 'oranges', 'kiwis']

if 'apple' in favorite_fruits:
	print("You really like apples!")
if 'tomato' is favorite_fruits:
	print("You really like tomatos!")
if 'grape' in favorite_fruits:
	print("You really like grapes!")
if 'oranges' in favorite_fruits:
	print("You really like oranges!")
if 'bananas' in favorite_fruits:
	print("You really like bananas!")
if 'kiwis' in favorite_fruits:
	print("You really like kiwis!")