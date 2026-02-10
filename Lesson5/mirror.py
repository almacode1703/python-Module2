rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    # print spaces first
    for j in range(rows - i):
        print(" ", end="")

    # print stars
    for k in range(i):
        print("*", end="")

    print()   # move to next line
