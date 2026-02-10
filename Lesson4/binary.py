num = int(input("Enter a decimal number: "))

# special case
if num == 0:
    print("Binary = 0")
else:
    binary = ""

    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary  # add at front
        num = num // 2

    print("Binary =", binary)
