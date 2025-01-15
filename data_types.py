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
