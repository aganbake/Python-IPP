#Kevin Villarroel

print("\n:::::::::::1:::::::::::\n")

#Constantes
#Definimos un array vacío para definir la cantidad de filas
custom = []

#Importamos el modulo prettytable, que nos genera la tabla deseada
from prettytable import PrettyTable, ALL
x = PrettyTable() #se define x como nuestra prettytable
x.hrules = ALL #el hrules le dará formato "columna" a la fila, para tener consistencia

#Consultamos por el tamaño de nuestra matriz
col = int(input('Ingrese el número de Columnas: '))
row = int(input('Ingrese el número de Filas: ')) 

#El metodo size es el que se encargará de dibujar la matriz, en este caso con valores vacíos
def size(col,row):
    for i in range(row-1): #nos paseamos por las filas, quitando una, ya que por defecto se dibuja 1 columa y 1 fila
        custom.append('') #le enviamos a nuestro array la cantidad de filas

    for i in range(col): #nos paseamos por las columnas y añadimos cuantas sean recibidas
        x.add_column("",custom)
    print(x) #finalmente se imprime la matriz

size(col,row) 

#https://stackoverflow.com/questions/57247223/how-to-add-borderline-between-row-items-in-prettytable/57247325#57247325
#https://pypi.org/project/prettytable/

print("\n:::::::::::2:::::::::::\n")

num = int(input('Ingrese un número entero (1 - 9)')) 

#definimos el metodo es multiplo, para consultar por un número y devolver true en caso de positiva
def esMultiplo(num,check):
    if num % check == 0: #la formula % == 0 nos dirá si el número es multiplo
        return True
    else:
        return False

#def ingreso para iniciar base número seleccionado
def ingreso():
    for i in range(1,10):
        if esMultiplo(i,num) == True: #verificamos si el número escogido y la actual posición es multiplo
            i+=1 #si lo es, el for crece y así podemos continuar saltando el multiplo
        else:
            check = int(input(f'Ingrese el número {i}: ')) #si no es multiplo de acuerdo al global, solicita  ingresar el número
            if check != i: #si el número es distinto de la posición del for, se rompe el ciclo y finaliza el programa
                print(f'Error: debe ingresar el número: {i}')
                break

ingreso()

#https://parzibyte.me/blog/2020/12/28/python-multiplo-submultiplo-numero/


print("\n:::::::::::3:::::::::::\n")

#ya que hay que verificar el año y no queremos hacerlo manual, importamos la libreria datetime para obtener el año de la maquina
import datetime

year = int(input('Ingrese el año de nacimiento: '))
death = int(input('Ingrese el año de muerte (0 si no ha muerto): '))

#definimos método esBisiesto para verificar si el año enviado cumple con los parametros
def esBisiesto(year):
    if not year % 4 and (year % 100 or not year % 400): #con esta formula vemos si el año es multiplo de 4 y el año es multiplo de 100 pero no de 400, así se determina el bisiesto
        return True
    else:
        return False
    
#el metodo cantidad nos dará la cantidad de bisiestos durante los años de vida
def cantidad():
    count = 0
    firstYear = year

    if death == 0:
        today = datetime.date.today()
        endYear = today.year
        calc = endYear - year #esto verifica si está vivo, usa el año actual, sino el deja el ingresado
    else:
        calc = death - year

    for i in range(calc):
        if esBisiesto(firstYear) == True:
            count += 1
        firstYear += 1 #acá los respectivos contadores, el año para ir verificando cuantos años tenga de vida y un contador para cada bisiesto que llegó "True"

    print(f'La cantidad de años bisiestos que has vivido es: {count}')


cantidad()

#https://miniwebtool.com/es/leap-years-list/
#https://favtutor.com/blogs/get-current-year-python
#https://www.codigopiton.com/como-saber-si-un-ano-es-bisiesto-en-python/

print("\n:::::::::::4:::::::::::\n")

primera = str(input('Ingrese la primera palabra: '))
segunda = str(input('Ingrese la segunda palabra: '))

while len(segunda) != len(primera): #acá verificamos si ambas palabras son del mismo tamaño, sino continuará hasta satisfascer la petición
        print('No tienen el mismo largo :(')
        segunda = str(input('Ingrese la segunda palabra: '))

frase = str(input('Ingrese una frase: '))
#en estos 3 campos a continuación convertimos los string a listas, para usarlos en el metodo
first = list(primera) 
second = list(segunda)
third = list(frase)
#se define el metodo replace, que verificará el tamaño de la frase y verificará cada palabra con las palabras ingresadas
def replace():            
    for i in range(len(third)):
        for j in range(len(first)):
            if third[i] == first[j]:
                third[i] = second[j] #acá lo mas importante, ya que al la primera y segunda palabra ser iguales, el reemplaza la que sea igual con la correspondiente en la segunda palabra
    frase = ''.join(third)
    print(f'La nueva frase es: {frase}')

replace()

#https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python

#Fin :)