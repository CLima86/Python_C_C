"""
File: places_travel.py
Original Autthor: C. D. Lima
"""

destinations = ['france', 'scotland', 'italy', 'china', 'samoa']

print(destinations)

print("\nHere's the sorted list: ")
print(sorted(destinations))

print("\nHere's the original list: ")
print(destinations)

print("\nHere's the sorted list in reverse order: ")
print(sorted(destinations, reverse=True))

print("\nHere's the original list: ")
print(destinations)

print("\nHere's the list in reverse order: ")
destinations.reverse()
print(destinations)

print("\nPrinting the list again, we see the order is permanent: ")
print(destinations)

print("\nHere's the original list, after reversing the reversed order: ")
destinations.reverse()
print(destinations)

print("\nHere's the sorted list, using the permanent sort() method: ")
destinations.sort()
print(destinations)

print("\nHere's the sorted list in reverse order: ")
destinations.sort(reverse=True)
print(destinations)