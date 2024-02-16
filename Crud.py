#Primer ejemplo de CRUD en Python

# Definir una clase para representar un elemento en nuestra lista
class Persona:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

# Inicializar una lista vacía para almacenar personas
personas = []

# Función para crear una nueva persona
def crear_persona(id, nombre, edad):
    persona_nueva = Persona(id, nombre, edad)
    personas.append(persona_nueva)
    return persona_nueva

# Función para leer todas las personas
def leer_personas():
    return personas

# Función para leer una persona por su ID
def leer_persona_por_id(id):
    for persona in personas:
        if persona.id == id:
            return persona
    return None

# Función para actualizar una persona por su ID
def actualizar_persona(id, nombre, edad):
    for persona in personas:
        if persona.id == id:
            persona.nombre = nombre
            persona.edad = edad
            return persona
    return None

# Función para eliminar una persona por su ID
def eliminar_persona(id):
    for i, persona in enumerate(personas):
        if persona.id == id:
            del personas[i]
            return True
    return False

# Ejemplo de uso
crear_persona(1, "Juan", 30)
crear_persona(2, "María", 25)

print("Personas creadas:")
for persona in leer_personas():
    print(f"ID: {persona.id}, Nombre: {persona.nombre}, Edad: {persona.edad}")

print("\nActualizando persona con ID 1...")
actualizar_persona(1, "Juan Pérez", 31)

print("Personas actualizadas:")
for persona in leer_personas():
    print(f"ID: {persona.id}, Nombre: {persona.nombre}, Edad: {persona.edad}")

print("\nEliminando persona con ID 2...")
eliminar_persona(2)

print("Personas restantes:")
for persona in leer_personas():
    print(f"ID: {persona.id}, Nombre: {persona.nombre}, Edad: {persona.edad}")


############################################################################################################################
    
# Ejemplo 2 de CRUD en Python
    
import json

# Nombre del archivo JSON
json_file = "personas.json"

# Función para cargar los datos del archivo JSON
def cargar_datos():
    try:
        with open(json_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"personas": []}

# Función para guardar los datos en el archivo JSON
def guardar_datos(data):
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)

# Función para crear una nueva persona
def crear_persona(id, nombre, edad):
    data = cargar_datos()
    nueva_persona = {"id": id, "nombre": nombre, "edad": edad}
    data["personas"].append(nueva_persona)
    guardar_datos(data)
    return nueva_persona

# Función para modificar la información de una persona por su ID
def modificar_persona(id, nombre, edad):
    data = cargar_datos()
    for persona in data["personas"]:
        if persona["id"] == id:
            persona["nombre"] = nombre
            persona["edad"] = edad
            guardar_datos(data)
            return persona
    return None

# Ejemplo de uso
crear_persona(1, "Juan", 30)
crear_persona(2, "María", 25)

# Mostrar personas creadas
print("Personas creadas:")
for persona in cargar_datos()["personas"]:
    print(persona)

# Modificar persona con ID 1
modificar_persona(1, "Juan Pérez", 31)

# Mostrar personas actualizadas
print("\nPersonas actualizadas:")
for persona in cargar_datos()["personas"]:
    print(persona)