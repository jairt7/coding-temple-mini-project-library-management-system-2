import datetime
from connect_mysql import connect_database

def title_in_library(title):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM books WHERE title = %s"

            title = (title, )

            cursor.execute(query, title)
            books = cursor.fetchall()
            if books:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Couldn't find the database.")


def user_in_library(id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM users WHERE id = %s"

            id = (id, )

            cursor.execute(query, id)
            user = cursor.fetchall()
            if user:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Couldn't find the database.")


def id_in_authors(id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM authors WHERE id = %s"

            id = (id, )

            cursor.execute(query, id)
            id_exists = cursor.fetchall()
            if id_exists:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Couldn't find the database.")

def add_books():
    title = input("What is the title of the book? ")
    title_exists = title_in_library(title)
    if title_exists:
        print("That title is already in the library.")
        return
    try:
        id = int(input("Enter the author ID: "))
    except ValueError:
        print("That's not a number. Please enter a number.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return
    id_exists = id_in_authors(id)
    if not id_exists:
        print("Author ID not found in author database.")
        return
    try:
        isbn = int(input("Enter the ISBN (13 digits): "))
    except ValueError:
        print("That's not a number. Enter a number, please.")
        return
    pub_date = input("Enter the date of publication (format YYYY-MM-DD): ")
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)"

            book_info = (title, id, isbn, pub_date)

            cursor.execute(query, book_info)
            conn.commit()
            print("Book added.")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Couldn't find the database.")

def search_books():
    book = input("Enter the book you'd like to search for: ").title()
    book_search_term = "%" + book + "%"
    book_search = (book_search_term, )
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM books WHERE title LIKE %s"

            cursor.execute(query, book_search)
            books = cursor.fetchall()
            if not books:
                print("No books in the library.")
            for book in books:
                print("Match found:")
                print(book)

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Couldn't find the database.")

def display_books():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM books"

            cursor.execute(query)
            
            books = cursor.fetchall()
            if not books:
                print("The library is empty.")
                return
            
            for book in books:
                print(book)

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()
    else:
        print("Couldn't find the database.")

def borrow_books():
    try:
        user_id = int(input("Please enter your library user ID: "))
    except ValueError:
        print("That's not a number. Please enter a number.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return
    
    user_exists = user_in_library(user_id)
    if not user_exists:
        print("Couldn't find a user with that ID. Try again.")
        return
    
    which_book = input("Which book would you like to borrow? Please enter the book title: ").title()
    
    book_exists = title_in_library(which_book)
    if not book_exists:
        print("Couldn't find that book. Sorry.")
        return

    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query1 = "SELECT id, availability FROM books WHERE title = %s"
            book_title = (which_book, )
            cursor.execute(query1, book_title)
            book_data = cursor.fetchone()

            if book_data is None:
                print("Book ID not found.")
                return

            book_id, availability = book_data
            if availability == 0:
                print("This book has already been borrowed. Sorry.")
                return

            query2 = "UPDATE books SET availability = 0 WHERE id = %s"

            cursor.execute(query2, (book_id,),)

            today = datetime.datetime.now()
            today = today.date()

            query3 = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"

            borrow_book = (user_id, book_id, today)

            cursor.execute(query3, borrow_book)
            conn.commit()
            print("Book borrowed successfully.")
        
        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()
    else:
        print("Couldn't find the database.")

def return_books():
    try:
        user_id = int(input("Please enter your library user ID: "))
    except ValueError:
        print("That's not a number. Please enter a number.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return
    
    user_exists = user_in_library(user_id)
    if not user_exists:
        print("Couldn't find a user with that ID. Try again.")
        return
    
    which_book = input("Which book would you like to return? Please enter the book title: ").title()
    
    book_exists = title_in_library(which_book)
    if not book_exists:
        print("Couldn't find that book. Sorry.")
        return
    
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query1 = "SELECT id, availability FROM books WHERE title = %s"
            book_title = (which_book, )
            cursor.execute(query1, book_title)
            book_data = cursor.fetchone()

            if book_data is None:
                print("Book ID not found.")
                return

            book_id, availability = book_data
            if availability == 1:
                print("This book is already available.")
                return

            query2 = "UPDATE books SET availability = 1 WHERE id = %s"

            cursor.execute(query2, (book_id,),)

            query3 = "UPDATE borrowed_books SET return_date = %s WHERE book_id = %s"

            today = datetime.datetime.now()
            today = today.date()

            book_data_2 = (today, book_id)

            cursor.execute(query3, book_data_2)
            conn.commit()
        
        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()
