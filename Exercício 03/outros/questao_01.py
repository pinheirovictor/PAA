import time

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
alist = [54,26,93,17,77,31,44,55,20]

start = time.time()
bubbleSort(alist)

end = time.time()
print(end-start)

============================================


                
                
def sort1(alist):
    i = 0
    j = 0
    while(i <= j):
        if(alist[1] >= alist[i]):
            temp = alist[1]
            alist[1] = alist[i]
            alist[i] = temp
            i = i + 1
        
        if (alist[1] <= alist[j]):
            twmp = alist[1]
            alist[1] = alist[j]
            alist[j] = temp
            j = j + 1
    
        
    

alist = [3, 1, 5, 2]

sort1(alist)
    
print(alist)
         
