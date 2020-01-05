"""
File: person.py
Original Author: C. D. Lima
"""

# someone's information
person = {'first_name': 'jessica', 'last_name': 'lima', 'age': 30, 'city': 'cypress'}
print(person['first_name'], "\n")
print(person['last_name'], "\n")
print(person['age'], "\n")
print(person['city'], "\n")

# people's numbers
fav_numbers ={'jessica': 15, 'camila': 19, 'carlos': 42, 'ricky': 99, 'natalia': 67}
for key, value in fav_numbers.items():
	print(key, value)