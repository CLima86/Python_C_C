"""
File: counting.py
Original Author: C. D. Lima
"""

current_number = 1
while current_number <= 4:
	print(current_number)
	current_number += 1

# letting the user choose when to quit...
prompt = "\nTell me somthing, and I will repaet it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print(message)

# The if-statement above keeps the program from printing 'quit'
# when the user enter it to the console. It makes a quick check to
# see if message = 'quit'...if it doesn't, then it will print the
# message, if not, then it doesn't pass the if test and won't print.

# using continue in a loop

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue

	print(current_number)