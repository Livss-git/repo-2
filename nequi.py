saldo = 0
retirado_total = 0

def ingresar_dinero():
    global saldo
    cantidad = float(input("Ingrese la cantidad a depositar: "))
    saldo += cantidad
    print(f'Se han ingresado {cantidad} unidades. Nuevo saldo: {saldo}')

def retirar_dinero():
    global saldo, retirado_total
    cantidad = float(input("Ingrese la cantidad a retirar: "))
    if cantidad > saldo:
        print('Saldo insuficiente. No se puede retirar.')
    else:
        saldo -= cantidad
        retirado_total += cantidad
        print(f'Se han retirado {cantidad} unidades. Nuevo saldo: {saldo}')

def ver_saldo():
    global saldo
    print(f'Su saldo actual es: {saldo}')

def ver_retirado_total():
    global retirado_total
    print(f'Cantidad total retirada hasta ahora: {retirado_total}')

def mostrar_menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Ver saldo")
        print("4. Ver total retirado")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            ingresar_dinero()
        elif opcion == '2':
            retirar_dinero()
        elif opcion == '3':
            ver_saldo()
        elif opcion == '4':
            ver_retirado_total()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

mostrar_menu()