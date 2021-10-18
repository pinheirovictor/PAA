
#recursivo
def lcs(X, Y, m, n):
    if m==0 or n==0:
        return 0
    elif X[m-1] == Y[n-1]:
        return lcs(X, Y, m-1, n-1) + 1
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))



#programação dinamica
def lcs_pd(X, Y, m, n):
    L1 = [[0]*(n + 1) for i in range(m + 1)]
  
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L1[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L1[i][j] = L1[i-1][j-1]+1
            else:
                L1[i][j] = max(L1[i-1][j], L1[i][j-1])
  
    return L1[m][n]

X = "GTHGTGTTTT"
Y = "GHHHHHTGHTHTHTHTHTHTHTHTHTHTHTHHTHTHTHTHTHHTHHTHTHTHTHTHTHTHTHTHHHHTTTTHHT"
n = len(Y)
m = len(X)

print(lcs_pd(X, Y, m, n))