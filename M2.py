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
# > descomentar
# col = int(input('Ingrese el número de Columnas: '))
# row = int(input('Ingrese el número de Filas: ')) 
#descomentar < 

#El metodo size es el que se encargará de dibujar la matriz, en este caso con valores vacíos
def size(col,row):
    for i in range(row-1): #nos paseamos por las filas, quitando una, ya que por defecto se dibuja 1 columa y 1 fila
        custom.append('') #le enviamos a nuestro array la cantidad de filas

    for i in range(col): #nos paseamos por las columnas y añadimos cuantas sean recibidas
        x.add_column("",custom)
    print(x) #finalmente se imprime la matriz
#descomentar >
# size(col,row) 
#descomentar <

#https://stackoverflow.com/questions/57247223/how-to-add-borderline-between-row-items-in-prettytable/57247325#57247325
#https://pypi.org/project/prettytable/

print("\n:::::::::::2:::::::::::\n")
#descomentar >
# num = int(input('Ingrese un número entero (1 - 9)')) 


# def esMultiplo(num,check):
#     if num % check == 0:
#         return True
#     else:
#         return False


# def ingreso():
#     for i in range(1,10):
#         if esMultiplo(i,num) == True:
#             i+=1
#         else:
#             check = int(input(f'Ingrese el número {i}: '))
#             if check != i:
#                 print(f'Error: debe ingresar el número: {i}')
#                 break

# ingreso()
#descomentar <

#https://parzibyte.me/blog/2020/12/28/python-multiplo-submultiplo-numero/


print("\n:::::::::::3:::::::::::\n")

# import datetime

# year = int(input('Ingrese el año de nacimiento: '))
# death = int(input('Ingrese el año de muerte (0 si no ha muerto): '))

# def esBisiesto(year):
#     if not year % 4 and (year % 100 or not year % 400):
#         return True
#     else:
#         return False
    

# def cantidad():
#     count = 0
#     firstYear = year

#     if death == 0:
#         today = datetime.date.today()
#         endYear = today.year
#         calc = endYear - year
#     else:
#         calc = death - year

#     for i in range(calc):
#         if esBisiesto(firstYear) == True:
#             count += 1
#         firstYear += 1

#     print(f'La cantidad de años bisiestos que has vivido es: {count}')


# cantidad()

#https://miniwebtool.com/es/leap-years-list/
#https://favtutor.com/blogs/get-current-year-python
#https://www.codigopiton.com/como-saber-si-un-ano-es-bisiesto-en-python/

print("\n:::::::::::4:::::::::::\n")

primera = str(input('Ingrese la primera palabra: '))
segunda = str(input('Ingrese la segunda palabra: '))

while len(segunda) != len(primera):
        print('No tienen el mismo largo :(')
        segunda = str(input('Ingrese la segunda palabra: '))

frase = str(input('Ingrese una frase: '))

first = list(primera)
second = list(segunda)
third = list(frase)

def replace():            
    for i in range(len(third)):
        for j in range(len(first)):
            if third[i] == first[j]:
                third[i] = second[j]
    frase = ''.join(third)
    print(f'La nueva frase es: {frase}')

replace()