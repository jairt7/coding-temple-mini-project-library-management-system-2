class Author():
    def __init__(self):
        self.author_list = {}
    
    def add_author(self, name, bio):
        if name in self.author_list:
            print("Author already in list.")
            return
        self.author_list[name] = {}
        self.author_list[name]["name"] = name
        self.author_list[name]["bio"] = bio

    def search_author(self):
        if self.author_list:
            search_term = input("Enter the author you'd like to search for: ").title()
            match_found = False
            for author in self.author_list.values():
                if search_term in author.values():
                    match_found = True
                    print(f"Match found:\n{author["name"]}\nAuthor bio:\n{author["bio"]}")
            if not match_found:
                print("No matches found. Sorry.")
        else:
            print("No authors in the database. Sorry.")
    
    def display_authors(self):
        if self.author_list:
            for value in self.author_list.values():
                print(f"Author:\n{value["name"]}\nBio:\n{value["bio"]}\n\n")
        else:
            print("No books here!")
            return


def add_authors(authors):

    new_author = input("Enter the name of the author you'd like to add: ")
    new_bio = input(f"Enter a brief description of {new_author}: ")
    if new_bio == "":
        new_bio = "None"
    authors.add_author(new_author, new_bio)
