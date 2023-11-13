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
    
    print("\nSE PASAN 2 LISTAS POR PARAMETRO Y UN BOOLEANO. SI ES TRUE, DEVUELVO LOS VALORES REPETIDOS, SINO LOS NO REPETIDOS")
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
def max_com_div(num_1, num_2):

    div_list = []

    for i in range(1, num_1 + 1):
        if num_1 % i == 0:
            div_list.append(i)

    for i in range(1, num_2 + 1):
        if num_2 % i == 0:
            div_list.append(i)
    
    div_list.sort(reverse = True)

    for num in div_list:
        if div_list.count(num) > 1:
            return num
    
    return None

def min_com_mul(num_1, num_2):

    mcd = max_com_div(num_1, num_2)
    return (num_1 * num_2)/mcd

print('\nMAXIMO COMUN DIVISIOR: ', max_com_div(10, 20))
print('\nMINIMO COMUN MULTIPLO: ', min_com_mul(10, 8))

'''
24
Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
    - ¿De cuántas maneras eres capaz de hacerlo?
    Crea el código para cada una de ellas.
'''
def one_to_hundred():

    print('\nIMPRIMO DEL 1 AL 100:')

    for i in range(1, 101):
        print(i)

    i = 1
    print('\n')
    while i < 101:
        print(i)
        i += 1
    
one_to_hundred()

'''
25
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
    - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
    - La función recibe un listado que contiene pares, representando cada jugada.
    - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
    - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
'''
def rock_paper_scissors(game_list):

    print('\nPIEDRA PAPEL O TIJERA - DEVUELVE EL GANADOR')

    player_1_list = []
    player_2_list = []
    games_result = []

    for i in range(0, len(game_list)):
        player_1_list.append(game_list[i][0])

    for i in range(0, len(game_list)):
        player_2_list.append(game_list[i][1])
    
    for i in range(0, len(player_1_list)):
        if player_1_list[i] == player_2_list[i]:
            games_result.append('TIE')
        else:
            if player_1_list[i] == 'R'and player_2_list[i] == 'S':
                games_result.append('PLAYER 1')
            elif player_1_list[i] == 'S' and player_2_list[i] == 'P':
                games_result.append('PLAYER 1')
            elif player_1_list[i] == 'P' and player_2_list[i] == 'R':
                games_result.append('PLAYER 1')
            else:
                games_result.append('PLAYER 2')

    cont = 0

    for i in games_result:
        if games_result.count(i) > cont:
            winner = i
            cont = games_result.count(i)
    
    if cont == 1:
        return 'TIE'

    return winner

print(rock_paper_scissors([('R', 'S'), ('R', 'R'), ('P', 'R')]))

'''
26
    Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
    - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
    - EXTRA: ¿Eres capaz de dibujar más figuras?
'''
def draw_figure(side, figure):

    print('\nDIBUJO UNA FIGURA CON "*" DEPENDIENDO DE LO PASADO POR PARAMETRO')

    cont = side

    if figure == 'C':
        # CODIGO PARA DIBUJAR UN CUADRADO
        for i in range(0, side):
            for j in range(0, side):
                print('* ', end = ' ')
            print('\n')
    else:
        # CODIGO PARA DIBUJAR UN TRIANGULO
        while cont > 0:
            for i in range(0, cont):
                print('* ', end = ' ')
            print('\n')
            cont -= 1

draw_figure(4, 'T')


'''
27
    Crea un programa que determine si dos vectores son ortogonales.
    - Los dos array deben tener la misma longitud.
    - Cada vector se podría representar como un array. Ejemplo: [1, -2]
'''
def ort_vect(vect_1, vect_2):

    print('\nVERIFICO SI DOS VECTORES SON ORTOGONALES')
    
    res = 0

    if len(vect_1) != len(vect_2):
        return 'Los vectores no tienen la misma longitud'
    else:
        for i in range(len(vect_1)):
            res += vect_1[i] * vect_2[i]

        if res == 0:
            return 'LOS VECTORES SON ORTOGONALES'
        return 'LOS VECTORES NO SON ORTOGONALES'

print(ort_vect([1, -2], [2, 1]))

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
def vending_machine(money_array, prod_num):

    print('\nSIMULACION DE VENDING MACHINE SI ALCANZA EL DINERO DA EL VUELTO DE LA MANERA MAS EFICIENTE POSIBLE, SI EL CODIGO DEL '
          'PRODUCTO NO ES VALIDO, DEVUELVE QUE NO ES POSIBLE LA OPERACION Y SI NO ALCANZA EL DINERO TAMBIEN LO AVISA')

    prod_list = list()
    codes = []
    money_map = {
        'Five' : 0,
        'Ten' : 0, 
        'Fifty' : 0,
        'OneHundred' : 0,
        'TwoHundred' : 0
    }

    try:
        money = money_array[0]*0.05 + money_array[1]*0.1 + money_array[2]*0.5 + money_array[3]*1 + money_array[4]*2
        print('DINERO INGRESADO: ', money)

        prod_list.append({
           'Name' : 'Agua',
            'Code': 1,
            'Value' : 7.50
        })
        prod_list.append({
            'Name' : 'Coca Cola',
            'Code': 2,
            'Value' : 7.50
        })
        prod_list.append({
            'Name' : 'Cerveza',
            'Code': 3,
            'Value' : 7.50
        })
        prod_list.append({
            'Name' : 'Vino Tinto',
            'Code': 4,
            'Value' : 7.50
        })
        prod_list.append({
            'Name' : 'Papas Fritas',
            'Code': 5,
            'Value' : 7.50
        })
        prod_list.append({
            'Name' : 'Piza',
            'Code': 6,
            'Value' : 7.50
        })

        for prod in prod_list:
            codes.append(prod['Code'])
        
        if prod_num not in codes:
            return "EL PRODUCTO NO EXISTE EN LA MAQUINA"        
        prod = prod_list[codes.index(prod_num)]

        print('EL PRODUCTO ELEGIDO ES: ', prod['Name'], '- SU PRECIO ES: ', prod['Value'], '€')

        if money < prod['Value']:
            return 'NO TIENE DINERO SUFICIENTE'

        dif = round(money - prod['Value'], 2)
        print('VUELTO: ', dif)
        while dif > 0.01:
            if round(dif // 2, 2) >= 1:
                money_map['TwoHundred'] = round(dif // 2, 2)
                dif = round((dif % 2), 2)
            elif round(dif // 1, 2) >= 1:
                money_map['OneHundred'] = round(dif // 1, 2)
                dif = round((dif % 1), 2)
            elif round(dif // 0.5, 2) >= 1:
                money_map['Fifty'] = round(dif // 0.5, 2)
                dif = round((dif % 0.5), 2)
            elif round(dif // 0.1, 2) >= 1:
                money_map['Ten'] = round(dif // 0.1, 2)
                dif = round((dif % 0.1), 2)
            elif round(dif // 0.05, 2) >= 1:
                money_map['Five'] = round(dif // 0.05)
                dif = round((dif % 0.05), 2)
        return "EL VUELTO A ENTREGAR ES: ", money_map
    except:
        print('\nHAY UN ERROR EN EL ARRAY DE MONEDAS')    

print(vending_machine([5, 3, 8, 2, 2], 4))


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