def factorial():
    a= int(input("Enter the number to get factorial - "))
    fact=1
    
    for i in range(1,a+1):     
        fact=fact*i
    print(fact)   
    return
factorial()