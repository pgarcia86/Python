##  FUNCIONES AUXILIARES PARA LOS CHALLENGES


import re, string
##  CONVIERTE UN STRING EN UNA LISTA DE STRINGS
def from_string_to_list(word):

    aux_word = ""
    word_list = []
    space = -1
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


##  QUITO LOS ESPACIOS DE LA EXPRESION Y CARACTERES QUE NO NECESITO. ME DEVUELVE UNA LISTA
def take_off_signs(phrase):

    phrase = re.findall('[(\)\[\]\{\}]', phrase)
    return phrase

def from_list_to_string(word_list):

    word_string = ''.join(word_list)
    return word_string

def take_off_spaces(phrase):

    phrase = re.sub('[%s_\ ]' %re.escape(string.punctuation), '', phrase)
    return phrase
