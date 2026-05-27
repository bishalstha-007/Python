# countries_capitals = {
#     "Nepal": "Kathmandu",
#     "Australia": "Canberra",
#     "Japan": "Tokyo",
#     "Brazil": "Brasília",
#     "Egypt": "Cairo"
# }

# print(countries_capitals.get("Nepal"))

# if countries_capitals.get("apple"):
#     print("Capital exists.")
# else:
#     print("Capital doesnot exists.")

# CONCESSION STAND PROGRAM

menu = {
    "pizza" : 4,
    "popcorn": 5,
    "soda": 3,
    "candy": 2,
    "hotdog": 4,
    "nachos": 6,
    "Sticker" : 0.5
}

cart = []
total = 0

print("Welcome to concession stand:")
print("Here's our Menu:")
print("=====================")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("=====================")

while True:
    order = input("Your order please(q to quit): ").lower()
    if order == "q":
        break
    elif order in menu:
        cart.append(order)
    else:
        print(f"{order} not in the menu")


for order in cart:
    total += menu.get(order)
    print(order, end=" ")


print()
print(f"Total is: ${total:.2f}")