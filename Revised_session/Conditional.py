# Control flow : Determines how a program executes instruction based on conditions and loops.

# if / elif / else
# Used to make decisions in a program.

# Can vote or not
# age = 21
# if age>=18  :
#     print("You can vote")
# else :
#     print("You can't vote") 
  

# Grade determination
   
# marks = 75
# if marks>= 90:
#     print("Grade A")
# elif marks>= 70:
#     print("Grade B")
# elif marks>= 50:
#     print("Grade C")
# else :
#     print("Fail")

# Program to print the days of week and check odd/even.

# Taking input from user
x = int(input("Enter the number between 1-7:"))

# list of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday"]

if (1 <= x <= 7):
    print("Days:", days[x-1]) 

    if (x % 2 == 0):
        print("This is even day.")
    else:
        print("This is odd day.")
else:
    print("Invalid input, please enter the number between 1 - 7")