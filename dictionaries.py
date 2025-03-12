# Dictionaries (look like JS arrays)

# creating dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
}
band2 = dict(vocals="Plant", guitar="Page")         # using the constructor

print(type(band))
print(len(band))

# accessing items inside dictionaries

print(band["vocals"])
print(band.get("guitar"))
# list all keys
print(band.keys())
# list all values
print(band.values())
# list of key/value pairs as tuples
print(band.items())         # returns a list of tuples [(vocals, plant), (guitar, page)]
#verify a key exists
print("guitar" in band)
print("triangle" in band)

# change values

band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})            # can be used to add new keys too, like this one
print(band)

# remove items

print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)
print(band.popitem())           # returns tuple
print(band)

# delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)
del band2

# copy dictionaries

# BAD COPY

# band2 = band            # create a reference
# # any changes made to band2 after that, will be on band too.
# band2["drums"] = "Nils"
# print(band)         # will return "drums": "Nils" at the end

# RIGHT COPY

band2 = band.copy()
band2["drums"] = "Nils"

band3 = dict(band)          # making copy using constructor

# nested dictionaries

member1 = {
    "Name": "Plant",
    "Instrument": "Vocals"
}
member2 = {
    "Name": "Page",
    "Instrument": "Guitar"
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["Name"])          # returns the name of member one => digging through dictionaries levels





# sets

nums = { 1, 2, 3, 4}
nums2 = set(( 1, 2, 3, 4))          # using the constructor

# no duplicates allowed
nums = { 1, 2, 2, 3}            # returns { 1, 2, 3}
# true is a dupe of 1, false of 0
nums = { 1, True, 2, False, 3, 4, 0}            # returns {False, 1, 2, 3, 4}
# check value in set
print(2 in nums)
# can't refer to an element in sets with index position or key
# add new value to set
nums.add(8)
# add elements from set to another
morenums = { 5, 6, 7}
nums.update(morenums)
print(nums)
# can use update with lists, tuples and dictionaries -> between the brackets, not applied on)

# merge 2 sets
one = { 1, 2, 3}
two = { 5, 6, 7}

newSet = one.union(two)
print(newSet)

# keep duplicates
one = { 1, 2, 3}
two = { 2, 3, 4}

one.intersection_update(two)
print(one)

# everything except duplicates
one = { 1, 2, 3}
two = { 2, 3, 4}

one.symmetric_difference_update(two)
print(one)