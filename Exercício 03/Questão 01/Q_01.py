import time
import random

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


random.seed(123456789)
N = int(input("\n"))
a = []

for _ in range (N):
    a.append(random.choice(range(1000)))
random.shuffle(a)

start = time.time()
bubbleSort(a)
end = time.time()

print(end - start)
