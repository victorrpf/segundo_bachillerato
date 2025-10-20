# -*- coding: utf-8 -*-
"""
05_colecciones.py

Ejemplos de colecciones en Python: listas, tuplas y diccionarios.
"""

def main():
    # Listas
    frutas = ["manzana", "plátano", "pera"]
    frutas.append("naranja")
    print("Lista de frutas:", frutas)

    # Tuplas (inmutables)
    coordenada = (10, 20)
    print("Coordenada:", coordenada)

    # Diccionarios
    alumno = {"nombre": "Luis", "edad": 18, "nota": 7.5}
    print("Alumno:", alumno)
    print("Nombre del alumno:", alumno["nombre"])

    # Iterar por diccionario
    for clave, valor in alumno.items():
        print(clave, "->", valor)

    # Comprensiones
    cuadrados = [x * x for x in range(1, 6)]
    print("Cuadrados:", cuadrados)


if __name__ == '__main__':
    main()
