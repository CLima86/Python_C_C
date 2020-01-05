"""
File: guests_list.py
Original author: C. D. Lima
"""

guests = []
guests.append('carl gauss')
guests.append('emmy noether')
guests.append('christopher hitchens')
guests.append('terence tao')
guests.append('maryam mirzakhani')
guests.append('sam harris')
guests.append('maajid nawaz')
guests.append('richard feynman')

for guest in guests:
	print("\nHello, " + guest.title() + " I would like to invite you to a casual dinner with other esteemed colleagues this Friday.")

print("\nUnfortunately Mr. " + guests[0].title() + " cannot make it to dinner.")

guests[0] = 'jacob lurie'
print("\n",guests)

for guest in guests:
	print("\nHello, " + guest.title() + " I would like to invite you to a casual dinner with other esteemed colleagues this Friday.")

for guest in guests:
	print("\nHello, " + guest.title() + ", I have found a larger dinner table.")

guests.insert(0, 'alan turing')
guests.insert(4, 'john von nuemann')
guests.insert(10, 'ada lovelace')

"""
for guest in guests:
	print("\nHello, " + guest.title() + " I would like to invite you to a casual dinner with even more esteemed colleagues this Friday.")

for guest in guests:
	print("\nHello, " + guest.title() + " , unfortunately I can only invite two people to dinner this Friday.")

ada = guests.pop(10)
print("\nHello, " + ada.title() + " , unfortunately I can't have you for dinner this Friday.")

john = guests.pop(4)
print("\nHello, " + john.title() + " , unfortunately I can't have you for dinner this Friday.")

alan = guests.pop(0)
print("\nHello, " + alan.title() + " , unfortunately I can't have you for dinner this Friday.")

dick = guests.pop(7)
print("\nHello, " + dick.title() + " , unfortunately I can't have you for dinner this Friday.")

maryam = guests.pop(4)
print("\nHello, " + maryam.title() + " , unfortunately I can't have you for dinner this Friday.")

terence = guests.pop(3)
print("\nHello, " + terence.title() + " , unfortunately I can't have you for dinner this Friday.")

chris = guests.pop(2)
print("\nHello, " + chris.title() + " , unfortunately I can't have you for dinner this Friday.")

emmy = guests.pop(1)
print("\nHello, " + emmy.title() + " , unfortunately I can't have you for dinner this Friday.")

jacob = guests.pop(0)
print("\nHello, " + jacob.title() + " , unfortunately I can't have you for dinner this Friday.")

for guest in guests:
	print("\nHello, " + guest.title() + ", if you're still able and willing, I would like to have you and one other guest for dinner.")
del guests[0]
del guests[0]

print(guests)
"""

print("\nThere will be " + str(len(guests)) + " guests coming to dinner on Friday.")