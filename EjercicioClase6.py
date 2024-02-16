# Preguntar producto y catidad al usuario
print ("Bienvenido a la tienda el porton, tenemos los siguientes productos: ")
producto = {
    'Empanada' : 3000,
    'Perro' : 10000,
    'Arepa' : 4000,
    'Pastel de pollo' : 5000
}
for llave , valor in producto.items():
    print(llave,valor)
    
    
seleccion = input("\nIntroduce el producto que deseas comprar: ")

cantidad = int(input(f"¿Cuántas unidades de {seleccion} deseas comprar? "))
if cantidad < 0:
    print("Por favor, introduce una cantidad válida.")
    
costototal = producto[seleccion] * cantidad
print(f"Has agregado {cantidad} de {seleccion} con un costo total de ${costototal}")
totalCompra=0
totalCompra = totalCompra+costototal