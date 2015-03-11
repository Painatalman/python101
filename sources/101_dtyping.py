x = 1
y = 2
x + y  # 3, no one expects NOT to be able to sum integers

str_1 = "bat"
str_2 = "man"

str_1 + str_2  # returns "batman", because there is a + operation expecting two strings

# but...
# x + str_1 # TypeError: cannot concatenate 'str' and 'int' objects

str_1 * 3  # this works, btw...
