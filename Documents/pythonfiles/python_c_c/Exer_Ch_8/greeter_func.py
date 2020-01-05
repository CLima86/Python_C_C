"""
File: greeter_func.py
Original Author: C. D. Lima
"""
# We can initially have a function that needs no information in order to call it.
# But we can add parameters to the function when it has a more complex code in
# the body of the function.


def greet_user(username):
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")

greet_user("carlos")

# in this example we have applied a parameter 'username' to the function. And
# when the function is called the value 'carlos' becomes the arguement for our
# parameter.