# Importar el módulo json para trabajar con archivos JSON
import json

# Leer el contenido actual del archivo JSON
with open('precios.json', 'r') as file:
    precios = json.load(file)

# Precios que queremos eliminar del diccionario existente
eliminar_precio = {
    "id": 4,
    "precio": 400,
}

# Usamos el método remove para eliminar un precio del array 'lista'
precios["lista"].remove(eliminar_precio)

# Guardar nuevamente el diccionario completo en el archivo JSON
with open('precios.json', 'w') as file:
    json.dump(precios, file)
    print("Precios eliminados del archivo 'precios.json' con éxito.")

# Modos de escritura de archivos:
# 'r' - lectura (predeterminado) 
# 'w' - escritura (sobrescribe el archivo si ya existe)
# 'a' - anexar (agrega contenido al final del archivo si ya existe)
# 'x' - creación exclusiva (crea un archivo nuevo, falla si el archivo ya existe)