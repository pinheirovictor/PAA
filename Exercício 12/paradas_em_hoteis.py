def paradas(D, x):
    dist = 0
    l = set()
    for i in range(len(x)-1):
        if(x[i] - dist < D):
            if(x[i+1] - dist > D):
                l.add(i)
                dist = x[i]
        elif((x[i] - dist) == D):
            l.add(i)
            dist = x[i]
    print(l)


D = 12
x = [0, 5,  8, 9, 14, 19, 20, 32]
paradas(D, x)