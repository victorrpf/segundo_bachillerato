#Calcular la raíz cúbica de un número sin math y luego con math

# Sin usar math
numero = float(input("Ingrese un número entero: "))
raiz_cubica = numero ** (1/3)
print("La raíz cúbica de " + str(numero) + " es " + str(raiz_cubica))

# Redondear a 5 decimales
raiz_cubica = round(raiz_cubica, 5)
print("Redondeada a 5 decimales: " + str(raiz_cubica))

# Usando math
import math
raiz_cubica = math.cbrt(numero)
print("La raíz cúbica de " + str(numero) + " es " + str(raiz_cubica))