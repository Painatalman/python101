name = "Bruce"
lastName = "Wayne"
nickname = "Batman"
age = 26

fullName = name + lastName                                 # oops, forgot the spaces

print name + " " + lastName + ", the " + nickname   # that \n over there...
print fullName
print "I am " + fullName
print "I am %s" % (fullName)

print "I am %s \n and I am %d years old" % (fullName, age)
