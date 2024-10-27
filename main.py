# Menus
import book
import user
import author

# books = book.Book()

# bible = books.add_book("Bible", "God", "Religion", "0", "available")
# harry_potter = books.add_book("Harry Potter", "J. K. Rowling", "Fantasy", "1997", "available")
# fsm_gospel = books.add_book("The Gospel of the Flying Spaghetti Monster", "Bobby Henderson", "Religion", "2006", "available")
# seven_habits = books.add_book("The 7 Habits of Highly Effective People", "Stephen R. Covey", "Self-help", "1989", "available")

# authors = author.Author()

# jkrowling = authors.add_author("J. K. Rowling", "Author of Harry Potter, one of the most successful book series of all time. \
# She was the first ever billionaire to lose her billionaire status by donating to charity.")
# god = authors.add_author("God", "An entity said to have created the universe and all within, with public opinion divided on the \
# legitimacy of His existence.")
# stephenrcovey = authors.add_author("Stephen R. Covey", "Creator of The 7 Habits of Highly Effective People, an extremely \
# successful self-help book.")
# bobbyhenderson = authors.add_author("Bobby Henderson", "Inventor of Pastafarianism, critic of intelligent design theory.")

# users = user.User()

# allanahmed = users.add_user(314159, "Allan Ahmed", [])
# jaredwilson = users.add_user(113113, "Jared Wilson", [])


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
        book.new_book(books)
    elif which_operation == "2":
        try:
            user_id = int(input("Enter user ID: "))
            if user_id not in users._User__user_list:
                raise Exception("Invalid user ID. Try again.")
            title = input("What book would you like to borrow? ").title()
            books.borrow_book(users, user_id, title)
        except Exception as e:
            print(f"An error occurred: {e}")
    elif which_operation == "3":
        title = input("Which book would you like to return? ")
        books.return_book(title)
    elif which_operation == "4":
        books.search_books()
    elif which_operation == "5":
        books.display_book()
    else:
        print("Invalid input. Please enter a number from 1 to 5.")

def user_menu():
    print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users")
    which_operation = input()
    if which_operation == "1":
        user.add_users()
    elif which_operation == "2":
        pass
    elif which_operation == "3":
        pass
    else:
        print("Invalid input. Please enter a number from 1 to 3.")
def author_menu():
    print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors")
    which_operation = input()
    if which_operation == "1":
        author.add_authors(authors)
    elif which_operation == "2":
        authors.search_author()
    elif which_operation == "3":
        authors.display_authors()
    else:
        print("Invalid input. Please enter a number from 1 to 3.")

main_menu()