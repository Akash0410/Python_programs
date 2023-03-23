class combination():
    def __init__(self,a,b,fact1,fact2,fact3):
        self.n=a
        self.r=b
        self.x=fact1
        self.y=fact2
        self.z=fact3
        
    def comb(self):
        '''fact1=1
        fact2=1
        fact3=1'''
        for i in range(1,(self.n)+1): 
            self.x=self.x*i 
        for i in range(1,(self.r)+1):
            self.y=self.y*i
        for i in range(1,(self.n-self.r)+1):
            self.z=self.z*i
        
        print(self.x/(self.y*self.z))
        return
class permutation(combination):
    def __init__(self,a,b,fact1,fact3,fact2=None):
        super().__init__(a,b,fact1,fact2,fact3)
        
        
x1=permutation(8,3,1,1)
x1.comb()

    
        