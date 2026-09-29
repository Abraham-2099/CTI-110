# Travel Expense Calculator
# Asks for a budget and expected costs, then shows what's left over.

print("This program calculates and displays travel expenses")

# 3. Ask user to enter their budget
budget = float(input("\nEnter Budget: "))

# 4. Ask user to enter travel destination
destination = input("\nEnter your travel destination: ")

# 5. Ask user for amount they will spend on gas
gas = float(input("\nHow much do you think you will spend on gas? "))

# 6. Ask user for amount they will spend on accommodation
accommodation = float(input("\nApproximately, how much will you need for accommodation/hotel? "))

# 7. Ask user for amount they will spend on food
food = float(input("\nLast, how much do you need for food? "))

# 8. Add expenses
total_expenses = gas + accommodation + food

# 9. Subtract expenses from budget
remaining_balance = budget - total_expenses

# 10. Display results
print("\n------------Travel Expenses------------")
print(f'{"Location":17s} {destination:15s}')
print(f'{"Initial Budget":17s} {"$" + format(budget, ".2f"):15s}')
print(f'{"Fuel":17s} {"$" + format(gas, ".2f"):15s}')
print(f'{"Accommodation":17s} {"$" + format(accommodation, ".2f"):15s}')
print(f'{"Food":17s} {"$" + format(food, ".2f"):15s}')
print("\n----------------------------------------")
print(f'{"Remaining Balance":17s} {"$" + format(remaining_balance, ".2f"):15s}')