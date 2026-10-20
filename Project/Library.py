def add_book():
    name = input("Enter book name:")
    author =  input("Enter author name:")

    with open("library.txt", "a") as f:
        f.write(name + "," + author + "\n")

    print("Book added successfully.")

def view_books():
    try:
        with open("library.txt", "r") as f:

            books = f.readlines()            # Reads all the lines from a file and returns in list
            if len (books) == 0:
                print("No books available.")
                return

            print("\nBook Name\t\tAuthor")
            print("-"*40)

            for book in books:
                name, author = book.strip().split(",")
                print(f"{name:<20}{author}")

    except FileNotFoundError:
        print("No books available.")

def search_book():
    search = input("Enter book name to search:")

    found = False

    try:
        with open("library.txt", "r") as f:

            for book in f:
                name, author = book.strip().split(",")

# We can search from both book name and author.
                if search.lower() == name.lower()  or search.lower() == author.lower():
                    print("\nBook found!!")
                    print("Book Namme:", name)
                    print("Book Author:", author)

                    found = True
                    break

        if not found:
            print("Book not found..")

    except FileNotFoundError:
        print("Library is empty.")

while True:
    print("\n-----LIBRARY MANAGEMENT SYSTEM-----")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        print("Thank You!!")
        break

    else:
        print("Invalid choice, Please Try Again!!")
