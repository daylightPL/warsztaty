def suma_dzielnikow(n):
    suma = 0
    for i in range(1,n-1):
        if n % i == 0:
            suma = suma+i
    return suma

print (suma_dzielnikow(15))
