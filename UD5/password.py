# Importar los módulos necesarios para manejar contraseñas y hashing
import getpass, hashlib

# Solicitar al usuario que ingrese una contraseña de manera segura
pwd = getpass.getpass("Contraseña: ")

# Calcular y mostrar el hash SHA-256 de la contraseña ingresada
print(hashlib.sha256(pwd.encode("utf-8")).hexdigest())