##Serie de Fibonacci sin recursividad ni listas

a = 0
b = 1
c = 0
for i in range(11):
    
    print(a)
    c = a + b
    a = b
    b = c