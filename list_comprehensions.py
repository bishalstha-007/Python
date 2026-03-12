# provides a concise way to create lists.
# short and concise

# creating list of square from 1 to 5
squares = [i**2 for i in range(10)]
print(squares)

# Only even squares

even = [i**2 for i in range(1,11) if i%2 == 0]
print(even)