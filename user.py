import random

class User():
    def __init__(self):
        self.__user_list = {}
    
    def add_user(self, id, name, borrowed):
        if id in self.__user_list.values():
            print("User already exists.")
            return
        self.__user_list[id] = {}
        self.__user_list[id]["name"] = name
        self.__user_list[id]["ID"] = id
        self.__user_list[id]["borrowed books"] = borrowed
    
    def search_user(self):
        if self.__user_list:
            search_term = input("Enter the user you'd like to search for: ").title()
            match_found = False
            for __user in self.__user_list.values():
                if search_term in __user.values():
                    match_found = True
                    print(f"Match found:\n{__user["name"]}\nUser ID:\n{__user["ID"]}")
            if not match_found:
                print("No matches found. Sorry.")
        else:
            print("No users in the database. Sorry.")
    
    def display_users(self):
        if self.__user_list:
            for value in self.__user_list.values():
                print(f"\nUser:\n{value["name"]}\nID:\n{value["ID"]}\nBorrowed books: {value["borrowed books"]}")
        else:
            print("No users found.")
            return


def add_users(users):
    name = input("What is the new user's username? ")
    id_in_database = False
    while not id_in_database:
        id = random.randrange(111111,999999)
        if id not in users._User__user_list:
            id_in_database = True
    
    borrowed = []
    users.add_user(id, name, borrowed)