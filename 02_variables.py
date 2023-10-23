##Operaciones básicas con variables. Asignaciones, concatenaciones, iteracion con for en un string

height = 22             ##Asigno el valor 22 a la variable height

width = 2               ##Asigno el valor 2 a la variable height

print(height * width)   ##Muestro por pantalla el producto del valor de ambas variables

word = "word"

print(word)

otherword = "other"

print(word + otherword)                 ##Concateno string

print(word + " " + otherword)

string = "this is a string"             ##Declaro un string

print(string)

print(string[0])                        ##Accedo al elemento 0 de la variable string (T)

print(string[1].upper())                ##Accedo y modifico el elemento 1 de la variable string (h -> H)

##Con el bucle for recorro la variable string cada uno de sus elementos y los imprimo modificados por pantalla                
for i in string:
    print(i.upper())