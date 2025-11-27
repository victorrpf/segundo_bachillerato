import json

# Abrir el archivo JSON y cargar los datos
with open('precios.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)

# Buscar el elemento con el id que queremos editar
id_a_editar = 3
nuevo_precio = 350
for elemento in datos["lista"]:
    if elemento["id"] == id_a_editar:
        elemento["precio"] = nuevo_precio
        break
else:
    print(f"No se encontró un elemento con id {id_a_editar}")
    exit()

# Guardar nuevamente la lista actualizada en el archivo JSON
with open('precios.json', 'w', encoding='utf-8') as file:
    json.dump(datos, file, indent=4)

print(f"Elemento con id {id_a_editar} actualizado a precio {nuevo_precio}")
