discription = input("Please enter the product description:")
print(discription)

amount =int(input("How many of item Black T-Shirt (XL) are being purchased?"))

price = float(input("What is the regular price?"))


if price  > 39.99:
  
    discount = price * 0.75
   
elif  price > 19.99:
  
    discount = price * 0.85
   

print(f"{discription} @ ${discount}")

salesTax = discount * 0.065
print(f"Sales Tax :${salesTax:.2f}" )


total = discount * amount + salesTax

print(f"Total amount due ${total:.2f}")

savings =(price - discount) * amount
print(f"You saved ${savings:.2f} today.")
