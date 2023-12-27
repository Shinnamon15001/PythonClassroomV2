again = "y"

while again == "y":
    wholesale_cost = float(input("Enter the item's wholesale cost: "))
    retail_price = float(wholesale_cost) * 2.5
    print("retail price is : ","%.2f" % retail_price)
    again = input("Do you have another item? (y/n) : ")
    