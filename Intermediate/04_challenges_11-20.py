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

    print("\n11 - ELIMINAR LETRAS REPETIDAS EN UN STRING Y NO EN OTRO Y VICEVERSA")
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

    print("\n12 - CHEQUEO QUE DOS FRASES SEAN PALINDROMO")
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
    
print("\n13 - CALCULO DEL FACTORIAL: ", factorial(17))


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

    print("\n14 - CHEQUEO SI EL NUMERO ES UN NUMERO DE ARMSTRONG")
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
from datetime import datetime
def dif_dates(first_string, second_string):

    print("\n15 - CALCULO DIFERENCIA ENTRE FECHAS")
    try:
        if first_string.count('/') > 1 and second_string.count('/') > 1:
            print("SON FECHAS VALIDAS")
            first_date = datetime.strptime(first_string, '%d/%m/%Y')
            second_date = datetime.strptime(second_string, '%d/%m/%Y')    
            diference = first_date - second_date
        if diference.days >= 0:
            return diference.days
        return diference.days * (-1)    
    except:
        print("NO SON FECHAS VALIDAS")

print("LA DIFERENCIA ENTRE LOS DIAS ES:", dif_dates("24/03/1986", "14/08/1989"))


"""
16
Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
    - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""
def upper_string(phrase):  

    print("\n16 - PONGO EN MAYUSCULA LA PRIMERA LETRA DE CADA PALABRA QUE INGRESO POR PARAMETRO")
    spaces = [0]
    ## Creo una lista con la  posicion de los espacios
    for i in range(len(phrase)):        
        if phrase[i] == " ":
            spaces.append(i + 1)

    letter_list = from_string_to_list(phrase)

    for position in spaces:
        letter_list[position] = letter_list[position].upper()

    new_phrase = from_list_to_string(letter_list)
    print(new_phrase)

upper_string(phrase = "esta es una frase de prueba. voy a intentar poner en mayuscula cada una de las primeras palabras de string")


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
from operator import length_hint
def athlete(run_jump, floor_fence):

    print("\n17 - JUEGO DEL ATLETA")

    count = 0

    if length_hint(run_jump) == len(floor_fence):
        for word in run_jump:
            if word == 'run' and floor_fence[count] == '|':
                floor_fence = floor_fence.replace(floor_fence[count], 'x', 1)
            elif word == 'jump' and floor_fence[count] == '_':
                floor_fence = floor_fence.replace(floor_fence[count], '/', 1)
            count += 1
        print(floor_fence)

        if floor_fence.count('x') > 0 or floor_fence.count('/') > 0:
            return False
        else:
            return True
    else:
        print("NO SE PUEDEN COMPARAR LOS STRINGS")
        return False
    
print(athlete(['run', 'run', 'run', 'jump', 'jump', 'run', 'jump', 'jump', 'run', 'run'], '___||_||__'))



"""
18
TRES EN RAYA
Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
    - "X" si han ganado las "X"
    - "O" si han ganado los "O"
    - "Empate" si ha habido un empate
    - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
"""
def three_in_row(matrix):

    print("\n18 - TRES EN FILA")    
    win_combination = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    position_x = []
    position_o = []
    matrix_x = []
    matrix_o = []
    row = []
    win = True

    if len(matrix) != 3:
        return "LA MATRIZ NO ES VALIDA"

    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix[0])):        
            row.append(matrix[i][j])
    
    for i in range(0, len(row)):
        if row[i] == 'x':
            position_x.append(i)
            position_o.append('/')
        elif row[i] == 'o':
            position_o.append(i)
            position_x.append('/')
        else:
            return "LA MATRIZ NO ES VALIDA"
        
    matrix_x = [position_x[0: 3], position_x[3: 6], position_x[6: 9]]
    matrix_o = [position_o[0: 3], position_o[3: 6], position_o[6: 9]]

    for i in range(0, len(matrix_x[0])):
        for j in range(0, len(win_combination)):
            if matrix_x[i] == win_combination[j]:
                return "GANO EL X"
            elif matrix_o[i] == win_combination[j]:
                return "GANO EL O"
            else:
                return "EMPATARON"

print(three_in_row([['x', 'o', 'x'], ['x', 'x', 'o'], ['o', 'o', 'o']]))


"""
19
Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
"""
def days_in_miliseconds(day, hour, minutes, seconds):

    print("\n19 - IMPRIMO EN MILISEGUNDOS LOS VALORES PASADOS POR PARAMETROS")

    milisec_per_day = 24 * 60 * 60 * 1000
    milisec_per_hour = 60 * 60 * 1000
    milisec_per_min = 60 * 1000
    milisec_per_sec = 1000

    return day * milisec_per_day + hour * milisec_per_hour + minutes * milisec_per_min + seconds * milisec_per_sec

print(days_in_miliseconds(5, 3, 4, 10))


"""
20
Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
    - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
    - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa 
    principal. Se podría ejecutar varias veces al mismo tiempo.
"""
import time
def time_lapse(num_1, num_2, lapse):

    print("\n20 - IMPRIMO UN RESULTADO DESPUES DE UN DETERMINADO LAPSO DE TIEMPO, ESTE TIEMPO SE PASA POR PARAMETRO")

    time.sleep(lapse)
    return num_1 + num_2

print(time_lapse(2, 2, 2))