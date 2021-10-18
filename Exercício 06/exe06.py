from UnionFind import UnionFind

def fusao(L, B):
    U = UnionFind()
    for b in B:
        U.add(b)
    for l in L:
        t, c1, c2 = 1
        if(t == 'C'):
            if(U.connected(c1, c2)):
                print("S")
            else:
                  print("N")
        elif(t == 'F'):
            U.union(c1, c2)
            
