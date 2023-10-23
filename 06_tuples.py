##Algunas operaciones con Tuples. Las tuplas son inmutables, es decir no pueden modificarse sus elementos.
##Pueden concatenarse y crear sub tuplas desde otra tupla. Pueden castearse a una lista, modificar esa lista y después volverlo a 
##asignar a la tupla

my_tuple = tuple()
my_other_tuple = ()
big_tuple = ()
sub_tuple = ()

my_tuple = ("Pablo", "Garcia Barros", 37, 1.66)
print(my_tuple)

print(my_tuple.count("Pablo"))

print(my_tuple.index("Garcia Barros"))

#print(my_tuple.index("Garcia"))             ##Esto da error, porque no hay ningun elemento dentro de la tupla que sea 'Garcia'

my_other_tuple = ("Sebastian", "Pissinis", 41, 1.77)


print("\n\nConcateno las 2 tuplas")
big_tuple = my_tuple + my_other_tuple
print(big_tuple)


print("\n\nCreo una sub tupla con datos de las otras 2 tuplas")
sub_tuple = big_tuple[2:4] + big_tuple[6:8]
print(sub_tuple)


print("\n\nCasteo la primer tupla a una lista y la doy vuelta")
my_list = list(my_tuple)
print(my_list.__class__)
print(my_list)
my_list.reverse()
print(my_list)


