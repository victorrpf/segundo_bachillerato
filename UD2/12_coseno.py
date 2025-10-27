import math

angulo_grados = 45
angulo_radianes = math.radians(angulo_grados)  # convierte grados a radianes con el método radians
print("El coseno de " +  str(angulo_grados) + " es " + str(math.cos(angulo_radianes)))

# como viene en el libro, sin usar radians
angulo_grados = 45
PI = 3.14159265
angulo_radianes = angulo_grados * PI / 180 # convierte grados a radianes multiplicando por π/180
print("El coseno de " +  str(angulo_grados) + " es " + str(math.cos(angulo_radianes)))