# Importar el módulo json para trabajar con archivos JSON
import json

# Crear un diccionario con algunos datos de ejemplo
dictionary = {
    "precio_1": 100,
    "precio_2": 200,
    "precio_3": 300
}

# Guardar el diccionario en un archivo JSON
# With open abre el archivo cuyo nombre se indica en el primer parámetro, como segundo parámetro se indica el modo de apertura ('w' para escritura)
# w significa que si el archivo no existe, se crea uno nuevo, pero si ya existe, se sobrescribe
# file es el objeto archivo donde se escribirá el contenido, en este caso el diccionario convertido a formato JSON
with open('precios.json', 'w') as file:
    json.dump(dictionary, file) # dump es el método que necesita como primer parámetro el diccionario y como segundo parámetro el objeto archivo
    print("Archivo 'precios.json' creado con éxito.")

# Modos de escritura de archivos:
# 'r' - lectura (predeterminado)
# 'w' - escritura (sobrescribe el archivo si ya existe)
# 'a' - anexar (agrega contenido al final del archivo si ya existe)
# 'x' - creación exclusiva (crea un archivo nuevo, falla si el archivo ya existe)