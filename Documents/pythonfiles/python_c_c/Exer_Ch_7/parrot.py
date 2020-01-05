"""
File: parrot.py
Original Author: C. D. Lima
"""

# Here we start using user inputs and while loops to solve problems.

# The input() function pauses a program and waits for the user to enter
# some text. Once Python receives the inout, it stores the information
# in a variable, which we can work with later. 

prompt = "\nTell me somthing, and I will repaet it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)