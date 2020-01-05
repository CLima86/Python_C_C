"""
File: motorcyles.py
Author: C. D. Lima
"""
# Here we'll look at changing, adding, and removing elements of lists
# First we create a list and try to change one of the elements in the list.
# In motorcyles we will change the first element. We will do so by explicitly
# pointing to the first element, indexed by [0], and setting it to a new string.

motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)

# motorcyles[0] = 'ducati'
# print(motorcyles)

# instead of changing an element we can just add an element by using the .append() method.

motorcyles.append('ducati')
print(motorcyles)

# If we had an empty list, append allows us to dynamically nuild the list by adding elements.
# Example:

foods = []
foods.append('pizza')
foods.append('salad')
foods.append('tacos')
print(foods)

# The append method automatically adds an element to the end of a list, but we could add
# an element at any point in the list by using the .insert(index, element) method.

motorcyles.insert(0, 'harley davidson')
print(motorcyles)

# Removing Elements from a List #

# This can be done in a couple of ways. Let's look at the 'del' statement first.
# The following line will remove 'harley davidson' from out list.

del motorcyles[0]
print(motorcyles)
# And so it does, but the issue with the 'del' statement is that one can no longer access
# the element that was removed, so let's place the value in again and then look at .pop() method.

motorcyles.insert(0, 'harley davidson')
print(motorcyles)

# The .pop() method allows you to remove an element from a list, and store the value in a variable,
# so one can work with it later. The method behoaves like LIFO stack in the sense that it will
# remove the last element of the list, but one can explicitly tell the method which element to pop
# if there is an element of interest. Look at the following lines of code.

popped_motorcyle  = motorcyles.pop()
print(motorcyles)
print(popped_motorcyle)

# Let us now explicitly tell the method what element to pop and use it in a statement.
# But let's append the element we removed.

motorcyles.append(popped_motorcyle)
print(motorcyles)

first_owned = motorcyles.pop(0)
print('The first motorcyle I owned was a ' + first_owned.title() + '.')
print(motorcyles)

# If we didn't know the number of elements we had in a list, but we knew the value of the element,
# then we can use the .remove() method in order take the item out of the list. For example, assume
# we didn't know where in the list 'suzuki' was, but we wanted to get rid of it.

motorcyles.remove('suzuki')
print(motorcyles)

# With the .remove() method we can also store the value in a variable and work with it if we like.

motorcyles.insert(2, 'suzuki')
print(motorcyles)

too_expensive = 'ducati'
motorcyles.remove(too_expensive)
print(motorcyles)
print("\nA " + too_expensive.title() + " is too expensive for me to purchase.")

# A thing to note!!! The .remove() method deletes only the first occurance of the value you specify.
# If there's a possibility that the vlau eappears more than once in the list, you'll need to use a loop
# to determine if all occurances of the value have been removed.