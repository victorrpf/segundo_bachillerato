# -*- coding: utf-8 -*-
"""
01_variables_tipos.py

Ejemplos básicos de variables y tipos en Python.
Diseñado para alumnos de 2º de Bachillerato.
"""

# Asignación de variables
nombre = "María"
edad = 17
nota_media = 8.5
es_estudiante = True

# Imprimir valores y tipos
print("Nombre:", nombre)
print("Edad:", edad, "-> tipo:", type(edad))
print("Nota media:", nota_media, "-> tipo:", type(nota_media))
print("¿Es estudiante?:", es_estudiante, "-> tipo:", type(es_estudiante))

# Conversión de tipos
edad_texto = str(edad)
nota_entera = int(nota_media)  # pierde la parte decimal
nota_redondeada = round(nota_media)  # redondea al entero más cercano

print("Edad como texto:", edad_texto, "(tipo:", type(edad_texto), ")")
print("Nota convertida a int (truncada):", nota_entera)
print("Nota redondeada:", nota_redondeada)

# Operaciones con cadenas
saludo = "Hola, " + nombre
saludo2 = f"{nombre} tiene {edad} años."
print(saludo)
print(saludo2)

# Ejercicio sugerido (comentado):
# Pide al alumno que cambie los valores y prediga la salida antes de ejecutar.
