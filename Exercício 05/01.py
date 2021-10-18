
def potencia (b, n):
    if (n == 1):
        return 1
    return (b * potencia(b, n-1))


a = potencia(9,2)

print(a)
