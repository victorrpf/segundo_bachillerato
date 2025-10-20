
# Explicaciones — UD2 (según índice del PDF)

01_caracteres.py

Contenido: ejemplos de cadenas y caracteres, incluyendo escapes (`\n`, `\t`), comillas, conversión entre caracteres y códigos (`ord`/`chr`) y uso de backspace (`\b`).

Explicación adaptada al contenido actual del script:

- Salto de línea (`\n`) y tabulación (`\t`): `print("Hola\nMundo\t➡\tTabulado")` muestra "Mundo" en la línea siguiente y usa una tabulación.
- Comillas: se puede incluir `'` dentro de una cadena entre dobles comillas y viceversa; si hace falta, se escapan con `\`.
- `ord(c)` y `chr(n)`: permiten convertir entre carácter y su código Unicode/ASCII.
- Backspace (`\b`): el script muestra `print("Backspace: 123456\b78")`.
	- `\b` es un carácter de control (backspace) que en la salida de la terminal mueve el cursor una posición atrás; el comportamiento exacto depende del terminal. En muchas consolas `123456\b78` aparecerá visualmente como `12378` porque el `\b` retrocede sobre el `6` y luego se escribe `78`.

02_identificadores.py

Contenido: ejemplos y reglas extraídas del script actual.

Explicación adaptada al contenido del script:

- Ejemplos válidos en Python (adaptados desde la tabla en C): `Numero`, `dia_del_mes`, `PINGUINO1`, `_ciudad`, `Z`.
- Elementos no válidos o problemáticos: no se pueden usar identificadores que comiencen por dígitos (p. ej. `123`), no se permiten espacios ni símbolos como `*` en los nombres, y aunque Python admite Unicode (`ñ`, acentos), su uso no es recomendable en código didáctico por cuestiones de portabilidad.
- Reglas clave:
	1. No puede empezar por dígito.
	2. Solo letras, dígitos y guion bajo en identificadores válidos (sin espacios ni símbolos).
	3. Python admite identificadores Unicode, pero suele evitarse cuando se comparte código.

Recomendaciones pedagógicas (incluidas en el script):
- Usar `snake_case` para variables y funciones.
- Reservar MAYÚSCULAS para constantes.


03_palabras_reservadas.py

Contenido: listado y explicación de las palabras reservadas del lenguaje.

Breve explicación:

- Las palabras reservadas (como `if`, `for`, `while`, `def`, `class`, `import`, etc.) tienen un significado sintáctico en Python y no pueden usarse como identificadores.
- Usa `import keyword; keyword.kwlist` para ver la lista actual en la versión de Python instalada.

04_variables_constantes.py

Contenido: tipos básicos y ejemplos de variables y constantes.

Breve explicación:

- Tipos básicos: `int`, `float`, `str`, `bool`. Python es dinámico, la variable toma el tipo del valor asignado.
- Conversión explícita entre tipos: `str()`, `int()`, `float()` y funciones como `round()` para redondear.
- Constantes por convención: nombres en MAYÚSCULAS (p. ej. `PI = 3.14`), aunque Python no impone inmutabilidad.

05_arrays.py

Contenido: listas en Python (creación, acceso, métodos y comprehensions).

Breve explicación:

- Listas son colecciones ordenadas y mutables. Operaciones comunes: `append`, `pop`, indexación y slicing.
- Comprehensions permiten construir listas de forma compacta: `[x*x for x in range(5)]`.

06_comentarios.py

Contenido: comentarios de línea y docstrings.

Breve explicación:

- Los comentarios de línea usan `#` y se ignoran en la ejecución. Los docstrings (triple comillas) documentan módulos, funciones o clases.
- Es buena práctica documentar las funciones con un docstring corto que explique su propósito y parámetros.

07_expresiones.py

Contenido: expresiones y operadores aritméticos y lógicos.

Breve explicación:

- Operadores aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- Operadores lógicos: `and`, `or`, `not`. Comparaciones: `==`, `!=`, `<`, `>`, `<=`, `>=`.

08_sentencias.py

Contenido: sentencias de control de flujo: `if/elif/else`, `for` y `while`.

Breve explicación:

- `if` permite ejecutar código condicionalmente; `for` itera sobre secuencias; `while` repite mientras la condición sea verdadera.
- Evitar bucles infinitos y preferir `for` cuando se itera sobre colecciones.

09_funciones.py

Contenido: introducción a la definición y uso de funciones con `def`.

Breve explicación:

- Las funciones permiten agrupar comportamiento reutilizable. Se definen con `def nombre(param):` y usan `return` para devolver valores.


Instrucciones de ejecución (Visual Studio Code / LliureX)

Abre la carpeta del proyecto en Visual Studio Code y usa el terminal integrado (Ver > Terminal). Sitúate en la carpeta `UD2` si es necesario y ejecuta:

```bash
# Ejecutar los scripts desde la terminal integrada
python 01_caracteres.py
python 02_identificadores.py
python 03_palabras_reservadas.py
python 04_variables_constantes.py
python 05_arrays.py
python 06_comentarios.py
python 07_expresiones.py
python 08_sentencias.py
python 09_funciones.py
```

Notas:
- Comprueba la versión de Python con `python --version`.
- Los archivos usan codificación UTF-8 para soportar acentos y caracteres especiales.
