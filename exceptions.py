x = 2
class JustNotCoolError(Exception):          # creating a custom exception inheriting everything from Excpetion
    pass

# try:
#     print(x)
# except NameError:
#     print("NameError means something is probably undefined")
try:
    raise JustNotCoolError("This isn't cool, man")
    # raise Exception("I'm a custom exception")
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed")         # if argument is empty will raise an empty line on output
except NameError:
    print("NameError means something is probably undefined")
except ZeroDivisionError:
    print("Please do not divide by zero")
except Exception as error:
    print(error)
else:
    print("No errors")
finally:            # will show if an error occured or not
    print("I'm going to print with or without an error")