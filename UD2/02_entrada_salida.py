# -*- coding: utf-8 -*-
"""
02_entrada_salida.py

Ejemplos de entrada y salida en Python (input/print) con validación básica.
"""

def pedir_entero(prompt):
    """Pide un entero al usuario y valida la entrada."""
    while True:
        texto = input(prompt)
        try:
            return int(texto)
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")


def main():
    print("Ejemplo de entrada/salida")
    nombre = input("Introduce tu nombre: ")
    edad = pedir_entero("Introduce tu edad: ")
    print(f"Hola {nombre}, tienes {edad} años.")

    # Ejemplo de uso: cálculo simple
    anyos_para_100 = 100 - edad
    print(f"Te faltan {anyos_para_100} años para cumplir 100.")


if __name__ == '__main__':
    main()
