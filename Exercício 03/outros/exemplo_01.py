
def soma_tres (a):
    n = len(a)
    cont = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1,n):
                if a[i] + a[j] + a[k] == 0:
                    cont+=1
    return cont

import random
import time
import sys


random.seed(123456)
N = int(input("\n"))
print(N, end='\t')
a = [random.randint(-N, N) for i in range(N)]

start = time.time()
soma_tres(a)

end = time.time()
print(end - start)