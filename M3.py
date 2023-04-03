#Kevin Villarroel

print("\n:::::::::::1:::::::::::\n")

err = True #Definimos una variable booleana para el ciclo de repetición y verificación del valor ingresado
nums = [] #Definimos un array en blanco para guardar los números ingresados

def order(): #se define el metodo order, para ordenar e imprimir los números en en orden ascendente
    nums.sort()
    print(nums)

while err == True: #incia el ciclo de consultas
    num = str(input('Ingrese un número: ')) #se pide ingresar string, para luego validar como entero
    try: #usamos el método try-except para validar que lo ingresado es efecitivamente un número
        num = int(num)
        if num != 0: #si el número es distinto de 0, lo guardamos en el array
            nums.append(num)
        else: #si el número es 0, damos por finalizado, pero este no se guarda en el array
            err = False
            order()
    except ValueError: #mensaje de error en caso de ser algo distinto a un entero
        print('El valor debe ser un número')
        err = True #se mantiene la variable booleana en true para no romper el ciclo aunque haya error
    if len(nums) == 20: #por defecto hasta 20 números o hasta 0, lo que ocurra primero
        err = False
        order()

#https://www.programiz.com/python-programming/methods/list/sort

print("\n:::::::::::2:::::::::::\n")

err = False
words = [] #definimos un array para almacenar las palabras

def checkWord(word): #se define el metodo checkword que recipe una palabra a verificar
    if word not in words: #si la palabra no es parte del array global, la añade, sino la salta
        words.append(word)

while err == False: #mientras el usuario no ingrese '***' el ciclo continua
    word = str(input('Ingrese una palabra: '))
    if word != '***': #Si no se ingresa '***' se ejecuta el metodo checkword para validar y añadir la palabra
        checkWord(word)
    else:
        err = True #en caso de que se escriba *** se cierra el programa y se imprime el array con las palabras únicas
        print(words)


print("\n:::::::::::3:::::::::::\n")

puntaje = {1:{'A','E','I','L','N','O','R','S','T','U'},
           2:{'D','G'},
           3:{'B','C','M','P'},
           4:{'F','H','V','W','Y'},
           5:{'K'},
           8:{'J','X'},
           10:{'Q','Z'}} #se define un diccionario con las letras y el puntaje, siguiendo el Key (letra) Value (Puntaje)

print("""
        ¡Juguemos Scrabble!

        """) #mensaje de bienvenida
palabra = str(input('Ingrese una palabra para verificar el puntaje :)\n> ')) 
word = list(palabra.upper()) #pasamalos la palabra a Mayúscula, para poder validar en el diccionario
puntos = [] #acá guardaremos los puntajes de cada letra

def checkWord(): #el metodo checkword se paseará por el diccionario para obtener los puntajes
    calc = 0
    flag = False
    for i in range(len(word)): #acá hacemos un for para ver el largo de la palabra ingresada
        check = [ key for key, value in puntaje.items() if word[i] in value] #con esta formula nos pasaremos letra por letra para verificar que la ingresada por usuario existe
        if (check): #si es verdero y existe, añadirá el puntaje al array de puntos
            puntos.append(check[0])
        else:
            flag = True #si no dejo una bandera para luego mostrar un mensaje personalizado, ya que no rompera el ciclo
    for i in range(len(puntos)): #luego valido los puntos y voy sumando cada uno para dar un valor final
        calc += int(puntos[i])
    if flag == False: #si no hay bandera, imprime el puntaje de la palabra
        print(f'\nLa palabra vale: {calc} puntos')
    else: #si hay bandera, los valores de caracteres invalidos, fueron saltados, por ejemplo (1,ñ u * )
        print(f'\nLa palabra vale: {calc} puntos, aunque hay caracteres no válidos ingresados :(')

checkWord() #se da inicio al scrabble

#https://thispointer.com/python-dictionary-with-multiple-values-per-key/


print("\n:::::::::::4.1:::::::::::\n")


wordA = str(input("Ingresa una palabra: ")) #se solicita ingresar las palabras
wordB = str(input("Ingresa otra palabra: "))

def esAnagrama(wordA, wordB): #se define el metodo esAnagrama, que recibirá ambas palabras para verificar

    wordA = list(wordA.lower()) #las convertimos a una lista y a minúsculas solo para asegurar la comparación
    wordB = list(wordB.lower())

    wordA.sort() #ordenamos nuestra lista
    wordB.sort()

    wordA = "".join(wordA) #juntamos las palabras para quitar los espacios en blanco, así queda un string
    wordB = "".join(wordB)

    return wordA == wordB #comparamos los string, si es verdadero es anamagrama

checkWord = esAnagrama(wordA, wordB) #damos inicio al metodo con las palabras

if checkWord: #si el return fue verdadero, nos indica si fue o no anagrama
    print(f"{wordA} es anagrama de {wordB}")
else:
    print(f"{wordA} NO es anagrama de {wordB}")


print("\n:::::::::::4.2:::::::::::\n")


err = False #definimos variable booleana para el ciclo de verificación
nums = [] #definimos un array para almacenar los números a sumar

print("""Bienvenido a la sumatoria de números, 
si no desea continuar, no ingrese ningún número 
y presione ENTER\n""")

def sum(): #se define el método sum que se ejecutará cuando ya no hayan más números para sumar
    calc = 0
    for i in range(len(nums)): #nos paseamos por el tamaño del array nums
        calc += int(nums[i]) #se suma cada uno de lo que ya está validado
    print(f'La suma de los números ingresados es: {calc}')

while err == False: #se solicita ingresar número, a menos que no sea número, no se guarda
    num = str(input('Ingrese un número: '))
    if num != "": #si no está en blanco, se siguen solicitando números
        try: #con el try except, validamos que efectivamente lo ingresado es un número
            num = int(num)
            nums.append(num)
        except ValueError:
            print('Error: Eso no es un número :(\n')
    else:
        err = True
        sum() #finalmente, si no hay mas números, llamamos el metodo sum

#Fin :)