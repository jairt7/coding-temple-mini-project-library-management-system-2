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