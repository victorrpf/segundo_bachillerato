# Identificadores en Python: ejemplos y reglas

# Ejemplos adaptados de la tabla en C (válidos / no válidos)
# Válidos en C    -> ¿Válidos en Python?
Numero = 123        # Válido en Python (empieza por letra)
dia_del_mes = 15    # Válido (snake_case con guion bajo)
PINGUINO1 = True    # Válido (mayúsculas: convención para constantes)
_ciudad = "Vigo"   # Válido (prefijo _ indica 'privado' por convención)
Z = 'z'             # Válido (identificador corto)

# No válidos en C / ejemplos que causarían problema en Python
# 123   -> no puede ser identificador (comienza por dígito)
# _DÍA -> válido como identificador pero no es recomendable usar mayúsculas con acentos
# numero* -> contiene '*' que no está permitido en identificadores
# 'lugar de nacimiento' -> espacios no permitidos
# año -> contiene 'ñ' (Python admite Unicode pero conviene evitar en código didáctico)

print("Ejemplos válidos en Python:", Numero, dia_del_mes, PINGUINO1, _ciudad, Z)

# Reglas y casos específicos en Python

# 1) No puede empezar por dígito
# 2) Solo letras, dígitos y guion bajo en identificadores válidos (no espacios ni símbolos como '*')
# 3) Python admite identificadores Unicode, por ejemplo con acentos o 'ñ', pero suele evitarse para mantener portabilidad y claridad.

# Recomendaciones:
# - Usar snake_case para variables y funciones.
# - Reservar MAYÚSCULAS para constantes.
