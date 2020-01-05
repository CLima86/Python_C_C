# Playing with lists #

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# if you ask Python to print a list, it will return its representation,
# including the brackets. Let's access individual elements of the list.

print(bicycles[0])
print(bicycles[0].title())
# the above lines access the first element of the list, which has the 
# index of 0. It is returned without the brackets. And we also change
# the format pf the string 'trek' by using the string method .title()
# in order to capitalize the string. Let's access other elements.

print(bicycles[1])
print(bicycles[3])

# By adding a minus sign to index 1, [-1], we access the last element
# in the list, which allows us to get that last element without having
# to know the length of the list. Take a look.

print(bicycles[-1])

# We can also store lisyt values in a variable and print them along
# with other strings and concatenate.

message = "My first bicycle was a " + bicycles[2].title() + "."

print(message)