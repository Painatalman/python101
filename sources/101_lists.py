l1 = []                     # there, it is now a list!
type(l1)

# manipulate items in the list
# slicing
l1.append("batman")
l1.append("t")
l1.append(2)                # items in the list can be of various types
l1.append([1, 3, 4])             # even lists!
l1.pop()                    # let us remove that last item, actually!

len(l1)                     # how many items are in a list?

print l1                    # can a list be printed?

item = l1[1]                # second item on the list, right?
item = l1[0]                # The first one would be l1[0]

subList = l1[1:3:1]         # no Batman?
print subList               # returns a copy of the list, but only from the second to the third item (won't include position 3)

subList = l1[::2]           # all items, but in intervals of 2 (l[0],l[2],...)
reverseList = l1[::-1]      # reversing a list is easy enough.
# It actually doesn't change the original list, just makes a copy of it

stringList = "Gustav"       # a string is like a list of characters
stringList[0:3:1]           # what would this return?

# a little extra...
range(50)                   # all up to 50

doubleList = [2 * n for n in range(40)]    # this one is kinda tough... what does it do?
