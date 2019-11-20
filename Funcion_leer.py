import os,sys
os.system("cls")

def contarletra(a,b):
    d = 0
    for i in a:
        if b == i:
            d += 1
        else:
            d += 0
    return d

A = contarletra("hola mundo", "o")
B = contarletra("1231133421", "1")

print(A)
print(B)