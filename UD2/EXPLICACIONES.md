
# Explicaciones — UD2 (según índice del PDF)

01_caracteres.py

Contenido: ejemplos de cadenas y caracteres, incluyendo escapes (`\n`, `\t`), comillas y conversión entre caracteres y códigos (`ord`/`chr`).

Breve explicación:

- Las cadenas en Python pueden contener caracteres especiales representados por secuencias de escape. Por ejemplo, `\n` inserta un salto de línea y `\t` una tabulación.
- Para mostrar comillas dentro de una cadena usamos comillas opuestas o escapamos las que coinciden con el delimitador.
- `ord(c)` devuelve el código Unicode de `c` y `chr(n)` devuelve el carácter cuyo código es `n`.

02_identificadores.py

Contenido: reglas y convenciones para nombrar identificadores en Python.

Breve explicación:

- Un identificador debe empezar por letra o guion bajo, no por cifra. Puede contener letras, dígitos y guion bajo.
- Evita usar nombres que colisionen con palabras reservadas o funciones integradas (p. ej. `list`, `str`).
- Convenciones: `snake_case` para variables y funciones, `PascalCase` para clases, MAYÚSCULAS para constantes.

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
