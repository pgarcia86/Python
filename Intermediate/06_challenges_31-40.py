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


'''
34
Enunciado: Dado un array de enteros ordenado y sin repetidos, crea una función que calcule y retorne todos los que faltan entre
el mayor y el menor.
    - Lanza un error si el array de entrada no es correcto.
'''


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


'''
37
Enunciado: ¡Han anunciado un nuevo "The Legend of Zelda"! Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos "The Legend of Zelda" de la historia? Crea un programa que calcule 
cuántos años y días hay entre 2 juegos de Zelda que tú selecciones.
    - Debes buscar cada uno de los títulos y su día de lanzamiento (si no encuentras el día exacto puedes usar el mes, o incluso 
    inventártelo)
'''


'''
38
Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar funciones propias del lenguaje que 
lo hagan directamente.
'''


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