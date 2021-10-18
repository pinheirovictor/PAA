def get_canditado_a_majoritario(V,cont):
    n = len(V)
    if(n == 1):
        return V[0], cont+1
    
    meio = n//2
    l,c1 = get_canditado_a_majoritario(V[:meio], cont)
    r,c2 = get_canditado_a_majoritario(V[meio:], cont)
    if(l == None and r == None):
        return None, 0
    elif(l != None and r == None):
        return l, c1+1
    elif(l == None and r != None):
        return r, c2+1
    elif(l == r):
        return l, c1+c2
    else: 
        if c1 > c2:
           return l, c1
        elif c1 < c2:
            return r, c2
        else:
            return None, cont
        
def conta_elemento(V, e):
    cont = 0
    for i in V:
        if(i == e):
            cont = cont + 1
    return cont


def majoritario(V):
    #executa em O(log n)
    m = get_canditado_a_majoritario(V,0)
    # executa em O(n)
    freq = conta_elemento(V, m)

    if(freq > len(V)/2):
        return m
    else:
        return None     

V = [3,0,0,1,1,0,3,3,3,0,1,2,1,1,1,1,1,1,1,1,1,1,1,6,0,0,0]

print(majoritario(V))


#efeitosa@icomp.ufam.edu.br
