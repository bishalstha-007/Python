# Student record system with file handling.
def new_student():          # Function to enter the details of new student.
    name = input("Enter name of Student:")
    marks = input("Enter obtained marks:")
    with open("newfile.txt", "a") as f:      # append mode
        f.write(name + "," + marks + "\n")
    print("Student record added successfully!!")

def view_students():        # To view student details.
# Error handling.
    try:
        with open("newfile.txt", "r") as f:     # read mode
            print("\n--- Student Records ---")
            for line in f:      # Reads one line at a time.
                name,marks = line.strip().split(",")
# line.strip() -> Removes the newline character(\n)
# .split() -> Splits the data into name and marks.

                print("Name:", name , "| Marks", marks)

    except FileNotFoundError:           # Runs only if newfile.txt doesnot exist.
        print("No records found. Please add student first.")

def main():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter your choice:")

        if choice == "1":
            new_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Existing program....")
            break
        else:
            print("Invalid choice, Try again!!")

# Run the progrm.
main()