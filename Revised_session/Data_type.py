# list: Collection of data of different types, Placed in square bracket.
# Allow duplicate values 

list = [1,3,5,6,9,20,15,12,7]

# concatination

list = list + [22,56,65,69,99]
print(list)

# Replacing value of list

list[0]= 11
print(list)

# Append 

list.append(72)
print(list)

color = ["red","blue", "yellow", "green", "purple"]
color.append("orange")
print(color)

# Shallow copy : copies the container

color[-1] = "Orange"
print(color)

color[1:3] = ["apple", "banana"]
print(color)

color[1:3] = []
print(color)

#  len()
print(len(list))

# Dictionary (dict) : It stores data in key-value pairs.
# dict_name = {key1:value1, key2:value2}
# key must be unique
# Mutable(can be changed)

student = {
    "name":"Bishal Shrestha",
    "age":20,
    "course":"Python"
}

print(student)
print(student["name"],student["age"])

# Tuple: Collection of items that cannot be changed(immutable)
# tuple_name = (value1, value2, value3)

numbers = (1,5,3,8,9,7)
print(numbers)

# Set
# set is a colletion of unique elements.
# set_name = {value1, value2, value3}
# No duplicate values, Duplicates are removed automatically.

color = {1,2,2,2,9,4,9,6,7,8}
print(color)