
# Explicaciones — UD2 (Variables, E/S y Control)

00_hola_mundo.py

Este script es un primer ejemplo sencillo que muestra salida por pantalla usando `print()` y demuestra:

- Uso de caracteres especiales como salto de línea (`\n`) y tabulación (`\t`).
- Cómo incluir comillas simples, dobles y el carácter de acento grave (backtick) dentro de cadenas.
- Uso de funciones `ord()` y `chr()` para convertir entre caracteres y sus códigos Unicode/ASCII.

Contenido y explicación línea por línea:

1. `print("Hola\nMundo\t➡\tTabulado");`
    - `\n` inserta un salto de línea, por eso la palabra "Mundo" aparece en la línea siguiente.
    - `\t` inserta una tabulación. El carácter `➡` es solo un ejemplo de un símbolo Unicode y mostrará correctamente si la consola soporta UTF-8.
    - Nota: el punto y coma `;` al final de la línea no es necesario en Python pero no provoca error; puede eliminarse para estilo más "pythónico".

2. `print("Comillas: 'simple', \"doble\", `invertida` (como texto)");`
    - Muestra cómo escribir comillas simples y dobles dentro de una cadena. Las comillas dobles que rodean la cadena permiten usar `'` sin escapar.
    - En este ejemplo hay backticks (acento grave) dentro de la cadena; si se quisiera usar backticks en el código fuente tal cual, no hace falta escaparlos.

3. `print("Código ASCII de 'A':", ord('A'), "⇄ chr(65):", chr(65))`
    - `ord('A')` devuelve el código entero correspondiente al carácter 'A' (65 en ASCII/Unicode).
    - `chr(65)` devuelve el carácter asociado al código 65.
    - Este ejemplo muestra la relación entre caracteres y sus códigos numéricos.

Ejercicio sugerido: Modifica el script para que pida al usuario un carácter y muestre su código con `ord()`, y luego pida un número y muestre el carácter con `chr()`.

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

04_funciones.py

Este script explora cómo declarar y usar funciones en Python. Incluye:

- Definición simple de función (`saludar`).
- Función con lógica más compleja (`es_primo`) que comprueba si un número es primo.
- Uso de funciones de orden superior: `aplicar_funcion_lista` que recibe una función y una lista.

Puntos clave:

- Las funciones agrupan comportamiento y facilitan la reutilización y las pruebas.
- Las lambdas son funciones anónimas útiles para operaciones pequeñas y puntuales.
- Separar la lógica en funciones pequeñas mejora la legibilidad.

Ejercicio corto: Escribe una función `factorial(n)` que calcule el factorial de `n` y otra que use `factorial` para calcular combinaciones (n choose k).

05_colecciones.py

Contiene ejemplos de las principales colecciones en Python: listas (mutables y con comprehensions), tuplas (inmutables) y diccionarios (mapas clave->valor).

Puntos clave:

- Listas: añadir, eliminar y recorrer elementos; comprehensions para construir nuevas listas.
- Tuplas: uso cuando no queremos que los datos cambien; se pueden desempaquetar en variables.
- Diccionarios: acceso por clave, iteración con `.items()` y utilidades comunes.

Ejercicio corto: Dada una lista de palabras, crea un diccionario que cuente la frecuencia de cada palabra (histograma).

Instrucciones de ejecución (Visual Studio Code / LliureX)

Abre la carpeta del proyecto en Visual Studio Code y usa el terminal integrado (Ver > Terminal). Sitúate en la carpeta `UD2` si es necesario y ejecuta:

```bash
# Ejecutar los scripts desde la terminal integrada
python3 00_hola_mundo.py
python3 01_variables_tipos.py
python3 02_entrada_salida.py
python3 03_control_flujo.py
```

Notas:
- En entornos Linux (incluido LliureX) el intérprete suele invocarse como `python3`; comprueba la versión con `python3 --version`.
- Los archivos usan codificación UTF-8 para soportar acentos y caracteres especiales.
