def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

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
    mergeSort(a)
    end = time.time()
    
    t = end - start
    if prev > 0: print(t / prev)
    
    prev = t
    N = 2*N