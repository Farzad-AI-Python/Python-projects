from cryptography.fernet import Fernet
import os


KEY_FILE = "secret.key"


def generate_key():
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

    print("Encryption key generated successfully.")


def load_key():
    if not os.path.exists(KEY_FILE):
        print("Key file not found. Generate a key first.")
        return None

    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def encrypt_file():
    key = load_key()

    if key is None:
        return

    cipher = Fernet(key)

    filename = input("Enter file name to encrypt: ").strip()

    if not os.path.exists(filename):
        print("File not found.")
        return

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = cipher.encrypt(file_data)

    encrypted_filename = filename + ".encrypted"

    with open(encrypted_filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File encrypted successfully: {encrypted_filename}")


def decrypt_file():
    key = load_key()

    if key is None:
        return

    cipher = Fernet(key)

    filename = input("Enter encrypted file name: ").strip()

    if not os.path.exists(filename):
        print("Encrypted file not found.")
        return

    with open(filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    decrypted_filename = "decrypted_" + filename.replace(".encrypted", "")

    with open(decrypted_filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"File decrypted successfully: {decrypted_filename}")


def main():
    while True:
        print("\n==============================")
        print(" FILE ENCRYPTION TOOL")
        print("==============================")
        print("1. Generate Encryption Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            generate_key()

        elif choice == "2":
            encrypt_file()

        elif choice == "3":
            decrypt_file()

        elif choice == "4":
            print("Program closed.")
            break

        else:
            print("Invalid option. Try again.")


main()