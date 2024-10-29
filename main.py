# Menus
import book
import user
import author

def main_menu():
    print("Welcome to the Library Management System!")
    keep_going = True
    while keep_going:
        print("\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
        which_operation = input()
        if which_operation == "1":
            book_menu()
        elif which_operation == "2":
            user_menu()
        elif which_operation == "3":
            author_menu()
        elif which_operation == "4":
            keep_going = False
        else:
            print("Invalid input. Please enter a number from 1 to 4.")

def book_menu():
    print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
    which_operation = input()
    if which_operation == "1":
        book.add_books()
    elif which_operation == "2":
        book.borrow_books()
    elif which_operation == "3":
        book.return_books()
    elif which_operation == "4":
        book.search_books()
    elif which_operation == "5":
        book.display_books()
    else:
        print("Invalid input. Please enter a number from 1 to 5.")

def user_menu():
    print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users")
    which_operation = input()
    if which_operation == "1":
        user.add_users()
    elif which_operation == "2":
        user.search_users()
    elif which_operation == "3":
        user.display_all_users()
    else:
        print("Invalid input. Please enter a number from 1 to 3.")
def author_menu():
    print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors")
    which_operation = input()
    if which_operation == "1":
        author.add_authors()
    elif which_operation == "2":
        author.search_authors()
    elif which_operation == "3":
        author.display_authors()
    else:
        print("Invalid input. Please enter a number from 1 to 3.")

main_menu()