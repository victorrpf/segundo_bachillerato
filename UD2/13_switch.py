# Clasifica una nota numérica usando match-case (lo que en otros legunajes se llamaría switch)

nota = float(input("Introduce una nota entre 0 y 10: "))

match nota:
    case nota if nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10.")
    case nota if nota < 5: # Si la nota es menor que 5
        print("Suspenso")
    case nota if nota < 9: # Si la nota es menor que 9
        print("Aprobado")
    case _: # Si no se ha cumplido ninguna de las anteriores condiciones debe ser sobresaliente
        print("Sobresaliente")
