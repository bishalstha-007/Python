def Add_book():
    name = input("Enter name of book:")
    author = input("Enter author name:")
    with open("file1.txt", "a") as f:
        f.write(name + "," + author + "\n")
    print("Record are Stored!!")

def View_book():
    try:
        with open("file1.txt", "r") as f:
            print("\n ---Book Records--- ")
            for line in f:
                name, author = line.strip().split(",")
                print("Name \t\t\t Author")
                print(name, "\t\t", author)

    except FileNotFoundError:
        print("No records found!!!")

def main():
    while True :
        print("7. To Add Books")
        print("8. To View Books")
        print("9. Exit")
        choice = input("\nEnter your choice:")

        if choice == "7":
            Add_book()
        elif choice == "8":
            View_book()
        elif choice == "9":
            print("Exiting Program....")
            break
        else:
            print("\nInvalid choice, choose between 7 - 9.\n")


main()