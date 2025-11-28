# Importar el módulo json para trabajar con archivos JSON
import json

# Leer el contenido actual del archivo JSON
with open('precios.json', 'r') as file:
    precios = json.load(file)

# Precios que queremos editar del diccionario existente
editar_precio = {
    "id": 4,
    "precio": 400,
}

# Usamos el método remove para eliminar un precio del array 'lista'
precios["lista"].remove(editar_precio)

# Agregar el precio eliminado con los nuevos valores
editar_precio_actualizado = {
    "id": 4,
    "precio": 450,
}

# Usamos el método append para agregar el nuevo precio al array 'lista'
precios["lista"].append(editar_precio_actualizado)

# Guardar nuevamente el diccionario completo en el archivo JSON
with open('precios.json', 'w') as file:
    json.dump(precios, file)
    print("Precios editados del archivo 'precios.json' con éxito.")

# Modos de escritura de archivos:
# 'r' - lectura (predeterminado) 
# 'w' - escritura (sobrescribe el archivo si ya existe)
# 'a' - anexar (agrega contenido al final del archivo si ya existe)
# 'x' - creación exclusiva (crea un archivo nuevo, falla si el archivo ya existe)