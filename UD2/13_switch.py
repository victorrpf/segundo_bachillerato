# Clasifica una nota numérica usando match-case (lo que en otros legunajes se llamaría switch)

nota_texto = float(input("Introduce una nota entre 0 y 10: "))

match nota_texto:
    case n if n < 0 or n > 10:
        print("La nota debe estar entre 0 y 10.")
    case n if n < 5:
        print("Suspenso")
    case n if n < 9:
        print("Aprobado")
    case _:
        print("Sobresaliente")
