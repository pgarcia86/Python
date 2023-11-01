##  Challenges


##  FUNCIONES AUXILIARES PARA LOS CHALLENGES

def from_string_to_list(word):

    aux_word = ""
    word_list = []
    space = -1
    print("PALABRA INGRESADA: ", word)
    word = word.lower()

    if "-·" in word or "·-" in word:
        #Primero cuento los espacios
        for i in range(0, len(word)):
            if word[i] == " ":
                word_list.append(word[space + 1:i])
                space = i
    else:
        for i in word:
            word_list.append(i)

    return word_list


"""
01
Escribe un programa que muestre por consola (con un print) los números de 1 a 100 
(ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
    - Múltiplos de 3 por la palabra "fizz".
    - Múltiplos de 5 por la palabra "buzz".
    - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
""" 

def fizz_buzz_fizzbuzz():
    number = 1

    while(number <= 100):
        
        if(number % 3 == 0 and number % 5 == 0):
            print("fizzbuzz")
        
        elif(number % 3 == 0):
            print("fizz")
        
        elif(number % 5 == 0):
            print("buzz")

        else:
            print(number)
        
        number += 1

fizz_buzz_fizzbuzz()


"""
02
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
    - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.    
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.
 """
def check_anagrama(first_word, second_word):
    
    if(first_word == second_word):
        print("Las palabras son iguales, no son anagramas")
        return False
    elif(sorted(first_word.lower()) == sorted(second_word.lower())):
        print("Las palabras son anagramas")
        return True
    else:
        print("Las palabras no son anagramas")
        return False

print(check_anagrama("amor", "romannn"))


"""
03
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores. 
0, 1, 1, 2, 3, 5, 8, 13...
 """
def fibonacci_while():
    i = 0
    num_one = 0
    num_two = 1  
    print("\nSERIE DE FIBONACCI BUCLE WHILE")  
    while i < 50:
        print(num_one)
        num_one, num_two, i = num_two, num_one + num_two, i + 1

def fibonacci_for():
    first = 0
    second = 1
    print("\nSERIE DE FIBONACCI CON BUCLE FOR")
    for i in range(0, 50):
        print(first)
        first, second = second, first + second
    
fibonacci_while()
fibonacci_for()


"""
04
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
    - Un numero es primo si y sólo si es divisible por 1 y por si mismo
"""
def prime_number():

    print("\nNUMEROS PRIMOS")

    for number in range(1, 101):                        ##  Recorro los numeros del 1 al 100

        if number >= 2:                                 ##  Si el numero es mayor a 2 NO es numero primo

            prime = False

            for i in range(2, number):                  ##  Recorro los numeros entre el 2 y el numero

                if(number % i == 0):                    ##  Si el resto es cero, el numero es primo

                    prime = True
                    break
            
            if not prime:
                
                print(number)

prime_number()


"""
05
Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
    - La función recibirá por parámetro sólo UN polígono a la vez.
    - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
    - Imprime el cálculo del área de un polígono de cada tipo.
"""
def poligon_area(height, width = 0, triangle = 0):

    if(width > 0 and triangle > 0):
        return "El area del triangulo es: ", ((height * width) / 2)
    
    elif(width > 0):
        return "El area del rectangulo es: ", (height * width)
    
    elif(width == 0):
        return "El area del cuadrado es: ", (height * height)

print(poligon_area(4))
print(poligon_area(4, 3))
print(poligon_area(4, 3, 1))

    
"""
06
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
    - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
def reverse_string(phrase):

    reverse_phrase = ""

    for i in range(1, len(phrase) + 1):
        
        reverse_phrase = reverse_phrase + phrase[-i]
    
    print("\nFRASE ORIGINAL:")
    print(phrase)
    print("\nFRASE REVERTIDA")
    print(reverse_phrase)

reverse_string("Hola a todo el mundo")


"""
07
Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
    - Los signos de puntuación no forman parte de la palabra.
    - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
    - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""
import re, string
def count_words(phrase):

    print("\nCONTAR PALABRAS REPETIDAS")
    spaces = [0]
    words_list = []
    word = ""

    ##  Quito todos los signos de puntuacion de la frase
    phrase = re.sub("[%s]" % re.escape(string.punctuation), '', phrase.lower())

    ## Creo una lista con la  posicion de los espacios
    for i in range(len(phrase)):        
        if phrase[i] == " ":
            spaces.append(i + 1)

    spaces.append(len(phrase) + 1)

    ##  Creo una lista con las palabras de la frase
    for i in range(1, len(spaces)):
        word = phrase[spaces[i - 1] : spaces[i] - 1]
        words_list.append(word)

    ##  Comparo los elementos de la lista 
    ##  Empiezo en el primer elemento
    for i in range(0, len(words_list)):
        ##  Guardo el primer elemento
        first_word = words_list[i]
        ##  Empiezo en el elemento + 1
        for j in range(i + 1, len(words_list)):
            ##  Guardo el elemento i + 1 en word
            word = words_list[j]
            ## Comparo  el elemento i con el elemento i + 1
            if word == first_word:
                ##  Si hay palabras repetidas, retorno
                return "Hay palabras repetidas"

    return "No hay palabras repetidas"

print(count_words("Hola mundo, bienvenidos a mi nuevo proyecto. Yo soy Pablo y programare un programa para contar "
                  "las palabras repetidas. Esto es todo personas programadas, espero que la pases lindo!!"))


"""
08
Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que 
lo hagan directamente.
"""
import math
def decimal_to_binary(number):

    print("\nCONVERTIR DE DECIMAL A BINARIO")

    rest = 0
    list = []
    length = 0
    aux_number = number

    while aux_number >= 1:
        rest = math.trunc(aux_number % 2)
        list.append(rest)
        aux_number = aux_number / 2
        length += 1

    list.reverse()

    return list

print(decimal_to_binary(774))


"""
09
Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en
https://es.wikipedia.org/wiki/Código_morse.
"""
def to_morse_to_text(word):

    print("\nCONVERTIR DE MORSE A TEXTO Y DE TEXTO A MORSE")

    morse = False
    word_morse = ""
    word_text = ""

    if "-·" in word or "·-" in word:
        print("Ingreso un mensaje en morse")
        morse = True
    else:
        print("Ingreso un mensaje en letras")
        morse = False

    word_list = from_string_to_list(word)
    
    for i in range(0, len(word_list)):

        if morse == True:

            if word_list[i] == '·-':
                word_text += 'a'

            elif word_list[i] == '-···':
                word_text += 'b'
            
            elif word_list[i] == '-·-·':
                word_text += 'c'

            elif word_list[i] == '-··':
                word_text += 'd'

            elif word_list[i] == '·':
                word_text += 'e'

            elif word_list[i] == '··-·':
                word_text += 'f'

            elif word_list[i] == '--·':
                word_text += 'g'

            elif word_list[i] == '····':
                word_text += 'h'

            elif word_list[i] == '··':
                word_text += 'i'

            elif word_list[i] == '·---':
                word_text += 'j'

            elif word_list[i] == '-·-':
                word_text += 'k'

            elif word_list[i] == '·-··':
                word_text += 'l'

            elif word_list[i] == '--':
                word_text += 'm'

            elif word_list[i] == '-·':
                word_text += 'n'

            elif word_list[i] == '--·--':
                word_text += 'ñ'

            elif word_list[i] == '---':
                word_text += 'o'

            elif word_list[i] == '·--·':
                word_text += 'p'

            elif word_list[i] == '--·-':
                word_text += 'q'

            elif word_list[i] == '·-·':
                word_text += 'r'

            elif word_list[i] == '···':
                word_text += 's'

            elif word_list[i] == '-':
                word_text += 't'

            elif word_list[i] == '··-':
                word_text += 'u'

            elif word_list[i] == '···-':
                word_text += 'v'

            elif word_list[i] == '·--':
                word_text += 'w'

            elif word_list[i] == '-··-':
                word_text += 'x'
    
            elif word_list[i] == '-·--':
                word_text += 'y'

            elif word_list[i] == '--··':
                word_text += 'z'

            elif word_list[i] == '-----':
                word_text += '0'

            elif word_list[i] == '·----':
                word_text += '1'

            elif word_list[i] == '··---':
                word_text += '2'

            elif word_list[i] == '···--':
                word_text += '3'

            elif word_list[i] == '····-':
                word_text += '4'

            elif word_list[i] == '·····':
                word_text += '5'

            elif word_list[i] == '-····':
                word_text += '6'

            elif word_list[i] == '--···':
                word_text += '7'

            elif word_list[i] == '---··':
                word_text += '8'

            elif word_list[i] == '----·':
                word_text += '9'

            elif word_list[i] == '·-·-·-':
                word_text += '.'

            elif word_list[i] == '--··--':
                word_text += ', '

            elif word_list[i] == '··--··':
                word_text += '? '

            elif word_list[i] == '·-··-·':
                word_text += '"'

            elif word_list[i] == '/':
                word_text += ' '

        else:

            if word_list[i] == 'a':
                word_morse += "·- "

            elif word_list[i] == 'b':
                word_morse += "-··· "
            
            elif word_list[i] == 'c':
                word_morse += "-·-· "

            elif word_list[i] == 'd':
                word_morse += "-·· "

            elif word_list[i] == 'e':
                word_morse += "· "

            elif word_list[i] == 'f':
                word_morse += "··-· "

            elif word_list[i] == 'g':
                word_morse += "--· "

            elif word_list[i] == 'h':
                word_morse += "···· "

            elif word_list[i] == 'i':
                word_morse += "·· "

            elif word_list[i] == 'j':
                word_morse += "·--- "

            elif word_list[i] == 'k':
                word_morse += "-·- "

            elif word_list[i] == 'l':
                word_morse += "·-·· "

            elif word_list[i] == 'm':
                word_morse += "-- "

            elif word_list[i] == 'n':
                word_morse += "-· "

            elif word_list[i] == 'ñ':
                word_morse += "--·-- "

            elif word_list[i] == 'o':
                word_morse += "--- "

            elif word_list[i] == 'p':
                word_morse += "·--· "

            elif word_list[i] == 'q':
                word_morse += "--·- "

            elif word_list[i] == 'r':
                word_morse += "·-· "

            elif word_list[i] == 's':
                word_morse += "··· "

            elif word_list[i] == 't':
                word_morse += "- "

            elif word_list[i] == 'u':
                word_morse += "··- "

            elif word_list[i] == 'v':
                word_morse += "···- "

            elif word_list[i] == 'w':
                word_morse += "·-- "

            elif word_list[i] == 'x':
                word_morse += "-··- "
    
            elif word_list[i] == 'y':
                word_morse += "-·-- "

            elif word_list[i] == 'z':
                word_morse += "--·· "

            elif word_list[i] == '0':
                word_morse += "----- "

            elif word_list[i] == '1':
                word_morse += "·---- "

            elif word_list[i] == '2':
                word_morse += "··--- "

            elif word_list[i] == '3':
                word_morse += "···-- "

            elif word_list[i] == '4':
                word_morse += "····- "

            elif word_list[i] == '5':
                word_morse += "····· "

            elif word_list[i] == '6':
                word_morse += "-···· "

            elif word_list[i] == '7':
                word_morse += "--··· "

            elif word_list[i] == '8':
                word_morse += "---·· "

            elif word_list[i] == '9':
                word_morse += "----· "

            elif word_list[i] == '.':
                word_morse += "·-·-·- "

            elif word_list[i] == ',':
                word_morse += "--··-- "

            elif word_list[i] == '?':
                word_morse += "··--·· "

            elif word_list[i] == '"':
                word_morse += "·-··-· "

            elif word_list[i] == " ":
                word_morse += "/ "

    if morse == True:

        word_text = word_text.replace(word_text[0], word_text[0].upper(), 1)

        for i in range(0, len(word_text)):

            if word_text[i] == "." and (i + 2) < len(word_text):
                word_text = word_text.replace(word_text[i+2], word_text[i+2].upper(), 1)
                print(word_text)               
        
        return word_text
    else:
        word_morse += "·-·-·"
        return  word_morse

print("PALABRA TRADUCIDA A MORSE: ", end = to_morse_to_text("Voy a escribir un texto mas largo. Espero que se entienda un poco mas "
        "lo que estoy haciendo. Tengo 37 anios y me llamo Pablo"))

print("PALABRA TRADUCIDA A MORSE: ", end = to_morse_to_text("Voy a probar algo nuevo. Todavia no se si 48 funciona"))

print("PALABRA TRADUCIDA A TEXTO: ", end = to_morse_to_text("·--· ·- ·-·· ·- -··· ·-· ·- --··-- "
    "/ - ·-· ·- -·· ··- -·-· ·· -·· --- / -·· · / - · -··- - --- --··-- / ·- / -- --- ·-· ··· · ·-·-·- ·-·-·"))

print("PALABRA TRADUCIDA A TEXTO: ", end = to_morse_to_text("···- --- -·-- / ·- / ·--· ·-· --- -··· ·- ·-· / ·- ·-·· --· --- "
    "/ -· ··- · ···- --- ·-·-·- / - --- -·· ·- ···- ·· ·- / -· --- / ··· · / ··· ·· / ····- ---·· / ··-· ··- -· -·-· ·· --- -· ·- ·-·-·"))



