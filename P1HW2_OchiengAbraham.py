# Travel Expense Calculator
# Asks for a budget and expected costs, then shows what's left over.


def fmt(amount):
    """Show whole numbers without decimals (1200), otherwise 2 places (1200.50)."""
    return f"{amount:.0f}" if amount == int(amount) else f"{amount:.2f}"


print("This program calculates and displays travel expenses")

# 3. Ask user to enter their budget
budget = float(input("\nEnter Budget: "))

# 4. Ask user to enter travel destination
destination = input("\nEnter your travel destination: ")

# 5. Ask user for amount they will spend on gas
gas = float(input("\nHow much do you think you will spend on gas? "))

# 6. Ask user for amount they will spend on accommodation
accommodation = float(input("\nApproximately, how much will you need for accomodation/hotel? "))

# 7. Ask user for amount they will spend on food
food = float(input("\nLast, how much do you need for food? "))

# 8. Add expenses
total_expenses = gas + accommodation + food

# 9. Subtract expenses from budget
remaining_balance = budget - total_expenses

# 10. Display results
print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", fmt(budget))
print()
print("Fuel:", fmt(gas))
print("Accomodation:", fmt(accommodation))
print("Food:", fmt(food))
print()
print("Remaining Balance:", fmt(remaining_balance))
