#Kevin Villarroel

print("\n:::::::::::1:::::::::::\n")

import re #importamos la librería re, para buscar dentro del texto

while True: #solo para validar que no entre un input vacío
    pw = input('Ingrese una clave para comprobar: \n')#solicitamos al usuario ingresar una clave para comprobar
    if pw:
        break

def check_pw (pw): #se define la función check_pw que recibirá lo ingresado por usuario
    #se almacena y busca la clave en base a true o false
    largo = len(pw) < 8 #clave mas pequeña que 8 carácteres
    num = re.search(r"\d", pw) is None #no encuentra números
    mayus = re.search(r"[A-Z]",pw) is None #no encuentra mayúsculas
    minus = re.search(r"[a-z]",pw) is None #no encuentra minúsculas

    pwOk = not (largo or num or mayus or minus) #si nada de lo anterior se cumple, devuelve True

    if pwOk == True: #si es True, nos avisa
        print('La clave es segura')
    else:
        print('La clave no es segura')
        

check_pw(pw)

#https://www.guru99.com/python-regular-expressions-complete-tutorial.html

print("\n:::::::::::2:::::::::::\n")

nums = []

while True:
    num = str(input('Ingrese un número: '))

    if num == "":
        if nums == "":
            nums.append(0)
        break
    else:
        nums.append(int(num))
    
def sum():
    calc = 0
    for i in range(len(nums)):
        calc += nums[i]
    print (calc)
sum()

print("\n:::::::::::3:::::::::::\n")