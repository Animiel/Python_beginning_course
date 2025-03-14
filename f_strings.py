
# printing messages containing variables
person = "Me"
coins = 3

# method 1
print("\n" + person + " has " + str(coins) + " coins left.")
# method 2
message = "\n%s has %s coins left." % (person, coins)
print(message)
#method 3
message = "\n{} has {} coins left.".format(person, coins)
print(message)
# method 4
# working with indexes
message = "\n{1} has {0} coins left.".format(person, coins)
print(message)
# method 5
message = "\n{person} has {coins} coins left.".format(person=person, coins=coins)
print(message)

# method 6
# working with dictionaries
player = {
    "person": "Me",
    "coins": 3
}

message = "\n{person} has {coins} coins left.".format(**player)         # dictionary must be called with **, {} must contain the keys
print(message)



# method 7 : f-Strings

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2 * 5} coins left."
print(message)

message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)

message = f"\n{player["person"]} has {2 * 5} coins left."
print(message)

# can pass formatting options

num = 10
print(f"\n2.25 time {num} is {2.25 * num:.2f}")         # :.2f = 2 decimals fixed

for num in range(1, 11):            # remember loop stops at n-1 -> so put 11 to stop at 10
    print(f"2.25 time {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")         # getting a percentage

# more about format : https://www.w3schools.com/python/ref_string_format.asp