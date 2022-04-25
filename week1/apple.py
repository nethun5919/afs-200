applePrice = float(0.5)
# checking varible is a float and not a integer
print(type(applePrice))

name= input("Please enter your name:")

itemQuanity= input(f"Hi {name}.  Apples cost ${applePrice:.2f} each.  How many would you like to buy?")
print(f"Thank you {name} for your purchase of {itemQuanity} apples at a cost of ${applePrice:.2f} each.")
