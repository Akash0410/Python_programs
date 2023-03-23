#create an empty list
import sys
def e_list(lst):
    print("Capacity:",(sys.getsizeof(lst)-36)//4)
    print("Size:",len(lst))
    print("Space left:",((sys.getsizeof(lst)-36)-len(lst*4))//4)
    return print(lst)
    

em_list=[]
#e_list(em_list)
em_list.append('Sugar')
em_list.append('Tea Bag')
em_list.append('Milk')
em_list.append('Biscuit')
em_list.insert(1,'Salt')
e_list(em_list)
em_list.pop(2)
e_list(em_list)
