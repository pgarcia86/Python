## Classes

class EmptyPerson:
    pass                                ##  Con la instruccion pass puedo dejar vacia la clase EmptyPerson

print(EmptyPerson)                      ##Devuelve el nombre de la clase
print(EmptyPerson())                    ##Devuelve el objeto de la clase


class Person:

    def __init__(self, name, surname, alias = "Sin Alias"):
        self.__name = name                                  ##  Propiedad privada
        self.surname = surname
        self.alias = alias

    
    def get_name(self):
        return self.__name
    
    def get_full_name(self):
        return f"{self.__name} {self.surname} ({self.alias})"
    
    def walk(self):
        return self.get_full_name() + " esta caminando"
    
    def set_name(self, name):
        self.__name = name
    

my_person = Person("Pablo", "Garcia")

my_other_person = Person("Sebastian", "Pissinis", "El Artista")

my_another_person = Person("Ruben", "Andam", "El Turko")

print(my_person.get_name())

print(my_person.walk())

print(my_other_person.get_name())

print(my_other_person.walk())

print(my_another_person.get_full_name())

my_another_person.__name = "Alex"                   ##  Este metodo no funciona porque el atributo name esta declarado privado

my_another_person.set_name("Alex")

my_other_person.surname = "Torres"                  ##  Esto funciona porque el atributo esta declarado publico

print(my_another_person.get_name())

print(my_another_person.walk())

print(my_other_person.walk())
        
