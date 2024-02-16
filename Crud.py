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