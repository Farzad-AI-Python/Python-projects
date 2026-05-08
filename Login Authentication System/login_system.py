import json
import hashlib
import os
from datetime import datetime

USER_FILE = "users.json"


def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as file:
        return json.load(file)


def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    users = load_users()

    print("\n--- Create New Account ---")
    username = input("Enter username: ").strip()

    if username in users:
        print("Username already exists.")
        return

    password = input("Enter password: ").strip()
    confirm_password = input("Confirm password: ").strip()

    if password != confirm_password:
        print("Passwords do not match.")
        return

    if len(password) < 6:
        print("Password must be at least 6 characters.")
        return

    users[username] = {
        "password": hash_password(password),
        "failed_attempts": 0,
        "is_locked": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "last_login": None
    }

    save_users(users)
    print("Account created successfully.")


def login():
    users = load_users()

    print("\n--- Login ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username not in users:
        print("Account not found.")
        return

    if users[username]["is_locked"]:
        print("Account is locked due to too many failed login attempts.")
        return

    if users[username]["password"] == hash_password(password):
        users[username]["failed_attempts"] = 0
        users[username]["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_users(users)

        print(f"Login successful. Welcome, {username}!")
    else:
        users[username]["failed_attempts"] += 1

        if users[username]["failed_attempts"] >= 3:
            users[username]["is_locked"] = True
            print("Too many failed attempts. Account has been locked.")
        else:
            remaining = 3 - users[username]["failed_attempts"]
            print(f"Incorrect password. Attempts remaining: {remaining}")

        save_users(users)


def view_users():
    users = load_users()

    print("\n--- Registered Users ---")

    if not users:
        print("No users found.")
        return

    for username, info in users.items():
        print(f"\nUsername: {username}")
        print(f"Account Locked: {info['is_locked']}")
        print(f"Created At: {info['created_at']}")
        print(f"Last Login: {info['last_login']}")


def unlock_user():
    users = load_users()

    print("\n--- Unlock User Account ---")
    username = input("Enter username to unlock: ").strip()

    if username not in users:
        print("User not found.")
        return

    users[username]["is_locked"] = False
    users[username]["failed_attempts"] = 0
    save_users(users)

    print(f"{username}'s account has been unlocked.")


def main():
    while True:
        print("\n==============================")
        print(" LOGIN & AUTHENTICATION SYSTEM")
        print("==============================")
        print("1. Register")
        print("2. Login")
        print("3. View Users")
        print("4. Unlock User")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            view_users()
        elif choice == "4":
            unlock_user()
        elif choice == "5":
            print("Program closed.")
            break
        else:
            print("Invalid option. Please try again.")


main()