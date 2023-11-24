'''
31
Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
    - Utiliza el menor número de líneas para resolver el ejercicio.
'''
def leap_year(year):
    print('\nMUESTRO POR PANTALLA LOS 30 AÑOS BISIESTOS SIGUIENTES AL PASADO POR PARAMETRO')
    cont = 1
    while cont < 31:
        if year % 4 == 0:
            if year % 100 != 0 and year % 400 != 0:
                print(cont, ' - BISIESTO: ', year)
                year += 4
                cont += 1
            else:
                year += 4
                cont += 1
        else:
            year += 1

leap_year(2046)


'''
32
Dado un listado de números, encuentra el SEGUNDO más grande.

'''
def sort_array(num_list):
    print('\nMUESTRO POR PANTALLA EL SEGUNDO VALOR MAS GRANDE DEL ARRAY PASADO POR PARAMETRO')
    
    aux_list = num_list
    aux_list.sort(reverse=True)    
    return aux_list[1]

print(sort_array([5,9,4,6,1,4,17,59]))


'''
33
Enunciado: Crea un función, que dado un año, indique el elemento y animal correspondiente en el ciclo sexagenario del zodíaco chino.
    - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
    - El ciclo sexagenario se corresponde con la combinación de los elementos madera, fuego, tierra, metal, agua y los animales rata, 
    buey, tigre, conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo (en este orden).
    - Cada elemento se repite dos años seguidos.
    - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
'''
def chinesse_horoscope(year):
    print('\nIMPRIMO POR PANTALLA EL ANIMAL Y EL ELEMENTO')
    animal_list = ['Rata', 'Buey', 'Tigre', 'Conejo', 'Dragón', 'Serpiente', 'Caballo', 'Oveja', 'Mono', 'Gallo', 'Perro', 'Cerdo']
    element_list = ['Madera', 'Fuego', 'Tierra', 'Metal', 'Agua']

    animal_pos = (year - 1924) % 12
    element_pos = ((year - 1924) % 10) // 2

    return animal_list[animal_pos], element_list[element_pos]

year = 1948
animal, element = chinesse_horoscope(year)
print('El año ', year, ' fue el año: ', animal, ' ', element)


'''
34
Enunciado: Dado un array de enteros ordenado y sin repetidos, crea una función que calcule y retorne todos los que faltan entre
el mayor y el menor.
    - Lanza un error si el array de entrada no es correcto.
'''
def complete_array(num_list):
    print('\nIMPRIMO POR PANTALLA EL ARRAY COMPLETO')

    i = 1
    num_list_aux = num_list
    long_array = len(num_list_aux)

    while i < long_array:
        if num_list_aux[i-1] + 1 != num_list_aux[i]:
            num_list_aux.append(num_list_aux[i -1] +1)
            num_list_aux.sort()
        long_array = len(num_list_aux)
        i += 1
    return num_list_aux

num_list = [1,2,3,6,9,12]
print('El array ordenado y completo es: ', complete_array(num_list))


'''
35
Enunciado: Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
    - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
    - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
    - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
    - El programa recibe los siguientes parámetros:
    - Tipo del Pokémon atacante.
    - Tipo del Pokémon defensor.
    - Ataque: Entre 1 y 100.
    - Defensa: Entre 1 y 100.
'''
def pokemon_card(poke_attack, poke_def, attack, deffense):
    
    '''
    EFECTIVIDAD
    ATAQUE  VS  DEFENSA 
    agua    vs  agua = 0.5
    agua    vs  fuego = 2
    agua    vs  planta = 0.5
    agua    vs  electrico = 1

    fuego   vs  fuego = 0.5
    fuego   vs  agua = 0.5
    fuego   vs  planta = 2
    fuego   vs  electrico = 1

    planta  vs  planta = 0.5
    planta  vs  agua = 2
    planta  vs  fuego = 0.5
    planta  vs  electrico = 1
    
    electrico   vs  electrico = 0.5
    electrico   vs  agua = 2
    electrico   vs  fuego = 1    
    electrico   vs  planta = 0.5
    '''

    print('\nCALCULO EL DAÑO REALIZADO POR LA CARTA DEL POKEMON')
    if poke_attack == poke_def:
        effectiveness = 0.5
        return 50 * (attack / deffense) * effectiveness
    
    elif poke_attack == 'agua':
        if poke_def == 'fuego':
            effectiveness = 2
            return 50 * (attack / deffense) * effectiveness
        elif poke_def == 'planta':
            effectiveness = 0.5
            return 50 * (attack / deffense) * effectiveness
        elif poke_def == 'electrico':
            effectiveness = 1
            return 50 * (attack / deffense) * effectiveness 
    elif poke_attack == 'fuego':
        if poke_def == 'agua':
            effectiveness = 0.5
            return 50 * (attack / deffense) * effectiveness
        elif poke_def == 'planta':
            effectiveness = 2
            return 50 * (attack / deffense) * effectiveness
        elif poke_def == 'electrico':
            effectiveness = 1
            return 50 * (attack / deffense) * effectiveness
    elif poke_attack == 'planta':
        if poke_def == 'agua':
            effectiveness = 2
            return 50 * (attack / deffense) * effectiveness
        elif poke_def == 'fuego':
            effectiveness = 0.5
            return 50 * (attack / deffense) * effectiveness
        elif poke_def == 'electrico':
            effectiveness = 1
            return 50 * (attack / deffense) * effectiveness
    elif poke_attack == 'electrico':
        if poke_def == 'agua':
            effectiveness = 2
            return 50 * (attack / deffense) * effectiveness
        elif poke_def == 'fuego':
            effectiveness = 1
            return 50 * (attack / deffense) * effectiveness
        elif poke_def == 'planta':
            effectiveness = 0.5
            return 50 * (attack / deffense) * effectiveness 

poke_attack, poke_def, attack, deffense = 'agua', 'fuego', 44, 98
print('El daño del pokemon es: ', pokemon_card(poke_attack, poke_def, attack, deffense))


'''
36
Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales a Sauron contra otras bondadosas que no quieren que el mal 
reine sobre sus tierras. Cada raza tiene asociado un "valor" entre 1 y 5:
    - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3), Númenóreanos (4), Elfos (5)
    - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2), Huargos (3), Trolls (5)
Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:
    - El resultado puede ser que gane el bien, el mal, o exista un empate. Dependiendo de la suma del valor del ejército y el número 
    de integrantes.
    - Cada ejército puede estar compuesto por un número de integrantes variable de cada raza.
    - Tienes total libertad para modelar los datos del ejercicio.
    - Ej: 1 Peloso pierde contra 1 Orco
        2 Pelosos empatan contra 1 Orco
        3 Pelosos ganan a 1 Orco
'''
def calc_battle(good_list, bad_list):
    '''
    BUENOS
    P = 1
    SB = 2
    E = 3
    N = 4
    EL = 5

    MALOS
    SM = 2
    O = 2
    G = 2
    H = 3
    T = 5
    '''
    print('\nCALCULO COMO TERMINO LA BATALLA')
    good = 0
    bad = 0
    for pers in good_list:
        if pers == 'P':
            good += 1
        elif pers == 'SB':
            good += 2
        elif pers == 'E':
            good += 3
        elif pers == 'N':
            good += 4
        elif pers == 'EL':
            good += 5

    for pers in bad_list:
        if pers == 'SM':
            bad += 2
        elif pers == 'O':
            bad += 2
        elif pers == 'G':
            bad += 2
        elif pers == 'H':
            bad += 3
        elif pers == 'TL':
            bad += 5

    if good > bad:
        return 'GANARON LOS BUENOS'
    elif bad > good:
        return 'GANARON LOS MALOS'
    else:
        return 'EMPATARON'

good_list = ['P', 'SB', 'E', 'N', 'EL', 'P']
bad_list = ['SM', 'O', 'G', 'H', 'TL', 'SM']
print(calc_battle(good_list, bad_list))


'''
37
Enunciado: ¡Han anunciado un nuevo "The Legend of Zelda"! Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos "The Legend of Zelda" de la historia? Crea un programa que calcule 
cuántos años y días hay entre 2 juegos de Zelda que tú selecciones.
    - Debes buscar cada uno de los títulos y su día de lanzamiento (si no encuentras el día exacto puedes usar el mes, o incluso 
    inventártelo)
'''
def legend_zelda(game_one, game_two):
    from datetime import datetime as dt
    from dateutil.relativedelta import relativedelta

    print('\nCALCULO LA DIFERENCIA ENTRE DOS FECHAS')
    zelda_one = dt.strptime(game_one, '%d/%m/%Y')
    zelda_two = dt.strptime(game_two, '%d/%m/%Y')
    difference = relativedelta(zelda_two, zelda_one)
    return difference

game_one = '26/09/1988'
game_two = '24/09/1992'
difference = legend_zelda(game_one, game_two)
print('La diferencia es ', difference.years, ' años ', difference.months, ' meses y ', difference.days, ' dias')


'''
38
Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar funciones propias del lenguaje que 
lo hagan directamente.
'''
def from_bin_to_dec(bin_num):
    print('\nCALCULO CUANTO VALE EL EN DECIMAL EL NUMERO BINARIO INGRESADO')
    return ''

bin_num = '0110011100'
print('El numero ', bin_num, ' en decimal es: ', from_bin_to_dec(bin_num))


'''
39
Enunciado: Implementa uno de los algoritmos de ordenación más famosos: el "Quick Sort", creado por C.A.R. Hoare.
    - Entender el funcionamiento de los algoritmos más utilizados de la historia nos ayuda a mejorar nuestro conocimiento sobre 
    ingeniería de software. Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
    - Esta es una nueva serie de retos llamada "TOP ALGORITMOS", donde trabajaremos y entenderemos los más famosos de la historia.
'''



'''
40
Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole únicamente el tamaño del lado.
    - Aquí puedes ver rápidamente cómo se calcula el triángulo: https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
'''