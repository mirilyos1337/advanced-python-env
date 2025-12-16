

a = float(input("Enter a number: "))

integer_part = int(a)
fractional_part = int((a - integer_part) * 100)

result = fractional_part + integer_part / 100

print(result)
