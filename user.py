from connect_mysql import connect_database

def add_users():
    name = input("What is the new user's name? ")
    library_id = input("Which library does this user belong to? ")
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            new_user = (name, library_id)

            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"

            cursor.execute(query, new_user)
            conn.commit()
            print("User added successfully.")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Couldn't find the database.")

def search_users():
    user = input("Enter the user you'd like to search for: ")
    user = (user, user)
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM users WHERE name = %s OR library_id = %s"

            cursor.execute(query, user)
            users = cursor.fetchall()
            if not users:
                print("No matches found.")
            for user in users:
                print("Match found:")
                print(user)

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Couldn't find the database.")

def display_all_users():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM users"

            cursor.execute(query)

            for user in cursor.fetchall():
                print(user)

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()
    else:
        print("Couldn't find the database.")