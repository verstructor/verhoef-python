# Return a collection of numbers.
def getNumsA(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

# Equivalent effect using a generator.
def getNumsB(n):
    num = 0
    while num < n:
        yield num
        num += 1

# Client code.
print("Sum using traditional function: %s" % sum(getNumsA(10)))
print("Sum using generator function:   %s" % sum(getNumsB(10)))