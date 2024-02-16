import json

json_file = open('Ejercicio.json', 'r')

print("Que desea hacer con esta persona?")
print("")
print("1. Ver datos de la persona")
print("2. Modificar ID")
print("3. Eliminar persona")
print("4. Salir")
modificar_persona = int(input("Ingrese el numero de la opcion que desea realizar: "))

def personas():
    Ejercicio = json.load(json_file)
    print(Ejercicio)
    print("")

    if modificar_persona == 1:
        personas()
    elif modificar_persona == 2:
        print("Modificar ID")
    elif modificar_persona == 3:
        print("Eliminar persona")
    elif modificar_persona == 4:
        print("Salir")