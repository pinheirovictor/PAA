def sort1(alist):
    pivo = alist[1]
    i = 2
    j = n
    
    while(j < i):
        if alist[i] <= pivo:
            i = i + 1
        elif (l[j] > pivo):
            j = j + 1
        else:
            temp = alist[i]
            alist[i] = alist[j]
            alist[j] = temp
            i = i + 1
            j = j + 1
        temp = alist[j]
        alist[j] = alist[i]
        alist[i] = temp
        
        
alist = [3, 1, 5, 2, 10, 90]

sort1(alist)
    
print(alist)





         
