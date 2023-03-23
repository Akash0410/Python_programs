def fabonacci():
    a=0
    b=1
    n=int(input("Enter the number upto which you want to calculate series - "))
    for i in range(0,n):
        print(b)
        c=a+b
        a=b
        b=c
       
    return 
fabonacci()