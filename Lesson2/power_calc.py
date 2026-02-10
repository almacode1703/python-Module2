# Power Calculator

base = int(input("Enter base number: "))
power = int(input("Enter power: "))

result = 1

# for loop to calculate power
for i in range(power):
    result = result * base

print(f"{base} raised to power {power} = {result}")
