from Person import Person

my_person = Person("Pablo", "Garcia")

print(my_person.get_name())

my_person.alias = "Chiche"

print(my_person.alias)

##print(my_person.__name)                             ##Esto no funciona porque el atributo es privado

my_person.set_name("Fernando")

print(my_person.get_full_name())

print(my_person.walk())

print(my_person.not_walk())