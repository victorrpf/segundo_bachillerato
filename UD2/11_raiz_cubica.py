#Calcular la raíz cúbica de un número sin math y luego con math

# Sin usar math
numero = float(input("Ingrese un número: "))
raiz_cubica = numero ** (1/3)
print("La raíz cúbica de " + str(numero) + " es " + str(raiz_cubica))

# Usando math
import math
raiz_cubica = math.cbrt(numero)
print("La raíz cúbica de " + str(numero) + " es " + str(raiz_cubica))