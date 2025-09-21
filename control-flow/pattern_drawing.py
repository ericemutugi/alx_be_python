# Request user for integer to use as pattern size
size = int(input("Enter the size of the pattern: "))

count = 0

while count < size:
    for size in range(size):
        print("*", end="")
        count = count + 1
    print()
    count = count + 1
