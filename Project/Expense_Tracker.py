def add_expense():
    item = input("Enter expense item:")
    amount = float(input("Enter amount:"))

    with open("expense.txt", 'a') as f:
        f.write(item + "," + str(amount) + "\n")

    print("Expense Added Successfully.")

def view_expenses():
    try:
        with open("expense.txt", "r") as f:

            expenses = f.readlines()
            if len(expenses) == 0:
                print("No expense found.")
                return
            print("\nITEM\t\tAMOUNT")
            print("-"* 35)

            for expense in expenses:
                item, amount = expense.strip().split(",")
                print(f"{item:<20}Rs.{amount}")     # Left-aligh and reserve 15 character space for it.
            # <  = Left align
            # >  = Right align
            # ^  = Center align

    except FileNotFoundError:
        print("No expense records found.")

def total_expense():
    total = 0

    try:
        with open("expense.txt", "r") as f:

            for expense in f:
                item, amount = expense.strip().split(",")

                total += float(amount)
        print(f"\nTotal expense = Rs.{total}")
    
    except FileNotFoundError:
        print("No expense records found.")


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expense")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")