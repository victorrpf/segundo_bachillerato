# Hola Mundo con caracteres especiales
print("Hola\nMundo\t➡\tTabulado");

# Comillas y conversión de caracteres
print("Comillas: 'simple', \"doble\", `invertida` (como texto)");

# Códigos ASCII y conversión
print("Código ASCII de 'A':", ord('A'), "⇄ chr(65):", chr(65))
# Ejemplos sencillos de expresiones regulares (cuantificadores +, *, ?)
import re

texts = ['a', 'aa', 'b', 'baaa', '']

print('\nDemostración de cuantificadores en regex (+, *, ?)\n')

# a+ : una o más 'a'
pat = re.compile(r'a+')
print('Ejemplo + (uno o más)')
for t in texts:
	m = pat.search(t)
	print(f"{t!r} ->", 'match' if m else 'no match')

# a* : cero o más 'a'
pat = re.compile(r'a*')
print('\nEjemplo * (cero o más)')
for t in texts:
	m = pat.search(t)
	print(f"{t!r} -> matched {m.group(0)!r}")

# a? : cero o una 'a' (opcional)
pat = re.compile(r'a?')
print('\nEjemplo ? (cero o una vez)')
for t in texts:
	m = pat.search(t)
	print(f"{t!r} -> matched {m.group(0)!r}")