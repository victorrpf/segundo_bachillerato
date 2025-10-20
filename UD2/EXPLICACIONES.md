# Explicaciones — UD2 (Variables, E/S y Control)

01_variables_tipos.py

Este script muestra cómo se definen variables en Python y los tipos básicos: cadenas (`str`), enteros (`int`), números con decimales (`float`) y booleanos (`bool`). Enseña también la función `type()` para comprobar el tipo de una variable y ejemplos de conversión de tipos con `str()`, `int()` y `round()`.

Puntos clave explicados en párrafos:

- Una variable es un nombre que referencia un valor en memoria. En Python no es necesario declarar el tipo previamente; el intérprete lo infiere.
- Diferencia entre `int` y `float`: los enteros no tienen parte fraccionaria, los `float` sí. Convertir `float` a `int` trunca la parte decimal.
- Las cadenas se pueden concatenar con `+` y formatear con f-strings (`f"...{var}..."`).

Ejercicio corto: Cambia los valores de `nombre`, `edad` y `nota_media`. Predice la salida y luego ejecuta el script.

02_entrada_salida.py

Este script introduce la interacción con el usuario mediante `input()` y la salida por pantalla con `print()`. Incluye una función `pedir_entero()` que repite la petición hasta que el usuario introduce un número válido, mostrando cómo gestionar excepciones con `try/except`.

Puntos clave:

- `input()` siempre devuelve una cadena (`str`), por tanto es necesario convertir el valor si queremos un número.
- Uso de `try/except ValueError` para capturar entradas no numéricas.
- Separación de lógica en funciones (`main()` y `pedir_entero()`) para mejorar la legibilidad.

Ejercicio corto: Modifica el script para que también pida la altura en cm y calcule el IMC (índice de masa corporal) simple.

03_control_flujo.py

Contiene ejemplos de condicionales (`if/elif/else`) para clasificar la edad y bucles `for` y `while`. El `for` recorre una lista con `enumerate` para mostrar índices y elementos; el `while` acumula una suma hasta que supera un umbral.

Puntos clave:

- `if` permite ejecutar código condicionalmente. El orden de las condiciones importa.
- `for` itera sobre secuencias (listas, tuplas, cadenas). `enumerate()` es útil cuando necesitamos el índice.
- `while` repite mientras la condición sea verdadera; hay que evitar bucles infinitos.

Ejercicio corto: Escribe una función que reciba una lista de notas (float) y calcule la nota media, devolviendo "Aprobado" o "Suspenso" según la media.
