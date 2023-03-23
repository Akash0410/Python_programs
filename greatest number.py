x=int(input("Enter First Number-"))
y=int(input("Enter second Number-"))
z=int(input("Enter third Number-"))
if x>=y:
    if x>=z:
        print(x)
    else:
        print(z)
else:
    if y>=z:
        print(y)
    else:
        print(z)