import math

# String data type

# literal assignement

first = 'firstname'
last = 'lastname'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function

# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation

fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string

decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock from the " + decade + "s."
print(statement)

# multiple lines

multiline = '''
Hey how are you ?

Good. I was just checking in.
                                All good.

'''
print(multiline)

# escaping special characters
sentence = 'I\'m back at work.\tHey !\n\nWhere\'s this at\\located ?'
print(sentence)

# string methods (functions)

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())  # capitalize first letter of each word
# replaces EVERY word good with okay /!\ CASE SENSITIVE !! replaces EVERY 'good' but not 'Good' or other variations
print(multiline.replace("good", "okay"))
print(multiline)

print(len(multiline))
multiline += "                 "
multiline = "              " + multiline
print(len(multiline))           # whitespaces are counted

print(len(multiline.strip()))            # removing all the whitespaces
print(len(multiline.lstrip()))          # removing all the whitespaces on the left side of the string
print(len(multiline.rstrip()))          # removing all the whitespaces on the right side of the string

print("")           # leaving an empty line to see results better on terminal (could comment all the upper code but wouldn't be readable anymore)

# Build a menu

title = "menu".upper()
print(title.center(20, "="))            # Puts "=" on the left and right side of "MENU" to reach a line length of 20 characters
print("Coffee".ljust(16, ".") + "$1".rjust(4))          # rjust(4) justifies the word to the right and puts spaces on the left of "$1" as nothing was mentionned to replace the spaces
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Applepie".ljust(16, ".") + "$5".rjust(4))

print("")

# String index values

print(first[1])
print(first[-1])            # always gives the last letter in a string
print(first[1:-1])            # gives a range of letters (here from 2nd letter to the end (as indexes begin at 0))  /!\ the laste letter won't be printed out !
print(first[1:])            # that includes the last character

print("")

# Some methods return boolean data

print(first.startswith("f"))
print(first.endswith("R"))

# Boolean data type

myValue = True          # Booelan type MUST begin with a cpatial or it won't work -> true won't work but True works
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

print("")

# Numeric data types

price = 100
bestPrice = int(80)

gpa = 3.28
y = float(1.14)

# complex type

compValue = 5+3j            # not used for the basics / learning yet
print(type(compValue))
print(compValue)
print(compValue.real)
print(compValue.imag)

# Built in functions for numbers

print(abs(gpa))
print(round(gpa))           # rounds to the nearest integer (here 3.28 to 3)
print(round(gpa, 1))            # rounds to the nearest first decimal (here 3.28 to 3.3)

#import math         # must figure at the beginning of the file and gives access to other methods like .pi or .sqrt

print(math.pi)          # gives the value of Pi
print(math.sqrt(64))
print(math.ceil(gpa))           # rounds to the upper int
print(math.floor(gpa))          # rounds to the lower int

# casting a string to number

zipCode = "10001"
zipValue = int(zipCode)
print(type(zipValue))

# Error when casting incorrect data

# zipValue = int("New York")