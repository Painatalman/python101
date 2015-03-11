# Python 101

+ Authors: @foxdarkmaster , @painatalman 
+ Version: 0.0.5
+ Last revision: 2015-03-10

### Table of contents

1. Abstract
1. About us
1. Why Python?
1. Around the world
1. Coding in Python
  + Py vs...
1. In conclusion
1. Sources

### Abstract

> 

### About us

#### The Organization

Dengun is a web agency dedicated to the development of solutions for online problems and campaigns. Notable works include # TODO

#### The presenters

Currently, @painatalman and @foxdarkmaster are two interns working at Dengun as web developers. @painatalman is mostly a front-end developer, whereas @foxdarkmaster focuses on mobile development and back-end.

#### The technology

At Dengun, the main objective is to provide customers with proper and updated web solutions that can be

### Python

Python is a programming language with efficiency and readability at the core of its concept. 

#### Main Characteristics (Summary)

+ Is a scripting language (?)
+ Types and variables
+ Indentation over curly braces for organizing blocks
+ variables and types in python
+ multiparadigm
+ wide list of libraries
+ standards: pep/flake philosophy

#### Scripting language?

Basically, this means that the code is not compiled but rather "interpreted", line by line. However, this "scripting" thing is more related to the working environment. For example, one might create a C interpreter (rather than a compiler) that automatically runs written code on demand.

In other words, if you want to try python, no need to have a specific "compiler". Just install it and try it on the command line... or one of these websites:

+ [ipython-try][https://www.pythonanywhere.com/try-ipython/]
+ [Learn Python][http://www.learnpython.org/]
+ [Codecademy]

Now, try this code, line by line, and pay attention to the interpreter's responses:

```python
3 + 10
x = 10
x + 3
print x
```

See how each action has a response from the interpreter (although 'x=10' returned no apparent answer)? That's because the python command line shell is a **REPL** (Read-eval-print loop), which is a type of software that reads single expressions and returns a response.

#### Types

As one might already know, different types of data can be stored in different types of "variables". This definition is important in order for the Python interpreter to know how to deal with specific type of information. It makes sense to add numbers, but not sequences of characters, for example.

So, on to the example:

```python
x = 10      # this is a comment, btw...
type(x)     # integer
y = "Rambo" 
type(y)     # string, right?
x = 2.0     
type(x)     # not an integer, anymore!
```

At the beginning, 'x' was an integer, but then, with another declaration, it became a float. It is also dynamic (in terms of typing), since type safety is done at runtime (in other words, it is while the program is running, and not during compile phase, that it is checked whether the operation is valid between elements of types involved.

But why that weird <type 'str'> syntax? Actually, it's because in Python, **everything** is an object. So Python is essentially what we call an Object-oriented programming language. And what defines an object? It is a type of data that has not only data inside it, but also methods that enable us to interact with such data. Type itself is an object, actually!

First, there's Boolean values:

##### True or False?

Boolean variables can only have one of two values: *True* and *False* (capitalized). These are useful for evaluating conditions, which are ways for a program to determine whether or not to run certain statements, based on other values.

```python
work = True

if work == True:
    print "Working"
else:
    print "Not working"
```

##### Numeric types

Usual numbers that support arithmetic operations, like sums, subtractions, division, modulus.

| Type | Description|
|------|------------|
| int  | Our good friend integer-sized number|
| long | For when you need a BIGGGGGGGGER number |
| float | A floating-point number |
| decimal | Floating-point numbers with a specific precision |
| complex | Python has built-in methods for dealing with complex numbers|

And here are a few numeric operations one can use:

```python
n1 = 10
n2 = 20.0
n3 = 4.323

type (n1)
type (n2)
type (n3)

n1 + n2
type (n1 + n2)
n1 * n3        # why the last decimal case? See https://docs.python.org/2/tutorial/floatingpoint.html
n1 += 3
n1 ** 2
n1 = -n1
abs(n1)
n2 = complex(10, 20)
print n2
n2.real
n2.imag
```

| Type | Description|
|------|------------|
| str | String, text... |
| list | List of variables |
| dict | Dictionary: groups of key/values, where each key must be unique|

The operations one can do with strings are distinct from the ones used in numbers, even if they share common operators:

```python
name = "Bruce"
lastName = "Wayne"
nickname = "Batman"

name + lastName                               # oops, forgot the spaces
name + " " + lastName + "\nthe " + nickname   # that \n over there...
```

And there are others, more complex, which are composed of other data types, like Lists and Dictionaries:

```python
l1 = []                        # there, it is now a list!
type(l1)  

                               # manipulate items in the list
l1.append("batman")
l1.append("t")
l1.append(2)                   # items in the list can be of various types
l1.append([1,3,4])             # even lists!
l1.pop()                       # let us remove that last item, actually!

len(l1)                        # how many items are in a list? 

print l1                       # can a list be printed?

item = l1[1]                   # second item on the list, right? 
                               
print item                     # The first one would be l1[0]

l1[1] = 0                      # changing l1[1]

print l1

print item                     # but item kept its value, becaus it was a copy of the value in l1[1] (and not a reference, like a pointer in C)


# another list
l2 = [1, 2, "three"]
l2.insert(0)

# can we 'join' them with a plus sign?
l1 + l2
````

With the following demo, a few conclusions could be reached:

+ list can be created by simply assigning variables to []
+ a list can be appended to another with the '+' sign 
+ when a variable is assigned to one of the items in the list, it becomes a copy of its current *value*, and not a reference to that position

The number of operations that can be done with lists doesn't end here, though. Python provides a clean way of getting parts/slices of a list, with the following nomenclature:

  ''<list_variable>[<start_index>:<end_index>:<step>]''

where <list_variable> is the variable of the type List, the start_index is an integer representing the starting position, and end_index being the finishing position (not included). The step (gap between one element and the other) is the third element, and can even be negative. All parameters are optional.

Let's focus on an example:

```python

##### list slicing ###################################################
l1 = [0,2,1,"batman"]
subList = l1[1:3:1]            # no Batman? And no zero?
print subList                  # returns a copy of the list, but only from the second to the third item (won't include position 3)

subList = l1[::2]              # all items, but in intervals of 2 (l[0],l[2],...)
reverseList = l1[::-1]         # reversing a list is easy enough. 
                               # It actually doesn't change the original list, just makes a copy of it

stringList = "Gustav"          # a string is like a list of characters
stringList[0:3:1]              # what would this return?

range(50)                      # all up to 50

[2 * n for n in range(40)] # this one is kinda tough... what does it do?
```

##### Dictionaries

Dictionaries, unlike lists, are adequate for organizing information that is somehow related, given that it has some kind of 'role' in the context of such data. As usual, it's simpler to just give an example. Let's suppose we would like to store the setting configurations of a videogame:

```python

settings = {
    "difficulty": 3,
    "nrLives": 3,
    "startingLevel": 1,
    "canCheat": False,
    "specialPowersAllowed": ["teleportation", "flying", "fireballs"]
}

print settings["nrLives"]
settings["nrLives"] = 50
```

In this context, a videogame has a settings configuration that has only one possible value (might be a list or not) for each property. It doesn't make sense to have two difficulties, but it is possible for different properties to have the value 3, for example. The properties have a name, which is called a 'key', which is unique for each Dictionary variable. The value, on the other hand, can be of any type (even a dictionary itself).

One might compare dictionary variables to real-life dictionaries: two words may have the same meaning, but there is just one entry for each word. If that were not the case, which definition would be chosen by someone consulting it?

##### Duck-typing?

Variable declaration in Python is not required - as a matter of fact, it's not even allowed directly!

```python
x = 1    # There! You have a variable x of the type integer... 
type(x)  
```

** Is this good, though?**

It depends on who one may ask to, but there is a key-factor here: *duck-typing*. This type of variable typing refers to programming languages where the type is inferred, not declared. When a variable is assigned a value and then used, it gets created, then deleted when out of scope (garbage collection, maybe some other time). However, this doesn't mean that python isn't strongly-typed. Variables have types, and are not converted inductively. If an unexpected type is detected in an expression, an error occurs.

```python

x = 1
y = 2
x + y # 3, no one expects NOT to be able to sum integers

str_1 = "bat"
str_2 = "man"

str_1 + str_2 # returns "batman", because there is a + operation expecting two strings

# but...
x + str_1 # TypeError: cannot concatenate 'str' and 'int' objects

str_1 * 3 # this works, btw...
```

In order to avoid bugs from coming in, ambiguous operations throw an error. In this case, would we want a sum or a concatenation.

> So, Python is indeed duck-typed, but it won’t do any of that auto-conversion magic for you if there’s more than one possible meaning. [source][http://mikelev.in/2011/01/python-programming-language-advantages/]

#### Code blocks and indentation

As mentioned by [Mike Lev][mikelev], Python does not use curly braces to organize code blocks (unlike the BCPL family of Programming Languages, like C or Java). This ensures **readability** for the code not only for the programmer but also for the team, as it defines a single standard for blocks to be written and defined properly. 



By Python coding standards like PEP or Flake, the standard indentation is 4 spaces, but it doesn't have to be strict to that spacing. 

For instance, let's check a function definition in C, with an if statement inside:

```C
void do_something(bool isFast){
  if (isFast==true){
     
     printf("Okay, okay...\n");
   int total, j, k;


       j = 4;
      k = 5;

            total = j + k;
  }
}
```

In the code block (the function and the *if* part), there is no need to keep indentation consistent, as long as it's inside the curly braces. 

Now, how would we do this in Python?

##### Functions

To define a function in python, a declaration has to start with the 'def' keyword, along with the function name and parameter names in braces. Parameters are values which are sent to the function in order to be used by it. A function may or may not have a return statement, which defines what the result of the block of operations would be.

```python
def do_something(isFast):
    if isFast == True:
        print "Okay, okay...";
        j = 4
        k = 5
        total = j + k;
        print "the sum of %d and %d is %d" % (j, k, total)
    else:
        print "not willing to work, yet!"
```

One of the most common functions  they can have parameters with default values, and they can be defined in different order than the one they're mentioned in the definition. 


###### Ready for a quiz?

Start [here][http://programarcadegames.com/quiz/quiz.php]

### Libraries and frameworks

Python has a wide variety of packages to extend its functionalities.

##### Installing packages


### Sources

+ [Which code editors do pythonists use][code-editor-use]

[code-editor-use]: http://www.sitepoint.com/which-code-editors-do-pythonists-use/ "Which code editors do pythonists use"
[python-lib-1]: http://programarcadegames.com/quiz/progress.php?lang=pt "Pygame python library"
[mikelev]: http://mikelev.in/2011/01/python-programming-language-advantages/ "Mike Lev"
[langpop]: http://www.langpop.com/ "Language Popularity"
[learn-python]: http://www.learnpython.org/ "Learn Python"
[codeskulptor]: http://www.codeskulptor.org/
[]