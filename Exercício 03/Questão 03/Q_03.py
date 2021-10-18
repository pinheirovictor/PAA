import time
import random

def recursivo(n):
    if(n <= 1):
        return 1
    else:
        return recursivo(n-1) + recursivo(n-1)
   


N = int(input("\n"))

start = time.time()
recursivo(N)
end = time.time()

#print(a)

print(end-start)