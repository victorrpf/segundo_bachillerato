# Importar el módulo json para trabajar con archivos JSON
import json

# Leer el contenido actual del archivo JSON
with open('precios.json', 'r') as file:
    datos = json.load(file)

# Nuevos datos que queremos agregar al diccionario existente
nuevo_dato = {
    "precio_4": 400,
    "precio_5": 500
}

# Actualizar el diccionario con las nuevas entradas
datos.update(nuevo_dato)

# Guardar nuevamente el diccionario completo en el archivo JSON
with open('precios.json', 'w') as file:
    json.dump(datos, file)

print("Nuevos datos agregados al archivo 'precios.json' con éxito.")

# Modos de escritura de archivos:
# 'r' - lectura (predeterminado)
# 'w' - escritura (sobrescribe el archivo si ya existe)
# 'a' - anexar (agrega contenido al final del archivo si ya existe)
# 'x' - creación exclusiva (crea un archivo nuevo, falla si el archivo ya existe)

