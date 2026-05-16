Shoes = []
Bicycles = []
 
# Price_1 = []    # Shoes
# Price_2 = []    # Bicycle
Prices = []     

# Total_1 = 0     # Total for shoe prices
# Total_2 = 0     # Total for Bicycle prices
Total = 0

while True:
    Shoe = input("Enter the name of shoe:")
    if Shoe.lower() == "q" :
        break    
     
    else :
        Price = float(input(f"Enter the price of {Shoe}: $"))
   

    Bicycle = input("Enter the name of Bicycle:")
    if Bicycle.lower() == "q" :    
        break

    else :
        Price = float(input(f"Enter the price of {Bicycle}: $"))
        Shoes.append(Shoe)
        Bicycles.append(Bicycle)
        Prices.append(Price)

print(Shoes)
print(Bicycles)
        

print("-----CART----")

for i in Shoes:
    print(i, end=" ")   # As default end is like end="\n" 

print()

# for total prices of Shoes only
# for a in Price_1:
#     Total_1 += a

for j in Bicycles:
    print(j, end=" ")
   
# for total prices of Bicycle only
# for a in Price_1:
#     Total_1 += a

for price in Prices :
    Total += price

print()
print(f"Your Total is ${Total}")