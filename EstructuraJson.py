import json

# Ejemplo de un objeto JSON
data = '''
{
    "personas": [
        {
            "id": 1,
            "nombre": "Juan",
            "edad": 30
        },
        {
            "id": 2,
            "nombre": "María",
            "edad": 25
        }
    ]
}
'''

# Cargar el objeto JSON en un diccionario de Pythom
objeto_json = json.loads(data)

# Acceder a un valor específico en el JSON
print("Nombre de la persona con ID 1:", objeto_json["personas"][0]["nombre"])

# Filtrar datos en el JSON
for persona in objeto_json["personas"]:
    if persona["edad"] > 28:
        print(f"Persona mayor de 28 años: {persona['nombre']}")

# Crear un nuevo objeto JSON
nuevo_json = {
    "nueva_persona": {
        "id": 3,
        "nombre": "Carlos",
        "edad": 35
    }
}

# Convertir el nuevo objeto JSON a una cadena JSON
nuevo_json_str = json.dumps(nuevo_json, indent=4)
print("\nNuevo objeto JSON:")
print(nuevo_json_str)