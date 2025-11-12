# Importar el módulo con la función para calcular la nota media de tres calificaciones
import funciones

# Al importar la función desde otro archivo, no es necesario definirla aquí
#def nota_media(a, b, c):
#    media = (a + b + c) / 3.0
#    estado = 'aprobado' if media >= 5 else 'suspenso'
#    return media, estado # Devuelve una tupla (media, estado)

print("Victor:", funciones.nota_media(5, 10, 7))
print("María:", funciones.nota_media(6, 9, 4))
print("Alberto:", funciones.nota_media(4, 4, 5))