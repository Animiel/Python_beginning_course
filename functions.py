# define a fucntion

def hello_world():          # only lowercase letters accepted
    print("Hello world !")

def sum(num1=0, num2=0):            # can only put the default value to num2, but if num1 has a default value, num2 NEEDS one too
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

total = sum(2, 3)

def multiple_items(*args):          # * means number of arguments is unknown -> return will be tuple
    print(args)
    print(type(args))

multiple_items("Me", "You", 3)

def mult_named_items(**kwargs):         # kwargs = keyword arguments
    print(kwargs)
    print(type(kwargs))

# mult_named_items("Me", "You", 3)            # gives error as keyword is missing
mult_named_items(first = "Me", second = "You", randomNum = 3)           # returns a dictionary