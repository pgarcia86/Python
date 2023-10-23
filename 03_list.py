##Operaciones con listas. Concatenación, asignación, modificación. Bucle While

my_list = list()
my_list = [1,2,3,4,5,6]

print("Imprimo una lista")
print(my_list)

print("\n\n\nSumo 4 e imprimo")
for i in my_list:
    print(i + 4)

my_words_list = [] 
my_words_list = ['one', 'two', 'three', 'four', 'five', 'six']

my_data_list = list()
my_data_list = ["Pablo", "Nicolas", "Garcia", "Barros", 37, 1.66]

print("\n\n\nImprimo una lista de palabras")
print(my_words_list)

print("\n\n\nImprimo las dos listas concatenadas")
print(my_list + my_words_list)

print("\n\n\nImprimo una lista de palabras concatenadas")
for word in my_words_list:
    print(word + " + four")


print("\n\n\nImprimo una lista de palabras, usando el largo de la lista como rango del for")
for i in range(len(my_words_list)):
    print(i, my_words_list[i])


print("\n\n\nInserto en la posicion 6, el numero 7")
my_list.insert(6,7)
print(my_list)


print("\n\n\nInserto en la ultima posicion el numero 8")
my_list.append(8)
print(my_list)

print("\n\n\nInserto en la posicion 6 la palabra siete")
my_words_list.insert(6,"seven")
print(my_words_list)


print("\n\n\nInserto en la ultima posicion la palabra ocho")
my_words_list.append("eight")
print(my_words_list)


print("\n\n\nAsigno a una lista de variables los elementos de la lista my_list")
one, two, three, four, five, six, seven, eight = my_list
print(two)

print("\n\n\nAsigno a variables cada uno de los elementos de my_data_list")

first_name = my_data_list[0]
second_name = my_data_list[1]
first_surname = my_data_list[2]
second_surname = my_data_list[3]
age = my_data_list[4]
heigth = my_data_list[5]

print(heigth)

number = 10

print("\n\n\nImprimo los numeros de 10 al 0 usando while")
while number > -1:    
    
    print(number)
    number -= 1

print("\n\n\nCuento la cantidad de veces que se encuentra ese objeto en la lista")
print(my_words_list.count("one"))


print("\n\n\nElimino todos los elementos de my_list")
my_list.clear()
print(my_list)


print("\n\n\n")
words_list_copy = my_words_list.copy()
print(words_list_copy)


print("\n\n\nCambio el elemento 2 a un entero")
my_words_list[2] = 3
print(my_words_list)


print("\n\n\nElimino de la lista el elemento igual al pasado por parametro")
my_words_list.remove(3)
print(my_words_list)


my_words_list.insert(2, "three")
print("\n\n\nInserto en la posicion 2 el elemento three e imprimo el indice donde se encuentra el elemento pasado por parametro")
print(my_words_list, end = "\t\t")
print(my_words_list.index("three"))


print("\n\n\nCon POP quito de la lista el elemento que esta en la posicion pasada por paramentro y lo asigno a una variable")
word = my_words_list.pop(4)
print(my_words_list, end = "\t\t")
print(word)


print("\n\n\nInserto el elemento five en la posicion 4 y revierto el orden de la lista")
my_words_list.insert(4, "five")
my_words_list.reverse()
print(my_words_list)


print("\n\n\nCon SORT ordeno la lista por orden alfabético")
my_words_list.sort()
print(my_words_list)
print(my_data_list)


