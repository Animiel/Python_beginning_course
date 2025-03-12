# constructing lists

myList = list([1, "Me", True])
ponies = ["Twilight", "Applejack", "Pinky Pie"]
data = ["Strawberries", 31, False]
empty = []

print("Twilight" in ponies)          # Says if Twilight is in the array (true) or not (false)

print(ponies[0])
print(ponies[-2])            # negative numbers search the array from the end where the last element is index -1

print(ponies.index("Pinky Pie"))         # gives position of the element in the array
print(ponies[0:2])           # searching all elements from first position to 2nd /!\ element at index 2 is excluded ! So here just 0 and 1 !
print(ponies[0:])            # same but checking everything, from first to last

print(len(data))            # returns number of items in array, but not indexes -> here gives 3, but indexes are 0, 1, 2.





# modifying items in lists

# adding items

ponies.append("Rainbow Dash")            # adds item to list
ponies += ["Celestia"]          # /!\ must be a list, if it's a string, will put every single letter as an entry inside ponies -> [..., "C", "e", "l", ...]
ponies.extend(["Fluttershy", "Rarity"])         # can be used to add lists too like below
# ponies.extend(data)         # adds data to ponies

ponies.insert(0, "Luna")            # adds Luna to ponies at index 0
ponies[2:2] = ["Trixie", "Sweetie Belle"]           # inserts these items at index 2 WITHOUT replacing the previous value at this position
# ponies[1:3] = ["Someone", "Somepony"]           # replaces values except at index 3

# deleting items

# ponies.remove("Someone")
data.pop()            # removes last item in array
del data[-1]          # removes last item too
# del data        # deletes entirely the list, doesn't exist anymore
data.clear()            # clears the list, still exists but is empty

# sorting lists

ponies.sort()           # sorts list by alphabetical order in ASCII order (means lowercase is sorted out after uppercase)
ponies[1:1] = ["derpy hooves"]
ponies.sort(key=str.lower)          # sorts with the alphabetical order for lower and uppercase
# /!\ to sort lists, must contain same item type for all

numbers = [1, 64, 78, 12, 9]
numbers.reverse()           # reverses order of array items
# numbers.sort(reverse=True)          # unlike the reverse() method, this does sort the list in descending order (from greatest to lowest value)

print(sorted(numbers, reverse=True))            # prints out the above result ONE time only, unlike the above statement that modifies the list

# copying a list

numbersCopy = numbers.copy()
myNumbers = list(numbers)
myCopy = numbers[:]





# tuples

myTuple = tuple(("Me", 22, True, "You"))
otherTuple = (1, 5, "He", False)
# tuples CAN NOT be changed, modified, sorted, etc.

newList = list(myTuple)         # making a list of a tuple
newList.append("Her")
newTuple = tuple(newList)           # making a tuple of a modified list taking a tuple as basis => trick to modify a tuple

(one, two, *hey) = otherTuple           # * -> puts the remaining items into variable hey in LIST type -> putting * at two would set everything in between first and last item in variable two in LIST again
print(one)          # gives 1
print(two)          # gives 5
print(hey)          # gives ["He", False]

print(otherTuple.count(2))          # counts how many times 2 appears in the tuple