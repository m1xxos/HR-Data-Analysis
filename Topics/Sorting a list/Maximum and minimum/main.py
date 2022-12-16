# the following code creates a list from input, please do not modify it
ints = [int(num) for num in input().split()]

# your solution here
ints = sorted(ints)
print(ints[-1], ints[0], ints[1])
