# Kevin Villarroel

print("\n:::::::::::1:::::::::::\n")

import re  # importamos la librería re, para buscar dentro del texto

while True:  # solo para validar que no entre un input vacío
    pw = input(
        "Ingrese una clave para comprobar: \n"
    )  # solicitamos al usuario ingresar una clave para comprobar
    if pw:
        break


def check_pw(pw):  # se define la función check_pw que recibirá lo ingresado por usuario
    # se almacena y busca la clave en base a true o false
    largo = len(pw) < 8  # clave mas pequeña que 8 carácteres
    num = re.search(r"\d", pw) is None  # no encuentra números
    mayus = re.search(r"[A-Z]", pw) is None  # no encuentra mayúsculas
    minus = re.search(r"[a-z]", pw) is None  # no encuentra minúsculas

    pwOk = not (
        largo or num or mayus or minus
    )  # si nada de lo anterior se cumple, devuelve True

    if pwOk == True:  # si es True, nos avisa
        print("La clave es segura")
    else:
        print("La clave no es segura")


check_pw(pw)

# https://www.guru99.com/python-regular-expressions-complete-tutorial.html

print("\n:::::::::::2:::::::::::\n")

nums = []

while True:
    num = str(input("Ingrese un número: "))

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
    print(calc)


sum()

print("\n:::::::::::3:::::::::::\n")

cuentas = []  # creamos un arreglo para almacenar las cuenta
create = True  # definimos una variable booleana para la creación o revisión de cuentas


class Cuenta:  # Creamos la clase cuenta
    def __init__(
        self, numero_cuenta, nombre_titular, saldo_inicial, tipo_cuenta
    ):  # definimos la instancia init con los parametros
        self.numero_cuenta = numero_cuenta  # almacenamos los parametros
        self.nombre_titular = nombre_titular
        self.saldo_inicial = saldo_inicial
        self.tipo_cuenta = tipo_cuenta

    def depositar(
        self, cantidad
    ):  # definimos la clase para depositar, donde se recibe un monto y se almacena en el init
        self.saldo_inicial += cantidad

    def retirar(
        self, cantidad
    ):  # definimos el retiro, donde verifica si la cantidad es suficiente
        if cantidad > self.saldo_inicial:
            print("Saldo insuficiente")
        else:
            self.saldo_inicial -= cantidad

    def obtener_balance(
        self,
    ):  # definimos el balance, así retornamos el saldo de la cuenta
        return self.saldo_inicial


while create == True:  # creamos un menú que se repetirá hasta que se seleccione el 5
    option = int(
        input(
            """
1 - Crear Cuenta
2 - Depositar
3 - Retirar
4 - Saldo
5 - Salir
            \n
        """
        )
    )

    if (
        option == 1
    ):  # en la opción una, creamos un objeto cuenta y lo almacenamos en el arreglo
        account = str(input("Número de cuenta: "))
        name = str(input("Nombre Usuario: "))
        initial = int(input("Saldo inicial: "))
        type = str(input("Tipo de cuenta: "))

        cuentas.append(Cuenta(account, name, initial, type))  # acá almacenmos

    if option == 2:  # si la opción es 2, se deposita el monto
        account = str(input("Número de cuenta: "))
        ammount = int(input("Monto a depositar: "))

        for (
            obj
        ) in (
            cuentas
        ):  # pero buscamos la cuenta en el arreglo, donde haga match llama a la función depositar
            if obj.numero_cuenta == account:
                obj.depositar(ammount)

    if option == 3:  # acá vamos a retirar fondos
        account = str(input("Número de cuenta: "))
        ammount = int(input("Monto a retirar: "))

        for (
            obj
        ) in (
            cuentas
        ):  # siguiendo la dinámica busca la cuenta y retirar el monto que decidan (si excede el monto la función se encargará de eso)
            if obj.numero_cuenta == account:
                obj.retirar(ammount)

    if (
        option == 4
    ):  # acá traemos el saldo, iba a llamar a la función, pero encontré mas limpio imprimir toda la cuenta
        account = str(input("Número de cuenta: "))

        for obj in cuentas:
            if obj.numero_cuenta == account:
                print(
                    f"""
*************************************
Número de cuenta: {obj.numero_cuenta}
Nombre de usuario: {obj.nombre_titular}
Saldo: {obj.saldo_inicial}
Tipo de cuenta: {obj.tipo_cuenta}
*************************************
                """
                )
                # obj.obtener_balance(account) #igual lo dejo acá
            else:
                print("Cuenta no existe")

    if option == 5:  # finalmente si quieren salir, acá cambió el create a False
        print("Gracias por su visita")
        create = False

    if (
        option == 0
    ):  # como no hay un login de "admin" entonces está como una opción secreta las cuentas y saldos :)
        print("Menú secreto, cuentas existentes y su saldo: ")

        for obj in cuentas:
            print(
                f"""
*************************************
Número de cuenta: {obj.numero_cuenta}
Nombre de usuario: {obj.nombre_titular}
Saldo: {obj.saldo_inicial}
Tipo de cuenta: {obj.tipo_cuenta}
*************************************
                """
            )
# fin :)
# repo: https://github.com/aganbake/Python-IPP
