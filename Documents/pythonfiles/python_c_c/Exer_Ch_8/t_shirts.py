"""
File: t_shirts.py
Original Author: C. D. Lima
"""

def make_shirt(message, size='large'):
	"""Function prints size and message of shirt"""
	print("\nThe t-shirt size is " + size.title() + " and the message printed on it is, " + message.title() + ".")

make_shirt(message='i love python!')


# Cities:

def describe_city(name, country='united states'):
	""" function that prints the name of a city and the country it's in."""
	print("\n" + name.title() + " is in " + country.title())

describe_city(name='san francisco')
describe_city(name='los angeles')
describe_city(name='paris', country='france')