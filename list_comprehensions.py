countries_capitals = {
    "Nepal": "Kathmandu",
    "Australia": "Canberra",
    "Japan": "Tokyo",
    "Brazil": "Brasília",
    "Egypt": "Cairo"
}

# print(countries_capitals.get("Nepal"))

if countries_capitals.get("apple"):
    print("Capital exists.")
else:
    print("Capital doesnot exists.")