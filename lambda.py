from functools import reduce

# simple expression returning value

squared = lambda num : num * num
print(squared(2))

addTwo = lambda num : num + 2
print(addTwo(12))

lambda a, b : a + b



###############



def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)
print(addTen(7))            # lambda is called when function is called => num = 7 here
print(addTwenty(7))



#################

# higher order functions = function that receives another function as argument or returns a function



lambda num : num * num
numbers = [3, 24, 69, 12, 47, 13, 9]
sqNums = map(lambda num : num * num, numbers)           # applies function on every item inside list
print(list(sqNums))



#################



lambda num : num % 2 != 0
oddNums = filter(lambda num : num % 2 != 0, numbers)            # filtered out anything that hasn't a True result
print(list(oddNums))



###############



lambda acc, curr : acc + curr
numbers = [1,2,3,4,5,1]
total = reduce(lambda acc, curr : acc + curr, numbers, 10)          # can define a starting value -> here 10
print(total)

print(sum(numbers))         # built in python function + can add a strating value too

lambda acc, curr : acc + len(curr)
names = ["Martin Garrix", "David Guetta", "Avicii"]
charCount = reduce(lambda acc, curr : acc + len(curr), names, 0)            # 0 is necessary to tell the reduce we are waiting for a number
print(charCount)