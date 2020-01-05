"""
File: pets.py
Original Author: C. D. Lima
"""

def describe_pet(animal_type, pet_name_1, pet_name_2):
	"""Display information about a pet."""
	print("\nI have two " + animal_type.title() + "s.")
	print("\nMy " + animal_type.title() + "'s names are " + pet_name_1.title() + " and " + pet_name_2.title() + ".")

describe_pet('dog', 'bam bam', 'iron hide')


# In the example above we worked with positional arguments. So the position of the arguments and
# variables matter when they are called with the function.


# Keyword Arguments...

# A keyword argument is a name-value pair that you pass to a function. Directly associating the name
# and the value within the argument, that way when you pass the argument to the function there is no
# confusion. This keeps you from having to worry about the position of your arguments in your function
# call.

# we will use a similar function name for this example.

def describe_pet_2(animal_type, pet_name_1, pet_name_2):
	"""Display information about a pet."""
	print("\nI have two " + animal_type.title() + "s.")
	print("\nMy " + animal_type.title() + "'s names are " + pet_name_1.title() + " and " + pet_name_2.title() + ".")

describe_pet(animal_type='dog', pet_name_1='bam bam', pet_name_2='iron hide')
describe_pet(pet_name_1='bam bam', pet_name_2='iron hide', animal_type='dog')
describe_pet(animal_type='dog', pet_name_2='iron hide', pet_name_1='bam bam')

# All the calls above will print the same result, because we have used a keyword argument.


# Default values...
# Default values are placed ase arguments at the initial definition of the function.
# When using default values you must place the default value after all undefined parameters. Or you
# will get a SyntaxError.

def describe_pet_3(pet_name, animal_type='dog'):
	"""Display information about a pet."""
	print("\nJessica has a favorite " + animal_type.title() + ".")
	print("\nHer favorite " + animal_type.title() + "'s name is " + pet_name.title() + ".")

describe_pet_3(pet_name='bam bam')