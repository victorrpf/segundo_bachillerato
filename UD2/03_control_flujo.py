# -*- coding: utf-8 -*-
"""
03_control_flujo.py

Ejemplos de condicionales y bucles en Python.
"""

def ejemplo_condicional(edad):
    if edad < 18:
        return "Menor de edad"
    elif edad < 65:
        return "Adulto"
    else:
        return "Persona mayor"


def ejemplo_bucles():
    frutas = ["manzana", "plátano", "pera"]
    print("Listado de frutas:")
    for i, f in enumerate(frutas, start=1):
        print(i, f)

    # while: sumar números hasta que la suma supere 20
    suma = 0
    n = 1
    while suma <= 20:
        suma += n
        n += 1
    print("Suma acumulada mayor que 20:", suma)


def main():
    print("Control de flujo: condicionales y bucles")
    edad = 20
    print("Edad ejemplo:", edad, "->", ejemplo_condicional(edad))
    ejemplo_bucles()


if __name__ == '__main__':
    main()
