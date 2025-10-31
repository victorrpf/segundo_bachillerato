
# Explicaciones — UD2 (según índice del PDF)

01_caracteres.py

Contenido: ejemplos de cadenas y caracteres, incluyendo escapes (`\n`, `\t`), comillas, conversión entre caracteres y códigos (`ord`/`chr`) y uso de backspace (`\b`).

- Salto de línea (`\n`) y tabulación (`\t`): `print("Hola\nMundo\t➡\tTabulado")` muestra "Mundo" en la línea siguiente y usa una tabulación.
- Comillas: se puede incluir `'` dentro de una cadena entre dobles comillas y viceversa; si hace falta, se escapan con `\`.
- `ord(c)` y `chr(n)`: permiten convertir entre carácter y su código Unicode/ASCII.
- Backspace (`\b`): el script muestra `print("Backspace: 123456\b78")`.
	- `\b` es un carácter de control (backspace) que en la salida de la terminal mueve el cursor una posición atrás; el comportamiento exacto depende del terminal. En muchas consolas `123456\b78` aparecerá visualmente como `12378` porque el `\b` retrocede sobre el `6` y luego se escribe `78`.

02_identificadores.py

Contenido: ejemplos y reglas extraídas del script actual.

- Ejemplos válidos en Python (adaptados desde la tabla en C): `Numero`, `dia_del_mes`, `PINGUINO1`, `_ciudad`, `Z`.
- Elementos no válidos o problemáticos: no se pueden usar identificadores que comiencen por dígitos (p. ej. `123`), no se permiten espacios ni símbolos como `*` en los nombres, y aunque Python admite Unicode (`ñ`, acentos), su uso no es recomendable en código didáctico por cuestiones de portabilidad.
- Reglas clave:
	1. No puede empezar por dígito.
	2. Solo letras, dígitos y guion bajo en identificadores válidos (sin espacios ni símbolos).
	3. Python admite identificadores Unicode, pero suele evitarse cuando se comparte código.

Recomendaciones:
- Usar `snake_case` para variables y funciones.
- Reservar MAYÚSCULAS para constantes.

03_palabras_reservadas.py

Contenido: listado y explicación de las palabras reservadas del lenguaje.

- Las palabras reservadas (como `if`, `for`, `while`, `def`, `class`, `import`, etc.) tienen un significado sintáctico en Python y no pueden usarse como identificadores.
- Usa `import keyword; keyword.kwlist` para ver la lista actual en la versión de Python instalada.

04_variables_constantes.py

Contenido: tipos básicos y ejemplos de variables y constantes.

- Tipos básicos: `int`, `float`, `str`, `bool`. Python es dinámico, la variable toma el tipo del valor asignado.
- Conversión explícita entre tipos: `str()`, `int()`, `float()` y funciones como `round()` para redondear.
- Constantes por convención: nombres en MAYÚSCULAS (p. ej. `PI = 3.14`), aunque Python no impone inmutabilidad.
- `type(obj)` permite ver el tipo que Python infiere en tiempo de ejecución (p. ej. `type("María")` -> `<class 'str'>`).
- Tipo booleano: `True` y `False` son valores del tipo `bool`. En el script aparece `aprobado = True` y se imprime su tipo con `type(aprobado)`.
- `None` es el valor que representa 'sin valor' (similar a `null` en otros lenguajes). Su tipo es `NoneType` (`type(None)`).
- Ejemplos concretos del script: se imprimen los valores y a continuación los tipos detectados por Python para `nombre`, `edad`, `nota_media`, `aprobado`, `sin_valor`, así como para las constantes `PI` y `MAX_ALUMNOS`.

05_arrays.py

Contenido: listas en Python (creación, acceso, métodos y comprehensions).

- Listas son colecciones ordenadas y mutables. Operaciones comunes: `append`, `pop`, indexación y slicing.
- Comprehensions permiten construir listas de forma compacta: `[x*x for x in range(5)]`.
- Declaración simple: `frutas = ["plátano", "fresa", "cereza"]` crea una lista con tres elementos.
- `append(x)` añade `x` al final de la lista: `frutas.append("naranja")`.
- Indexación: `frutas[3]` accede al cuarto elemento (los índices empiezan en 0).
- Heterogeneidad de tipos: las listas en Python pueden contener elementos de distinto tipo; por ejemplo, `frutas.append(1)` añade un entero a la lista de strings. Esto es permitido por diseño pero conviene evitar mezclar tipos si luego se procesan los elementos suponiendo un tipo concreto.

Consejo:
- Para mantener código claro, procura que las listas sean homogéneas por convención (p. ej. `List[str]`), o valida/convierte los elementos al insertarlos.

06_comentarios.py

Contenido: comentarios de línea y docstrings.

- Los comentarios de línea usan `#` y se ignoran en la ejecución. Los docstrings (triple comillas) documentan módulos, funciones o clases.
- Es buena práctica documentar las funciones con un docstring corto que explique su propósito y parámetros.
- Comentario de una sola línea: comienza con `#` y sirve para explicar una línea o una idea breve.
	- Ejemplo: `# Comentario de una sola línea`
- Docstrings / cadenas multilínea: usando `""" ... """` o `''' ... '''` puedes escribir texto en varias líneas.
	- Si colocas una docstring justo al inicio de un módulo, función o clase, Python la asocia como documentación (`__doc__`).
	- Ejemplo de uso en un módulo o función para describir su propósito.
- Comentarios inline: puedes añadir un comentario al final de la línea de código para aclarar una variable o una expresión.
	- Ejemplo: `valor = 10  # este comentario explica la variable 'valor'`

Recomendación:
- Enseña `#` para comentarios y docstrings para documentación formal. Evita usar docstrings como sustituto de comentarios de bloque salvo cuando realmente documentes la API.

07_expresiones.py

Contenido: expresiones y operadores aritméticos y lógicos.

- Operadores aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- Operadores lógicos: `and`, `or`, `not`. Comparaciones: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- División `/` produce un `float` aunque ambos operandos sean enteros (p. ej. `10 / 3` -> `3.333...`).
- División entera `//` descarta la parte fraccionaria (`10 // 3` -> `3`).
- Operador módulo `%` devuelve el resto de la división entera (`10 % 3` -> `1`).
- Potencia `**` eleva a la potencia (`10 ** 3` -> `1000`).

08_sentencias.py

Contenido: sentencias de control de flujo: `if/elif/else`, `for` y `while`.

- `if` permite ejecutar código condicionalmente; `for` itera sobre secuencias; `while` repite mientras la condición sea verdadera.
- Evitar bucles infinitos y preferir `for` cuando se itera sobre colecciones.

09_funciones.py

Contenido: introducción a la definición y uso de funciones con `def`.

- Las funciones permiten agrupar comportamiento reutilizable. Se definen con `def nombre(param):` y usan `return` para devolver valores.

Función nota_media:
- Definición de la función `nota_media(a, b, c)` que calcula la media aritmética de
	tres notas y devuelve una tupla `(media, estado)` donde `estado` es `'aprobado'`
	si la media >= 5 y `'suspenso'` en caso contrario.
- Ejemplos de uso en el script:
	- `print("Victor:", nota_media(5, 10, 7))` → muestra la tupla con media y estado.
	- `print("María:", nota_media(6, 9, 4))`
	- `print("Alberto:", nota_media(4, 4, 5))`

- La función devuelve una tupla (p. ej. `(7.33, 'aprobado')`). Una tupla es inmutable
	y es adecuada para devolver un pequeño conjunto de valores heterogéneos (aquí: número
	y texto). Si quisieras una colección modificable usarías una lista (`[media, estado]`).

10_input.py

Contenido: pedir dos enteros por teclado con `input()`, convertirlos con `int()` y mostrar
la suma. Refuerza el flujo `input → conversión → operación → print`.

11_raiz_cubica.py

Contenido: cálculo de la raíz cúbica de un número dado. Un *módulo* de Python es un
archivo con funciones reutilizables. Para usarlo se importa con `import math`. Sin `math`,
`numero ** (1/3)` se calcula con tipo `float`. Los `float` guardan una cantidad limitada de
decimales porque la memoria se almacena en binario. Cuando la raíz no cabe exacta, la
operación se aproxima (por ejemplo, con 64 aparece `3.9999999999999996`). `math.cbrt(numero)`
añade la corrección para normalizar el resultado (`4.0`). Si la raíz produce un número que el tipo `float` puede almacenar sin redondeos, como en 27 → `3`, ambas versiones coinciden. Cuando el cálculo requiera
máxima precisión o queramos evitar esas aproximaciones, usamos funciones del módulo `math`
o redondeamos la salida (`round(raiz_cubica, 5)`).

12_coseno.py

Contenido: cálculo del coseno de un ángulo expresado en grados.

- `import math` habilita el acceso a funciones trigonométricas y a la constante `math.pi`.
- Primer bloque: `math.radians(angulo_grados)` convierte directamente de grados a radianes.
- Segundo bloque: reproduce la fórmula vista en el libro, multiplicando por π/180 (`angulo_grados * PI / 180`). Aquí `PI` se fija con un literal flotante (`3.14159265`).
- Ambos caminos obtienen el mismo valor para `math.cos(angulo_radianes)`.
- La diferencia es didáctica (usar la utilidad de la librería frente a aplicar la fórmula manualmente).

13_switch.py

Contenido: clasificación de una nota numérica usando `match-case`, la estructura equivalente al switch en Python 3.10+.

- Se pide al usuario una nota entre 0 y 10 y se convierte a `float`.
- `match nota` usa guardas (`case nota if ...`) para detectar valores fuera de rango, suspensos (`< 5`), aprobados (`< 9`) y sobresalientes (resto de casos).
- `case _` actúa como cláusula por defecto cuando ningún caso previo coincide.
- Es un ejemplo directo para mostrar cómo `match` reemplaza al `switch` clásico en versiones modernas de Python.


Instrucciones de ejecución (Visual Studio Code / LliureX)

Abre la carpeta del proyecto en Visual Studio Code y usa el terminal integrado (Ver > Terminal). Sitúate en la carpeta `UD2` si es necesario y ejecuta:

```bash
python <nombre_del_script>
```

Notas:
- Comprueba la versión de Python con `python --version`.
- Los archivos usan codificación UTF-8 para soportar acentos y caracteres especiales.
