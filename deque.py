import numpy as np
from array import array
class deque:
    def __init__(self):
        self.capacity=5
        self.data=[None]
        self.size=len(self.data)
        self.f=0
        self.l=len(self.data)-1
        
    def add_to_front(self,item):
        if self.size<1:
            self.data[self.f]=item
            self.size=self.size+1
            #print(self.size)
        else:
            while self.l>=self.f:
                k=self.data[self.l]
                self.data=np.resize(self.data,self.size+1)
                self.data[self.l+1]=k
                self.l=self.l-1
            self.l=len(self.data)-1
            self.data[self.f]=item
            self.size=self.size+1
        return self.data, self.size
    
    def add_to_back(self,item):
        self.data=array.resize(self.data,self.size+1)
        self.data[self.l+1]=item
        self.size=self.size+1
        return self.data,self.size
    
    def remove_from_front(self):
        if self.size==1:
            self.data=[]
        else:
            while self.f<=self.l:
                self.data[self.f]=self.data[self.f+1]
                self.f=self.f+1
            self.size=self.size-1
        return self.data
            
        
    def remove_from_back(self,item):
        
    
kofi=deque()
kofi.add_to_front(2)
kofi.add_to_front(4)
kofi.add_to_front(5)
kofi.add_to_front(8)
##kofi.add_to_front(7)
#print(kofi.add_to_back(4))
print(kofi.remove_from_front())



        
                
            
            
        