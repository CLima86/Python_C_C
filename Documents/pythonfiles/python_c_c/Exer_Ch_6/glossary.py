"""
File: glossary.py
Original Author: C. D. Lima
"""

glossary = {
	'string': 'object',
	'list': 'object',
	'dictionary': 'data structure',
	'method': 'an action',
	'for-loop': 'control flow statement',
	'if-elif-else': 'control flow statement',
	'boolean': 'binary variable',
	'tuple': 'immutable object'
	}

for key, value in glossary.items():
	print("\n")
	print(key.title() + ": " + value.title())

# Rivers #
rivers = {
	'nile': 'egypt',
	'ganges': 'india',
	'mississippi': 'united states'
	}

for river, country in rivers.items():
	print("The " + river.title() + " river runs through " + country.title() + ".")

print("\n")

for river in rivers:
	print(river.title())

print("\n")

for country in rivers.values():
	print(country.title())