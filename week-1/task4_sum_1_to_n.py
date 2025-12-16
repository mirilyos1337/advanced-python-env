

n = int(input("Enter N: "))

total = 0

if n >= 1:
    for i in range(1, n + 1):
        total += i
else:
    for i in range(1, n - 1, -1):
        total += i

print(total)

