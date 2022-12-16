# the follwing line reads the list from the input, do not modify it, please
passwords = input().split()

# your code below
passwords.sort(key=len)
for i in passwords:
    print(i, len(i))
