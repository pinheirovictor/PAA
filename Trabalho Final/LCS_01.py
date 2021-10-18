import time
import numpy as np

#recursivo
def lcs(X, Y, m, n):
    if m==0 or n==0:
        return 0
    elif X[m-1] == Y[n-1]:
        return lcs(X, Y, m-1, n-1) + 1
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))


V = ["A","T","C","G"]
X = ""
Y = ""
tamanho = 20
for i in range(tamanho + 1):
    X = X + V[np.random.choice([0,1,2,3])]

for i in range(tamanho):
    Y = Y + V[np.random.choice([0,1,2,3])]

n = len(Y)
m = len(X)


print(X)
print(Y)


start = time.time()
lcs(X, Y, m, n)
end = time.time()


print(end - start)
