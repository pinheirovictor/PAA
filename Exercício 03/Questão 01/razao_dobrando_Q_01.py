def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

import random
import time
import sys


N = 800
prev = 0
while True:
    a = []
    for _ in range (N):
        a.append(random.choice(range(1000)))
    random.shuffle(a)

    start = time.time()
    bubbleSort(a)
    end = time.time()
    
    t = end - start
    if prev > 0: print(t / prev)
    
    prev = t
    N = 2*N