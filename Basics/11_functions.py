##  Functions

def my_function():
    print("Imprimo desde la funcion")

def my_other_function(num_1, num_2):
    print(num_1 + num_2)


def my_another_function(num_1, num_2):
    res = num_1 + num_2
    return res

def print_string(name, surname):
    print(f"{name} {surname}")

def print_other_string(name, surname, alias = "Chiche"):
    print(f"{name} {surname} {alias}")

my_function()

print("\n")

my_other_function(2, 2)

print("\n")

my_other_function(17, 22)

print("\n")

num = my_another_function(2, 2)
print(num)

print("\n")

print_string("Pablo", "Garcia")

print("\n")

print_string("Garcia", "Pablo")

print("\n")

print_string(surname = "Pablo", name = "Garcia")

print("\n")

print_other_string("Pablo", "Garcia")

print("\n")

print_other_string(surname = "Pablo", name = "Garcia", alias = "Cramiento")

print("\n")

print_other_string("Garcia", "Pablo")

print("\n")
