a=int(input("Enter a number-"))
b=0
while a>0:
    c=a%10
    b=b*10+c
    a=a//10
print(b)

