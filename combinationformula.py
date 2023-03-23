class p_and_c():
    def combination():
        n=int(input("Enter the value of n - "))
        r=int(input("Enter the value of r- "))
        fact1=1
        fact2=1
        fact3=1
        for i in range(1,n+1):
            fact1=fact1*i
        for i in range(1,r+1):
            fact2=fact2*i
        for i in range(1,(n-r)+1):
            fact3=fact3*i
        print('Value of nCr -',fact1/(fact2*fact3))
        return
    def permutaion():
        n=int(input("Enter the value of n - "))
        r=int(input("Enter the value of r- "))
        fact1=1
        fact2=1
        for i in range(1,n+1):
            fact1=fact1*i
        for i in range(1,(n-r)+1):
            fact2=fact2*i
        print('value of nPr',fact1/fact2)
        return
        

p_and_c.combination()
