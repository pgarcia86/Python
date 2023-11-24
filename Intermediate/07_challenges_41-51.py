## Challenges - 41-51
'''
41
Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
    - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
    - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".
'''


'''
42
Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
    - Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
    - En caso contrario retornará un error.
'''


'''
43
Enunciado: Este es un reto especial por Halloween. Deberemos crear un programa al que le indiquemos si queremos realizar "Truco o Trato"
y un listado (array) de personas con las siguientes propiedades:
    - Nombre de la niña o niño
    - Edad
    - Altura en centímetros
Si las personas han pedido truco, el programa retornará sustos (aleatorios) siguiendo estos criterios:
    - Un susto por cada 2 letras del nombre por persona
    - Dos sustos por cada edad que sea un número par
    - Tres sustos por cada 100 cm de altura entre todas las personas
    - Sustos: 🎃 👻 💀 🕷 🕸 🦇
Si las personas han pedido trato, el programa retornará dulces (aleatorios) siguiendo estos criterios:
    - Un dulce por cada letra de nombre
    - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
    - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
    - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
'''


'''
44
Enunciado: Crea una función que retorne el número total de bumeranes de un array de números enteros e imprima cada uno de ellos.
    - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números seguidos, en el que el primero y el último son iguales, 
    y el segundo es diferente. Por ejemplo [2, 1, 2].
    - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2] y [4, 2, 4]).
'''


'''
45
Enunciado: Dado un array de números enteros positivos, donde cada uno representa unidades de bloques apilados, debemos calcular cuantas 
unidades de agua quedarán atrapadas entre ellos.
    - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].

        ⏹
        ⏹
   ⏹💧💧⏹
   ⏹💧⏹⏹💧⏹
   ⏹💧⏹⏹💧⏹
   ⏹💧⏹⏹⏹⏹

Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades de agua. Suponemos que existe un suelo impermeable en la parte
inferior que retiene el agua.
'''


'''
46
Enunciado: Calcula dónde estará un robot (sus coordenadas finales) que se encuentra en una cuadrícula representada por los ejes 
"x" e "y".
    - El robot comienza en la coordenada (0, 0).
    - Para idicarle que se mueva, le enviamos un array formado por enteros (positivos o negativos) que indican la secuencia de pasos 
    a dar.
    - Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene, luego 5, se detiene, y finalmente 2. 
    El resultado en este caso sería (x: -5, y: 12)
    - Si el número de pasos es negativo, se desplazaría en sentido contrario al que está mirando.
    - Los primeros pasos los hace en el eje "y". Interpretamos que está mirando hacia la parte positiva del eje "y".
    - El robot tiene un fallo en su programación: cada vez que finaliza una secuencia de pasos gira 90 grados en el sentido contrario 
    a las agujas del reloj.
'''


'''
47
Enunciado: Crea un función que reciba un texto y retorne la vocal que más veces se repita.
    - Ten cuidado con algunos casos especiales.
    - Si no hay vocales podrá devolver vacío. 
'''


'''
48
¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)? 24 días, 24 regalos sorpresa relacionados con desarrollo 
de software, ciencia y tecnología desde el 1 de diciembre.
Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne lo siguiente:
    - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo de ese día (a tu elección) y cuánto queda para que 
    finalice el sorteo de ese día.
    - Si la fecha es anterior: Cuánto queda para que comience el calendario.
    - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
Notas:
    - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00 y finaliza a las 23:59:59.
    - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos y segundos.
    - 🎁 Cada persona que aporte su solución entrará en un nuevo sorteo del calendario de aDEViento hasta el día de su corrección
    (sorteo exclusivo para quien entregue su solución).
'''


'''
49
Enunciado: Crea una función que sea capaz de detectar y retornar todos los handles de un texto usando solamente Expresiones Regulares.
Debes crear una expresión regular para cada caso:
    - Handle usuario: Los que comienzan por "@"
    - Handle hashtag: Los que comienzan por "#"
    - Handle web: Los que comienzan por "www.", "http://", "https://" y finalizan con un dominio (.com, .es...)
'''


'''
50
Enunciado: Crea una función que sea capaz de encriptar y desencriptar texto utilizando el algoritmo de encriptación de Karaca 
(debes buscar información sobre él).
'''


'''
51
Enunciado: Crea tu propio enunciado para que forme parte de los retos de 2023.
    - Ten en cuenta que su dificultad debe ser asumible por la comunidad y seguir un estilo semejante a los que hemos realizado durante 
    el año.
    - Si quieres también puedes proponer tu propia solución al reto (en el lenguaje que quieras).
'''