def bill(food,clothes,rent,electricity_bill):
    total_bill=food+clothes+rent+electricity_bill
    return total_bill

x=0
y=0
z=0
a=0
x=int(input("Enter the amount to be paid for food-"))
y=int(input("Enter the amount to be paid for clothes-"))
z=int(input("Enter the amount to be paid for rent-"))
a=int(input("Enter the amount to be paid for electricity bill-"))
print(bill(x,y,z,a))
    

