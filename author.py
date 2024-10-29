from connect_mysql import connect_database

def add_authors():

    new_author_name = input("Enter the name of the author you'd like to add: ").title()
    new_author_bio = input(f"Enter a brief description of {new_author_name}: ")
    if new_author_bio == "":
        new_author_bio = "None"
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            new_author = (new_author_name, new_author_bio)

            query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"

            cursor.execute(query, new_author)
            conn.commit()
            print("Author added successfully.")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Couldn't find the database.")

def search_authors():
    author = input("Enter the author you'd like to search for: ").title()
    author_search_term = "%" + author + "%"
    author_search = (author_search_term, )
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM authors WHERE name LIKE %s"

            cursor.execute(query, author_search)
            authors = cursor.fetchall()
            if not authors:
                print("No matches found.")
            for author in authors:
                print("Match found:")
                print(author)

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Couldn't find the database.")

def display_authors():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM authors"

            cursor.execute(query)
            
            for author in cursor.fetchall():
                print(author)

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()
    else:
        print("Couldn't find the database.")