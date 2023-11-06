## Challenges - 11-20

from modules import from_string_to_list, from_list_to_string, take_off_spaces
import re, string

"""
11
Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
    - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
    - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
"""
def equals_characters(word_one, word_two):

    print("\nELIMINAR LETRAS REPETIDAS EN UN STRING Y NO EN OTRO Y VICEVERSA")
    word_one_list = from_string_to_list(word_one)
    word_two_list = from_string_to_list(word_two)
    repeated_list = []
    one_not_two = []
    two_not_one = []

##  Creo una lista con los valores repetidos
    for i in range(0, len(word_one_list)):
        for j in range(0, len(word_two_list)):
            if word_one_list[i] == word_two_list[j]:
                repeated_list.append(word_one_list[i])
                break

##  Quito los valores repetidos de la lista de repetidos
    for repeted in repeated_list:
        if repeated_list.count(repeted) > 1:
            repeated_list.remove(repeted)

##  Quito de cada una de las listas los valores repetidos
    for letter in word_one_list:
        if letter not in repeated_list:
            one_not_two.append(letter)

    for letter in word_two_list:
        if letter not in repeated_list:
            two_not_one.append(letter)

    print(from_list_to_string(one_not_two))
    print(from_list_to_string(two_not_one))
equals_characters("palabra uno", "camion dudoso")


"""
12
Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
    - Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
    - NO se tienen en cuenta los espacios, signos de puntuación y tildes.
    Ejemplo: Ana lleva al oso la avellana.

"""
def is_palindrome(phrase):

    print("\nCHEQUEO QUE DOS FRASES SEAN PALINDROMO")
    aux_phrase = take_off_spaces(phrase.lower())
    reverse_phrase = aux_phrase[::-1]

    if aux_phrase == reverse_phrase:
        return True
    else:
        return False

print(is_palindrome("Ana llevA al oso la Avellana!!!!"))


"""
13
Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
"""
def factorial(number):
    if number < 0:
        return None
    elif number <= 1:
        return 1
    else:
        return number * factorial(number - 1)  
    
print("\nCALCULO DEL FACTORIAL: ", factorial(17))


"""
14
Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista). 
    - Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
    - Por ejemplo, 371, 8208 y 4210818 son números de Armstrong ya que:
        · 371 = 3^3 + 7 + 1³   
        · 8208 = 8^4 + 2^4 + 0^4 + 8^4 
        · 4210818 = 4^7 + 2^7 + 1^7 + 0^7 + 8^7 + 1^7 + 8^7
"""
import math
def armstrong_number(number):

    print("\nCHEQUEO SI EL NUMERO ES UN NUMERO DE ARMSTRONG")
    aux_num = number
    arsmtrong = 0
    cant_digits = int(math.log10(number)) + 1 
    cont = cant_digits - 1

    while cont >= 0:
        arsmtrong += math.trunc(aux_num / (10 ** (cont))) ** cant_digits
        aux_num -= math.trunc(aux_num / (10 ** (cont))) * (10 ** (cont))
        cont -= 1

    if arsmtrong == number:
        return "Es un numero de Armstrong"
    return "No es un numero de Armstrong"

print(armstrong_number(4210818))


















"""
15
Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
    - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
    - La función recibirá dos String y retornará un Int.
    - La diferencia en días será absoluta (no importa el orden de las fechas).
    - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
 */
"""













"""
16
Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
    - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""
















"""
17
Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
    - La función recibirá dos parámetros:
    - Un array que sólo puede contener String con las palabras "run" o "jump"
    - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
    - La función imprimirá cómo ha finalizado la carrera:
    - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista.
    - Si hace "jump" en "_" (suelo), se variará la pista por "x".
    - Si hace "run" en "|" (valla), se variará la pista por "/".
    - La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""





















"""
18
Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
    - "X" si han ganado las "X"
    - "O" si han ganado los "O"
    - "Empate" si ha habido un empate
    - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
"""





















"""
19
Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
"""





















"""
20
Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
    - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
    - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa 
    principal. Se podría ejecutar varias veces al mismo tiempo.
"""