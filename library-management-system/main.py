import json
import os

FILE_NAME = "books.json"


def load_books():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")

    book = {
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }

    books.append(book)
    save_books(books)

    print("Book added successfully.")


def view_books(books):
    if not books:
        print("No books found.")
        return

    print("\nLibrary Books:")
    for index, book in enumerate(books, start=1):
        status = "Available" if book["available"] else "Borrowed"
        print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {status}")


def search_book(books):
    keyword = input("Enter book title or author to search: ").lower()

    found = False

    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            status = "Available" if book["available"] else "Borrowed"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {status}")
            found = True

    if not found:
        print("No matching book found.")


def borrow_book(books):
    title = input("Enter the title of the book to borrow: ").lower()

    for book in books:
        if book["title"].lower() == title:
            if book["available"]:
                book["available"] = False
                save_books(books)
                print("Book borrowed successfully.")
            else:
                print("This book is already borrowed.")
            return

    print("Book not found.")


def return_book(books):
    title = input("Enter the title of the book to return: ").lower()

    for book in books:
        if book["title"].lower() == title:
            if not book["available"]:
                book["available"] = True
                save_books(books)
                print("Book returned successfully.")
            else:
                print("This book was not borrowed.")
            return

    print("Book not found.")


def delete_book(books):
    title = input("Enter the title of the book to delete: ").lower()

    for book in books:
        if book["title"].lower() == title:
            books.remove(book)
            save_books(books)
            print("Book deleted successfully.")
            return

    print("Book not found.")


def main():
    books = load_books()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            borrow_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            delete_book(books)
        elif choice == "7":
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please try again.")


main()