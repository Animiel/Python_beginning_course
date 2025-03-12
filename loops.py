# while loop

value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))





# for loop

names = ["Flo", "Alexia", "Iris"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Alexia":
#         break
#     print(x)

# for x in names:
#     if x == "Alexia":
#         continue            # skips the value and goes on with the loop
#     print(x)

# for x in range(4):          # beginns at 0 like indexes
#     print(x)

# for x in range(2, 4):           # includes the beginning number but not the last -> returns 2, 3
#     print(x)

# for x in range(5, 101, 5):
#     print(x)
# else:
#     print("Glad that\'s over.")




# loop through several lists

actions = ["Codes", "Eats", "Sleeps"]

# for name in names:
#     for action in actions:
        # print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")