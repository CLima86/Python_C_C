"""
File: formatted_name.py
Original Author: C. D. Lima
"""

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted. """
	full_name = first_name + ' ' + last_name
	return full_name.title()

my_name = get_formatted_name('carlos', 'lima')
print(my_name)


# Making an argument optional
# Maybe you want to make giving a middle name optional. But in order to avoid a TypeErro
# we need to account for the missing value in the function that may not be given. We
# do so by using conditional control flow statements.

# Also we leave the parameter middle_name with the default value of an empty string and
# move it to the end. That way we can add string values to the parameter if necessary. 

def get_formatted_name_op(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted. """
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

my_name = get_formatted_name_op('carlos', 'lima')
print(my_name)

my_name = get_formatted_name_op('carlos', 'lima', 'de jesus')
print(my_name)