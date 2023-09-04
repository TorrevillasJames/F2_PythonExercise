num = int(input("Please enter a number: "))

count = 0
smallest = 9
highest = 0

if num == 0:
    count = 1
    smallest = 0
    highest = 0

while num != 0:
    digit = num % 10
    count += 1

    if digit < smallest:
        smallest = digit
    if digit > highest:
        highest = digit

    num //= 10

print("Number of digits in the given number is: ", count)
print("Smallest number is: ", smallest)
print("Highest number is: ", highest)
