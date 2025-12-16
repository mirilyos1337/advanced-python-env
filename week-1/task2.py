
salaries_input = input("Enter salaries separated by spaces: ")

salaries = list(map(int, salaries_input.split()))

max_salary = max(salaries)
min_salary = min(salaries)

difference = max_salary - min_salary

print(difference)

