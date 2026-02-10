age = int(input("Enter your age: "))

if age in range(10, 21):   # 21 because range end is exclusive
    print("Age is between 10 and 20")
else:
    print("Age is NOT between 10 and 20")
