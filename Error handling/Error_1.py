# This code produces error when we give 0 as input value.
# number = int(input("Enter the number:"))
# print(10 / number)

# Code with error handling.

try:
    number = int(input("Enter the number:"))
    answer = 10 / number
except ValueError:
    print("Please enter a whole number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(answer)
