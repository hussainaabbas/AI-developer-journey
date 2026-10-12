print("****** Welcome to smart spending checker program ******")

budget = int(input("Enter available budget:"))
price = int(input("Enter the item price:"))
remaining = budget - price
print("Your remaining money is Rs", remaining)
if price > budget:
    print("Sorry!You cannot afford it")

elif budget==price:
    print("The entire budget will be spent.")

elif remaining < 20*budget/100:
    print("Warning: Very little money remains")

else:
    print("User will have enough money left.")

    print ("Your remaining money is Rs:", remaining)
print("******* Thanks for using smart spending checker program*******")





