##  Conditionals

my_conditional = False

if (my_conditional):

    print("Imprimo esto")

else:

    print("Esto se imprime en el else\n")

my_conditional = 100

while(my_conditional > -1):

    if(my_conditional % 2 == 0):
        print(my_conditional)
    
    else:
        print("Es un numero impar")

    my_conditional -= 1


my_conditional = 10

my_other_conditional = 5

if my_conditional == 10 and my_other_conditional == 5:
    print("\nLas dos condiciones son verdaderas")

if my_conditional == 10 and my_other_conditional == 13:
    print("\nLas dos condiciones son verdaderas")

elif my_conditional % my_other_conditional == 0:
    print("\nLos numeros son multiplos")
else:
    print("\nNo hay cosas en comun en los numeros")


my_conditional = 11

my_other_conditional = 3

if my_conditional == 10 and my_other_conditional == 5:
    print("\nLas dos condiciones son verdaderas")

if my_conditional == 10 and my_other_conditional == 13:
    print("\nLas dos condiciones son verdaderas")

elif my_conditional % my_other_conditional == 0:
    print("\nLos numeros son multiplos")
else:
    print("\nNo hay cosas en comun en los numeros")

