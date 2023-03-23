sub1= int(input("Subject 1 marks -"))
sub2= int(input("Subject 2 marks -"))
sub3= int(input("Subject 3 marks -"))
average = (sub1+sub2+sub3)//3
print(average)
if average>100 and average<=0:
    print("Wrong input")
else:
    if average>=90:
        print("Merit")
    elif average<90 and average>=60:
        print("A")
    elif average<60 and average>=50:
        print("B")
    elif average<50 and average>=40:
        print("C")
    else:
        print("F")
