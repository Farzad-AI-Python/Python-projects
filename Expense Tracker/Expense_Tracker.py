import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    print("\nAdd New Expense")

    title = input("Title: ")

    while True:
        try:
            amount = float(input("Amount: $"))
            break
        except ValueError:
            print("Please enter a valid amount.")

    category = input("Category: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense saved successfully.")


def view_expenses(expenses):
    print("\nYour Expenses")

    if not expenses:
        print("No expenses added yet.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"\n{index}. {expense['title']}")
        print(f"Amount: ${expense['amount']}")
        print(f"Category: {expense['category']}")
        print(f"Date: {expense['date']}")


def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal spent: ${total:.2f}")


def category_summary(expenses):
    print("\nSpending by Category")

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    if not summary:
        print("No data available.")
        return

    for category, amount in summary.items():
        print(f"{category}: ${amount:.2f}")


def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses(expenses)
            print(f"Deleted: {removed['title']}")
        else:
            print("Expense number not found.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("Program closed.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()