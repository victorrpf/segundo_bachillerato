# Importar la librería base64 para codificación y decodificación
import base64

# Función de mezcla el mensaje con la clave (cifrar).
# Cada byte del mensaje se combina con un byte de la clave usando XOR.
def mezcla(data, key):
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

# Solicitar al usuario el mensaje y la clave
mensaje = input("Mensaje: ").encode()
clave = input("Clave: ").encode()
if not clave:
    raise SystemExit("La clave no puede estar vacía")

# Cifrar el mensaje
c = mezcla(mensaje, clave)

# Codificar el mensaje cifrado en base64 para facilitar su manejo
token = base64.urlsafe_b64encode(c).decode()
print("Cifrado:", token)

# Descifrar el mensaje que no sería posible con hash
print("Descifrado:", mezcla(base64.urlsafe_b64decode(token), clave).decode())
