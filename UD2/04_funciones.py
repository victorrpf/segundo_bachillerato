# -*- coding: utf-8 -*-
"""
04_funciones.py

Ejemplos de definición y uso de funciones en Python.
"""

def saludar(nombre):
    """Devuelve un saludo para el nombre proporcionado."""
    return f"Hola, {nombre}!"


def es_primo(n):
    """Devuelve True si n es primo, False en caso contrario (n entero >= 2)."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def aplicar_funcion_lista(func, lista):
    """Aplica una función a cada elemento de la lista y devuelve una nueva lista."""
    return [func(x) for x in lista]


def main():
    print(saludar("Alumnado"))

    numeros = [2, 3, 4, 16, 17, 19]
    primos = [n for n in numeros if es_primo(n)]
    print("Números:", numeros)
    print("Primos encontrados:", primos)

    # Usando aplicar_funcion_lista con una lambda
    cuadrados = aplicar_funcion_lista(lambda x: x * x, [1, 2, 3, 4])
    print("Cuadrados:", cuadrados)


if __name__ == '__main__':
    main()
