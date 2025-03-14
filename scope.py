# Scope = place where a variable is defined

name = "Flo"            # global scope -> name is available everywhere
count = 1

# def greeting(name):
#     color = "Green"         # local scope -> color is only available inside the function
#     print(color)
#     print(name)

# greeting("Me")



def another():
    color = "Green"
    # count = 2           # Count = 2 but printing it outside the function Count = 1
    global count            # manipulating variable cannot be on same line
    count += 1
    print(count)

    def greeting(name):
        nonlocal color          # gets a variable from parent
        color = "Red"           # reassigning the color variable from the parent
        print(color)
        print(name)
    
    greeting("You")

another()