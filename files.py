import os

# r = read
# a = append
# w = write
# x = create

# similar to CRUD



##########################

# Read - error if it doesn't exist



f = open("names.txt", "r")          # can be "rt" (text) or "rb" (binary)
# print(f.read())
# print(f.read(4))
# print(f.readline())
# print(f.readline())
for line in f:
    print(line)

f.close()           # always closing the file when done with it

try:
    f = open("names.txt")
    print(f.read())
except:
    print("File doesn't exist")
finally:
    f.close()




#####################

# Append - creates the file if it doesn't exist



f = open("names.txt", "a")          # a for append
f.write("Thomas\n")
f.close()
# if not closed above but instead read it, Thomas wouldn't appear => importance of closing the file after manipulation
f = open("names.txt")          # default = read -> nothing mentionned
print(f.read())
f.close()



#####################

# Write (overwrite) - creates file if it doesn't exist too



f = open("context.txt", "w")            # w for write
f.write("I deleted all of context.")
f.close()

f = open("context.txt")
print(f.read())
f.close()



#######################

# Create

# creates file, but returns error if file exists

if not os.path.exists("flo.txt"):
    f = open("flo.txt", "x")
    f.close()

# Delete

# avoid error if doesn't exist

if os.path.exists("flo.txt"):
    os.remove("flo.txt")
else:
    print("The file doesn't exist.")

# "copy paste" a file

with open("context.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)