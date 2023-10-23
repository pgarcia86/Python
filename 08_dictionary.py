##Diccionarios

my_dict = dict()
my_other_dict = {}
new_dict = {}
my_list = list()

print(type(my_dict))
print(my_other_dict.__class__)

my_dict = {

    "Name" : "Pablo",
    "Surname" : "Garcia Barros",
    "Age" : 37,
    "Height" : 1.66
}

my_other_dict = {

    "Name" : "Sebastian",
    "Surname" : "Pissinis",
    "Age" : 41,
    "Height" : 1.77,
    "Year" : 1981
}

my_list = my_dict.keys()


print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Name"])
print(my_other_dict["Year"])

print("Name" in my_dict)
print("Year" in my_dict)

print("Year" in my_other_dict)

my_dict["Address"] = "Vintro 15"
print(my_dict)

my_dict["Name"] = "Ruben"
print(my_dict)

my_dict["Name"] = "Pablo"
print(my_dict)

del my_dict["Address"]

print(my_dict)

print(my_dict.items())

print(my_dict.keys())               ##Con el metodo keys() obtengo el nombre del campo del diccionario con el que estoy trabajando
print(my_dict.values())             ##Con el metodo values() obtengo el nombre de los valores del diccionario con el que estoy trabajando

new_dict = dict.fromkeys(my_list)
# new_dict['Name'] = "Juan Carlos"
# new_dict['Age'] = 98
# new_dict['Height'] = 1.94

print(new_dict)
