total = 0

while True:
    expense = input("Enter expense amount (or 'done' to finish): ")

    if expense.lower() == "done":
        break

    expense = float(expense)

    total = total + expense

print("Total Spent:", total)