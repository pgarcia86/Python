##  Exception

num_one = 13
num_two = 3
num_three = "3"

try:
    print(num_one + num_two)
except:
    print("Hubo un problema")

print("Sigue ejecutando\n")

try:
    print(num_one / num_two)
except:
    print("No se puede dividir por cero")
finally:
    print("Ejecuta esto siempre")

print("Sigue ejecutando\n")

try:
    print(num_one + num_three)
except ValueError:
    print("Hubo un error ValueError")
except TypeError:
    print("Hubo un error TypeError")
finally:
    print("Esto se ejecuta siempre")


print("Sigue ejecutando\n")

try:
    print(num_one + num_three)
except ValueError as error:
    print(error)
except Exception as my_error:
    print(my_error)
finally:
    print("Esto se ejecuta siempre")