"""
File: magicians.py
"""

# Here we will use a 'for loop' to iterate throuhg a list of magician names.

# The first line of the for loop tells Python to take an element from the list magicians,
# and store it in the VARIABLE 'magician'. It then prints the value, and does this again
# for every element until there are no more elements left in the list.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great show!")
# Since the line above is outside the for loop it is only executed once.
