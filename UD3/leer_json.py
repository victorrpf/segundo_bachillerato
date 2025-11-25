# Importar el módulo json para trabajar con archivos JSON
import json

with open('precios.json', 'r') as file:
    precios = json.load(file)  # load es el método que carga el contenido del archivo JSON en un diccionario
    print("Contenido del archivo 'precios.json':")
    print(precios)

# Modos de escritura de archivos:
# 'r' - lectura (predeterminado)
# 'w' - escritura (sobrescribe el archivo si ya existe)
# 'a' - anexar (agrega contenido al final del archivo si ya existe)
# 'x' - creación exclusiva (crea un archivo nuevo, falla si el archivo ya existe)

