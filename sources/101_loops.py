'''
http://www.devcasts.io/p/python-loops-and-iterations/
'''
# why lists before loops?
# because for loops make sense WITH lists

# a nice and "clean" list of fruits
fruits = [
    "raspberry",
    "strawberry",
    "melon",
    "batman"
]

# the classic loop
for fruit in fruits:
    # each time, this block content will be run
    # with each of the fruits as fruit
    print fruit


# but what about the classic, old
# for (i=0; i < MAX; i++) ?

# REMEMBER, FOR was made for LISTS
# (also known as foreach in other languages)
# but what if, instead of seeing it as an iterator that is increased,
# we think of all numbers [1..10]

# remember
for i in [1:10:1]:
    print i # for (int i=0; i< 10; i++){ ... }

for i in [1:10:2]:
    print i # for (int i=0; i< 10; i=i+2){ ... }

# however, range() is more common


# regular for loops
range(6)
range(1, 7)
range(0, 8, 2)
