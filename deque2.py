import random
import array

# I created a class called deque which peforms the operage add to the front of the array,add to the back of the array and remove from the front and remove from the back.
class Deque:
    #I set the array capacity to 20 
    Default_Capacity =20
    # Instantiate my Deque constracter to hold my instance varibles
    def __init__(self):
        self.data=[None]*Deque.Default_Capacity
        self.front=0
        self.size=0
        self.last=0
    # instatiated a length function to hold the size of the array.
    def __len__(self):
        return self.size
    # # Created an isEmpty function to know if track wjen the Array is empty
    def is_empty(self):
        return self.size ==0
    # Created the first function to dispay the first item in the array
    def first(self):

        if self.is_empty():
            raise Empty("Deque is Empty")
        return self.data[self.front]
    
    #  Created this function to remove an item from the first position of the array
    def remove_front(self):
        if self.is_empty():
            raise Empty(" Deque is empty")
        first_ans= self.data[self.front+1]
        self.data[self.front]=None
        self.front=(self.front+1)%len(self.data)
        self.size=self.size-1
        return first_ans

    # create this fuction to add element to the front index of the array

    def add_to_front(self,x):
        if self.size==len(self.data):
            self.resize(2* len(self.data))
        avail=(self.front+self.size) % len(self.data)
        self.data[avail]=x
        self.size=self.size+1
        return self.data
    # created the resize fuction to increase the size of the array incase the array becomes full
    def resize(self,cap):

        old=self.data
        self.data=[None]*cap
        walk=self.front
        for k in range(self.size):
            self.data[k]=old[walk]
            walk=(1+walk)%len(old)
        self.front=0
        
    # created a function to add to the back index of the array.
    def add_to_back(self,x):
        if self.size==len(self.data):
            self.resize(2*len(self.data))
        self.last=self.size-1
        avail=(self.last-self.size)%len(self.data)
        self.data[avail]=x
        self.size=self.size+1
        return self.data
    # created a fuction to remove an item from the back index of the array
    def remove_back(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        self.last=self.size
        last_ans=self.data[self.last-1]
        self.data[self.last]=None
        self.last=(self.last+1)%len(self.data)
        self.size=self.size-1
        return last_ans
    
    
    # create this function to return the size of the array
    def Size_array(self):
        return len(self.data)
    
    # create this function to return a display of the status of the array affter various insertions and deleations
    def status_array(self):
        
        status=""" Size_array: {}\nArray: {}
               """
        stat=status.format(self.size,self.data)
        return stat
    
# Here i instantiated my Deque class to store start the simulations on the array by using a random float to decide which operation take priority.   
kofi=Deque()
for emlement in range(0,10):
    x=random.randrange(1,100)
    print(kofi.add_to_front(x))
size=kofi.Size_array()
choice=[0.1,0.2,0.1,0.6]
for i in range(50):
    
    prob=random.choice(choice)
    if prob==0.1:
        print(kofi.add_to_front(random.randrange(1,100)))
        print()
        print(kofi.add_to_back(random.randrange(1,100)))
        print()
    elif prob==0.2:
        print(kofi.remove_front())
        print()
        print(kofi.remove_back())
        print()


            
        

    
