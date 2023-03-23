a= input("enter a binery number  \n")
z = 65
b = ""

for i in range(len(a)):
    if a[i] == "0":
        b = b+" "
    else:
        b = b+(chr(z))
        z+=1
print(b)
