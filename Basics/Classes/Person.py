
class Person:

    def __init__(self, name, surname, alias = "Sin alias"):
        self.__name = name
        self.surname = surname
        self.alias = alias

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_full_name(self):
        return f"{self.__name} {self.surname} ({self.alias})"
    
    def walk(self):
        return self.get_full_name() + " esta caminando"
    
    def not_walk(self):
        return self.get_full_name() + " no esta caminando"
