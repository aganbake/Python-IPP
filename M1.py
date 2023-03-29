#Kevin Villarroel

print("\n:::::::::::1:::::::::::\n")
#Convertir grados celcius a fahrenheit

ingreso = str(input('Por favor ingrese los grados Celcius: '))

def grados():
    ingresoToInt = int(ingreso)
    convert = ( ingresoToInt * 1.8 ) + 32
    print(f'\n{ingresoToInt} Grados celcius, son: {convert:.0f} grados Fahrenheit\n')

grados()

print("\n:::::::::::2:::::::::::\n")
#Calcular promedio de 3 números solicitados

A = int(input('Por favor ingrese el primer número: '))
B = int(input('Por favor ingrese el segundo número: '))
C = int(input('Por favor ingrese el tercer número: '))

def promedio():
    calculo = (A + B + C) / 3
    print(f'\nEl promedio es: {calculo:.1f}\n')

promedio()

print("\n:::::::::::3:::::::::::\n")
#calcular notas de un curso en base a parametros

#Contantes

lab = 0.15
clas = 0.15
sol = 0.35
notas = 8
nLab = []
nClas = []
nSol = []

print("""Bienvenido al calculador de notas del curso\n
        En total tenemos 3 tareas de laboratorio, valen 15%,
        3 tareas de clase de 15% y 2 solemnes de 35% c/u.
    """)

for i in range(notas):

    if (i <= 2):
        resp = str(input('Ingrese nota de tarea de laboratorio: '))
        resp = float(resp)
        nLab.append(resp)
    if (i >= 3 and i <= 5):
        resp = str(input(f'Ingrese nota de tarea de clase: '))
        resp = float(resp)
        nClas.append(resp)
    if (i > 5):
        resp = str(input(f'Ingrese nota de solemne: '))
        resp = float(resp)
        nSol.append(resp)

def calculo():
    promLab = 0.0
    promClas = 0.0
    promSol = 0.0
    for i, a in enumerate(nLab):
        promLab += a
    for i, a in enumerate(nClas):
        promClas += a
    for i, a in enumerate(nSol):
        promSol += a

    promLab = (promLab / len(nLab))*lab
    promClas = (promClas / len(nClas))*clas
    promSol = promSol * sol

    promedio = promLab + promClas + promSol

    print(f'\nSu Nota de Presentación es: {promedio:.1f}\n')

calculo()

print("\n:::::::::::4:::::::::::\n")
#calcular el dígito verificador de un número de rut

#Contantes
secuencia = [2,3,4,5,6,7,2,3]
n = 0

rut = str(input('Ingrese un número de RUT: '))
rut = int(rut)

#tests
#26885463-0
#14558655-0
#26885455-K
#14558647-K

def inverso(rut):
    n = 0
    while rut != 0:
        n = 10*n+rut %10
        rut //= 10
    return n

def calculo():
    calc = 0
    numbers = [int(x) for x in str(n)]
    for i, a in enumerate(numbers):
        calc += a*secuencia[i]

    resto = int(calc%11)
    verif = 11-resto

    if verif < 10:
        return verif
    if verif == 10:
        return 'K'
    if verif == 11:
        return '0'

n = inverso(rut)
print(f'\nEl rut con digito verificador es: {rut}-{calculo()}\n') 

print("::::::::::FIN::::::::::")
#repo de github https://github.com/aganbake/Python-IPP.git