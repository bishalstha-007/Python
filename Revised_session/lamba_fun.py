# lambda : small anonymous function. 
# syntax
# lambda arguments : expression
# a, b, x, y are arguments.

# normal function
# x = 42
# y = 22
# def add(x, y) :
#     return x+y
# print(add(x,y))

# lambda function
x = lambda a, b : a+b
print(x(4,7))

# lambda with built-in functions
# map()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
doubled = list(map(lambda x: x*2 , numbers))
print(doubled)

# filter() : 
odd = list(filter(lambda x:x % 2 !=0, numbers))
print( "Odd numbers between 1 to 8:" ,odd)

# sorted() : for custom sorting
students = [("Bishal", 25), ("Charles", 22), ("Lina", 28),("Tina", 32), ("Amisha", 21), ("Bhumi",23)]
sorted_student = sorted(students, key=lambda x: x[1]) 
print(sorted_student)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key= lambda x: len(x))
print(sorted_words)