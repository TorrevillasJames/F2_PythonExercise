n = int(input("Please enter a number: "))

total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"The sum of numbers from 1 to {n} is: {total_sum}")
