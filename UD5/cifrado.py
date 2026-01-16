# Para codificación y decodificación en base64 que es un tipo de cifrado sencillo
import base64

# Función lambda para realizar una operación XOR entre los datos y la clave
# La operación XOR es una técnica básica de cifrado simétrico
xor = lambda d,k: bytes(b ^ k[i % len(k)] for i,b in enumerate(d))

m = input("Mensaje: ").encode()
clave = input("Clave: ").encode()
if not clave:
	raise SystemExit("La clave no puede estar vacía")

c = xor(m, clave)
token = base64.urlsafe_b64encode(c).decode()
print("Cifrado:", token)

# El mensaje cifrado se puede descifrar
print("Descifrado:", xor(base64.urlsafe_b64decode(token), clave).decode())
