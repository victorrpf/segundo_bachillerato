# -*- coding: utf-8 -*-
"""
06_regex.py

Ejemplos básicos de expresiones regulares en Python mostrando los cuantificadores:
  +  -> uno o más
  *  -> cero o más
  ?  -> cero o uno (opcional)

Diseñado para alumnos de 2º de Bachillerato.
"""

import re


def ejemplo_mas():
    # + : la letra 'a' una o más veces
    patrón = re.compile(r'a+')
    textos = ['a', 'aa', 'b', 'baaa', '']
    print('\nEjemplo + (uno o más)')
    for t in textos:
        m = patrón.search(t)
        print(f"{t!r} ->", 'match' if m else 'no match')


def ejemplo_asterisco():
    # * : la letra 'a' cero o más veces
    patrón = re.compile(r'a*')
    textos = ['a', 'aa', 'b', 'baaa', '']
    print('\nEjemplo * (cero o más)')
    for t in textos:
        # .search() siempre encuentra, porque a* puede coincidir con cadena vacía
        m = patrón.search(t)
        print(f"{t!r} -> matched '{m.group(0)}'")


def ejemplo_interrogacion():
    # ? : la letra 'a' cero o una vez (opcional)
    patrón = re.compile(r'a?')
    textos = ['a', 'aa', 'b', 'baaa', '']
    print('\nEjemplo ? (cero o una vez)')
    for t in textos:
        m = patrón.search(t)
        print(f"{t!r} -> matched '{m.group(0)}'")


def main():
    print('Demostración de cuantificadores en regex (+, *, ?)')
    ejemplo_mas()
    ejemplo_asterisco()
    ejemplo_interrogacion()


if __name__ == '__main__':
    main()
