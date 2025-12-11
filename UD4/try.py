a = 5
b = 0
# A través de esta comprobación prevenimos que se divida entre cero.
if b!=0:
    print(a/b)
else:
    print("No se puede dividir!")

try:
    # Nos saltamos la comprobación condicional y forzamos ZeroDivisionError
    print(a/b)
except:
    print("Esta línea sí se ejecuta porque está antes del raise")
    #raise ZeroDivisionError("Relanzamos ZeroDivisionError con información personalizada")
    print("Esta línea no se ejecuta porque está después del raise")

try:
    # Forzamos NameError usando una variable no definida
    print(valor_inexistente)
except:
    print("Capturamos el NameError antes del raise")
    #raise NameError("Relanzamos NameError con información personalizada")
    print("No se ejecuta porque está después del raise")

# En este try/except solo mostramos el mensaje y continuamos, a diferencia del bloque de líneas 9-16 donde re-lanzamos ZeroDivisionError.
try:
    print(a/b)
except ZeroDivisionError:
    print("No se ha podido realizar la división")

# Aquí manejamos NameError sin raise adicional, mientras que el bloque de líneas 17-23 vuelve a lanzar la excepción para detener la ejecución.
try:
    print(valor_inexistente)
except NameError:
    print("No se ha podido acceder a la variable")

try:
    #c = 5/0       # Si comentas esto entra en TypeError
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except ZeroDivisionError:
    print("No se puede dividir entre cero!")
except TypeError:
    print("Problema de tipos!")

try:
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except Exception as ex:
    print("Ha habido una excepción", type(ex))
    # Ha habido una excepción <class 'TypeError'>

try:
    # Forzamos excepción
    x = 2/0
except:
    # Si entra en except, no entra en else
    print("Entra en except, ha ocurrido una excepción")
else:
    # Si entra en else, no entra en except
    print("Entra en el else, no ha ocurrido ninguna excepción")
finally:
    # También entra porque finally es ejecutado siempre
    print("Entra en finally, se ejecuta el bloque finally")

# Se intenta abrir un fichero y se captura una posible excepción
try:
    with open("fichero.txt") as file:
        read_data = file.read()
# Excepción de tipo OSError si el fichero no existe
except OSError:
    print("OSError. No se pudo abrir")

# ValueError al convertir una cadena no numérica a entero
try:
    x = int(input("Escribe un número: "))
except ValueError:
    print("Eso no era un número.")
else:
    print("Has escrito", x)
finally:
    print("Hecho.")

"""
try:
    print("Hola"))
except SyntaxError:
    print("Hay un error de sintaxis")"""