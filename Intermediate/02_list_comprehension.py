##  List Comprehension

def operation(number):
    return number + 5

original_list = [1, 9, 14, 37, 25, 44, 12, 74]

my_range = range(8)

print(my_range)

my_list = [i for i in my_range]                     ##  Creo una lista con los numeros del rango my_range

print(my_list)

my_other_list = [3 for i in my_range]               ##  Creo una lista de 3 del tamaño del rango my_range

print(my_other_list)

my_other_list = [(i * 3) for i in my_range]         ##  Hace la operacion i*3 antes de agregar el valor a la lista

print(my_other_list)

my_list = [i * i for i in my_range]                 ##  Hace la operacion i * i antes de agregar el valor a la lista

print(my_list)

my_list = [operation(i) for i in original_list]     ##  Llamo a la funcion operation y la ejecuta antes de agregar ek valor a la lista

print(my_list)
