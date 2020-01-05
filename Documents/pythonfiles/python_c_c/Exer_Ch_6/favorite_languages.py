"""
File: favorite_languages.py
Original Author: C. D. Lima
"""

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	'carlitos': 'haskell',
	'camila': 'java',
	'jessica': 'rust',
	}

#print("Sarah's favorite language is " +
#	favorite_languages['sarah'].title() +
#	".")

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
		language.title() + ".")

# Looping Through All Keys in a Dictionary #

# We can access purely the keys in a dictionary using the .keys() method

print("\n")

for name in favorite_languages.keys():
	print(name.title())

# Looping through the keys is actually default behavior when looping through
# a dictionary, the the following line of code gives the same result as above.

print("\n")

for name in favorite_languages:
	print(name.title())

print("\n")

friends = ['phil', 'sarah']

for name in favorite_languages:
	print(name.title())

	if name in friends:
		print("Hello " + name.title() + 
			", I see your favorite language is " + 
			favorite_languages[name].title() + "!")


# You can also use the .keys() method to see if a particualer key exists.
print("\n")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll.")


print("\n")

for name in favorite_languages:
	print(name.title())

print("\n")

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

print("\n")

# Looping through all vallues in a dictionary #
print("The following languages ahev been mentioned in the poll: ")
for language in favorite_languages.values():
	print(language.title())

# We need to check if there are any repeated values. Using the set() method, we can do so.
# The set method identifies unique elements in a list and places them into a subset
# from those elements.

print("\n")

print("The following languages have been mentioned in the poll: ")
for language in set(favorite_languages.values()):
	print("\t" + language.title())