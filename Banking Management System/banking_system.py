import json
import os
from datetime import datetime

DATA_FILE = "bank_accounts.json"


def load_accounts():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_accounts(accounts):
    with open(DATA_FILE, "w") as file:
        json.dump(accounts, file, indent=4)


def create_account():
    accounts = load_accounts()

    print("\n--- Create Bank Account ---")
    account_number = input("Enter account number: ").strip()

    if account_number in accounts:
        print("Account already exists.")
        return

    name = input("Enter account holder name: ").strip()
    initial_deposit = float(input("Enter initial deposit amount: "))

    if initial_deposit < 0:
        print("Initial deposit cannot be negative.")
        return

    accounts[account_number] = {
        "name": name,
        "balance": initial_deposit,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "transactions": [
            {
                "type": "Initial Deposit",
                "amount": initial_deposit,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        ]
    }

    save_accounts(accounts)
    print("Bank account created successfully.")


def deposit_money():
    accounts = load_accounts()

    print("\n--- Deposit Money ---")
    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter deposit amount: "))

    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return

    accounts[account_number]["balance"] += amount
    accounts[account_number]["transactions"].append({
        "type": "Deposit",
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_accounts(accounts)
    print("Deposit successful.")


def withdraw_money():
    accounts = load_accounts()

    print("\n--- Withdraw Money ---")
    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
        return

    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
        return

    accounts[account_number]["balance"] -= amount
    accounts[account_number]["transactions"].append({
        "type": "Withdrawal",
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_accounts(accounts)
    print("Withdrawal successful.")


def check_balance():
    accounts = load_accounts()

    print("\n--- Check Balance ---")
    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("Account not found.")
        return

    account = accounts[account_number]
    print(f"Account Holder: {account['name']}")
    print(f"Current Balance: ${account['balance']:.2f}")


def transfer_money():
    accounts = load_accounts()

    print("\n--- Transfer Money ---")
    sender = input("Enter sender account number: ").strip()
    receiver = input("Enter receiver account number: ").strip()

    if sender not in accounts:
        print("Sender account not found.")
        return

    if receiver not in accounts:
        print("Receiver account not found.")
        return

    amount = float(input("Enter transfer amount: "))

    if amount <= 0:
        print("Transfer amount must be greater than zero.")
        return

    if amount > accounts[sender]["balance"]:
        print("Insufficient balance.")
        return

    accounts[sender]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    accounts[sender]["transactions"].append({
        "type": "Transfer Sent",
        "amount": amount,
        "to": receiver,
        "date": date
    })

    accounts[receiver]["transactions"].append({
        "type": "Transfer Received",
        "amount": amount,
        "from": sender,
        "date": date
    })

    save_accounts(accounts)
    print("Transfer successful.")


def view_transaction_history():
    accounts = load_accounts()

    print("\n--- Transaction History ---")
    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("Account not found.")
        return

    transactions = accounts[account_number]["transactions"]

    if not transactions:
        print("No transactions found.")
        return

    for transaction in transactions:
        print("\n--------------------")
        for key, value in transaction.items():
            print(f"{key.capitalize()}: {value}")


def view_all_accounts():
    accounts = load_accounts()

    print("\n--- All Bank Accounts ---")

    if not accounts:
        print("No accounts found.")
        return

    for account_number, account in accounts.items():
        print("\n--------------------")
        print(f"Account Number: {account_number}")
        print(f"Name: {account['name']}")
        print(f"Balance: ${account['balance']:.2f}")
        print(f"Created At: {account['created_at']}")


def main():
    while True:
        print("\n==============================")
        print(" BANKING MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. View Transaction History")
        print("7. View All Accounts")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transfer_money()
        elif choice == "6":
            view_transaction_history()
        elif choice == "7":
            view_all_accounts()
        elif choice == "8":
            print("Program closed.")
            break
        else:
            print("Invalid option. Please try again.")


main()