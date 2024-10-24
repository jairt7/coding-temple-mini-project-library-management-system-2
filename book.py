import user
class Book():
    def __init__(self):
        self.library = {}

    def add_book(self, title, author, genre, pub_date, available):
        self.library[title] = {}
        self.library[title]["title"] = title
        self.library[title]["author"] = author
        self.library[title]["genre"] = genre
        self.library[title]["pub_date"] = pub_date
        self.library[title]["available"] = available


    def update_availability(self, available):
        self.available = available

    def borrow_book(self, users, user_id, title):
        try:
            if title in self.library:
                if self.library[title]["available"] == "available":
                    self.library[title]["available"] = "borrowed"
                    users._User__user_list[user_id]["borrowed books"].append(title)
                    print(f"{title} borrowed.")
                else:
                    print(f"{title} has been borrowed. Sorry.")
            else:
                print(f"{title} not found.")
        except TypeError:
            print("Invalid input. Please enter a six-digit number corresponding to a user.")
        except ValueError:
            print("Invalid input. Please enter a six-digit number corresponding to a user.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def return_book(self, title):
        if title in self.library:
            if self.library[title]["available"] == "borrowed":
                self.library[title]["available"] = "available"
                print("Book returned.")
            else:
                print("Looks like that was already returned.")
        else:
            print("Title not found. Are you sure you borrowed it from this library?")

    def search_books(self):
        if self.library:
            search_term = input("Enter your search term: ").title()
            match_found = False
            for book in self.library.values():
                if search_term in book.values():
                    match_found = True
                    print(f"Match found: {book["title"]}")
            if not match_found:
                print("No matches found. Sorry.")
        else:
            print("No books in the library right now.")

    def display_book(self):
        if self.library:
            for value in self.library.values():
                print(f"Title: {value['title']}, Author: {value['author']}, Genre: {value['genre']}, Published on {value['pub_date']}, \
is {value['available']}")
        else:
            print("No books here!")
            return
        

def new_book(books):
    title = input("What is the title of the book? ").title()
    if title in books.library:
        print("That book is already in the library.")
        return
    author = input("Who is the author of the book? ").title()
    genre = input("What is the genre of the book? ").title()
    if genre == "":
        genre = "General"
    try:
        pub_date = int(input("What year was the book published? "))
    except ValueError:
        print("Doesn't look like you entered a year. Please try again.")
        return
    available = "available"
    books.add_book(title, author, genre, pub_date, available)