## Challenges - 21-30

from modules import from_string_to_list, from_list_to_string, take_off_spaces
'''
21
Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
    - El .txt se corresponde con las entradas de una calculadora.
    - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
    - Soporta números enteros y decimales.
    - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
    - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
    - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
'''



'''
22
Crea una función que reciba dos array, un booleano y retorne un array.
    - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
    - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
    - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
'''
def count_repeated(list_one, list_two, bool):
    
    print("SE PASAN 2 LISTAS POR PARAMETRO Y UN BOOLEANO. SI ES TRUE, DEVUELVO LOS VALORES REPETIDOS, SINO LOS NO REPETIDOS")
    repeated = []
    not_repeated = []
    
    for word_one in list_one:
        for word_two in list_two:
            if word_one == word_two:
                repeated.append(word_one)

    for word in list_one:
        if word not in repeated:
            not_repeated.append(word)
    
    for word in list_two:
        if word not in repeated:
            not_repeated.append(word)

    for rep in repeated:
        if repeated.count(rep) > 1:
            repeated.remove(rep)

    for no_rep in not_repeated:
        if not_repeated.count(no_rep) > 1:
            not_repeated.remove(no_rep)

    if bool:
        return repeated    
    return not_repeated

print(False, " ", count_repeated(['a', 'c', 'd', 'p'], ['b', 'e', 'f', 'p', 'f'], False))
print(True, " ", count_repeated(['a', 'c', 'd', 'p'], ['b', 'e', 'f', 'p', 'f'], True))


'''
23
Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
    - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
 '''


'''
24
Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
    - ¿De cuántas maneras eres capaz de hacerlo?
    Crea el código para cada una de ellas.
'''


'''
25
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
    - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
    - La función recibe un listado que contiene pares, representando cada jugada.
    - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
    - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
'''


'''
26
    Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
    - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
    - EXTRA: ¿Eres capaz de dibujar más figuras?
'''


'''
27
    Crea un programa que determine si dos vectores son ortogonales.
    - Los dos array deben tener la misma longitud.
    - Cada vector se podría representar como un array. Ejemplo: [1, -2]
'''


'''
28
Simula el funcionamiento de una máquina expendedora creando una operación que reciba dinero (array de monedas) y un número que indique 
la selección del producto.
    - El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor número de monedas).
    - Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un mensaje y retornar todas las monedas.
    - Si no hay dinero de vuelta, el array se retornará vacío.
    - Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
    - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
'''


'''
29
Crea una función que ordene y retorne una matriz de números.
    - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro adicional "Asc" o "Desc" para indicar si debe 
    ordenarse de menor a mayor o de mayor a menor.
    - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''


'''
30
Crea una función que reciba un texto y muestre cada palabra en una línea, formando un marco rectangular de asteriscos.
    - ¿Qué te parece el reto? Se vería así:
    **********
    * ¿Qué   *
    * te     *
    * parece *
    * el     *
    * reto?  *
    **********
'''