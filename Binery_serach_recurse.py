from array import array
import math
import random
# According to the question we were supposed to use the python inbuilt sort function so that is what i used.
#import Merge_sort
import time

def binary_search(Arr, target,low,high):
    
    if low>high:
        return False
    else:
        pos=(low+high)/2
        pos=math.ceil(pos)
        if target == Arr[pos]:
            return True
        elif target < Arr[pos]:
            return binary_search(Arr,target,low,pos-1)
        else:
            return binary_search(Arr,target,pos+1,high)
        
    
    
def Interpolation_search(Arr,target,low,high):
    found=True
    if low>high:
        return not found
    else:
        pos=math.ceil(low+((high-low)*(target-Arr[low])/(Arr[high]-Arr[low])))
        print(pos)
        if target is not found:
            return not found
        if target==Arr[pos]:
            found=True
            return found
        elif target< Arr[pos]:
            return Interpolation_search(Arr,target,low,pos-1)
        
        else:
            return Interpolation_search(Arr,target,pos+1,high)


def main(N):
    Arr=[]
    target=0
    for i in range(N):
        Arr.append(random.randrange(1,132767))
        
    
    #Merge_sort.merge_SortV2(Arr)
    Arr.sort()
    print(" The time taken todo a comparative binary search is: ") 
    Total_time=0
    for element in range (5):
        target=random.randrange(1,132767)
        print(" The target figure is",target)
        start=time.time()
        print()
        print(binary_search(Arr,target,0,N-1))
        end=time.time()
        Time_take=end-start
        
        Total_time=Total_time+Time_take
    Average1=Total_time/5
    print(Average1)
    
    Total_take2=0
    print(Arr)
    for element in range(5):
        target=random.randrange(1,132767)
        print("The target is " ,target)
        start=time.time()
        print(Interpolation_search(Arr,target,0,N-1))
        end=time.time()
        Time_take2=end-start
        Total_take2=Total_take2+Time_take2
    Average2=Total_take2/5
    print(Average2)
    return Average1,Average2
    
def comparative_table():
    Average1,Average2=main(10000)
    Av1=Average1
    Av2=Average2
    Average1,Average2=main(100000)
    Av3=Average1
    Av4=Average2
    Average1,Average2=main(500000)
    Av5=Average1
    Av6=Average2
    xomp_table="""      Binary Search             Interpolation Search
100  {}        {}
1000 {}        {}
5000 {}        {}                   """
    print(xomp_table.format(Av1,Av2,Av3,Av4,Av5,Av6))
comparative_table()
        
   
    
