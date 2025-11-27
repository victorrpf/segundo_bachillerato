# Importar el módulo json para trabajar con archivos JSON
import json

# Leer el contenido actual del archivo JSON
with open('precios.json', 'r') as file:
    precios = json.load(file)

# Nuevos precios que queremos agregar al diccionario existente
nuevo_precio = {
    "id": 4,
    "precio_4": 400,
}

# Actualizar el diccionario con las nuevas entradas
# Usamos el método append para agregar el nuevo precio al array 'lista'
precios["lista"].append(nuevo_precio)

# Guardar nuevamente el diccionario completo en el archivo JSON
with open('precios.json', 'w') as file:
    json.dump(precios, file)
print("Nuevos precios agregados al archivo 'precios.json' con éxito.")

# Modos de escritura de archivos:
# 'r' - lectura (predeterminado) 
# 'w' - escritura (sobrescribe el archivo si ya existe)
# 'a' - anexar (agrega contenido al final del archivo si ya existe)
# 'x' - creación exclusiva (crea un archivo nuevo, falla si el archivo ya existe)