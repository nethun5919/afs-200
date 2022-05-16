

num =0
while (num==0):
 
    description = input("Please enter a positive number:")
    print(description)
    if(description.isdigit()):
        num= int(description)
    else:
        print("Please try again")

for n in range(0,num+1):
    if  n %2 == 0:
        print(n)