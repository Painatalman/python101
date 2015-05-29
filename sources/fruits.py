fruits = ["banana", "lemon", "apple", "orange", "batman"]

# fruits.sort()    # how will it work if there are different types there?

for fruit in fruits:
    # each item in the list will now be known as fruits
    print "I would like a %s" % fruit

# but the keyword 'in' can also be used OUTSIDE of a 'for' cycle


#
#
# Nothing special, just generates a list of items with the word eaten on it
#
# @pre must be a list of fruits
# @param fruits{List} a list of fruits (probably!)
# @return {List} a new list of fruits
#
#
def eat_fruits(fruits):

    return [fruit + " eaten" for fruit in fruits]

print eat_fruits(fruits)


#
#
# Nothing special, just generates a list of items with the word eaten on it
#
# @pre must be a list of fruits
# @param fruit{String} a list of fruits (probably!)
# @return {Boolean} True if all fruits are valid
#
def validate_fruit(fruit):

    validFruits = [
        'apple',
        'banana',
        'kiwi',
        'lemon',
        'mango',
        'orange',
        'peach'
        'pear',
        'pineapple',
        'plum',
        'prune',
        'strawberry'
    ]

    return True if fruit in validFruits else False


def eat_good_fruits(fruits):
    return [fruit + " eaten" for fruit in fruits if validate_fruit(fruit)]


# import Random
from random import randrange


def get_random_fruit(fruits):
    #  return fruits[Random.randrange(0, len(fruits))]
    return fruits[randrange(0, len(fruits))]


# an example of default values in definitions
# here, we will list fruits in order
def list_fruits(fruits, byName=True):

    if byName:
        fruits.sort()

    for index, fruit in enumerate(fruits):
        if validate_fruit(fruit):
            print "Fruit nr %d is %s" % (index, fruit)
        else:
            print "This %s is no fruit!" % (fruit)
