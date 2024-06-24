total = 0

expenses = []

num_expenses = int(input("How many expenses do you want to add?"))

for i in range(num_expenses):
    expenses.append(float(input("Add expenses: ")))

total = sum(expenses)

print("You have expenses of $", total, sep = "")