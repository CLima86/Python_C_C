"""
File: greeter.py
Original Author: C. D. Lima
"""

name = input("Please tell me your name: ")
print("Hello, " + name + "!")

# You can also store your prompt in a variable and then plug
# that into your input() function to make the code nicer to read.

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat's your last name? "

name_1 = input(prompt)
print("\nHello, " + name + " " + name_1 + "!")

# Using int() to take in integer inputs:

age = input("How old are you? ")
print(age)
age = int(age)
print(age >= 18)