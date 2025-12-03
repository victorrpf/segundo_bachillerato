# UD4. Introducción a las Clases en Python
# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase.
# Una instancia es el “ejemplar” resultante de usar una clase como plantilla.
# La clase es el molde y la instancia es el objeto creado a partir de ese molde.
# Nos permite agrupar datos (atributos o propiedades) y funciones (métodos) en un solo lugar.

# Ejemplo básico de una clase
class Coche:
  # atributo de clase (todos los objetos de esta clase comparten este atributo)
  tipo = "vehículo de cuatro ruedas"
  ruedas = 4

  # método especial que construye el objeto: el constructor
  # se llama automáticamente este método cuando creas la instancia
  def __init__(self, marca, modelo, color):
    # atributos del objeto que pueden variar entre objetos de la misma clase
    self.marca = marca # self es una referencia a la instancia actual, en otros lenguajes se usa "this"
    self.modelo = modelo
    self.color = color

  # método que los objetos de la clase pueden realizar
  def arrancar(self): # si no usara self daría error porque no sabría a qué instancia se refiere
    print(f"El coche {self.marca} {self.modelo} arrancó! 🚗")
    #print(f"El {self.tipo} {self.marca} {self.modelo} {self.color} arrancó! 🚗")


mi_coche = Coche("Toyota", "Corolla", "rojo") # Crear una instancia/objeto de la clase Coche
mi_coche.arrancar() # Llamar al método arrancar de la instancia mi_coche

print(mi_coche.marca) # Acceder al atributo marca de la instancia mi_coche

coche_de_pheralb = Coche("Ford", "Fiesta", "azul")
coche_de_pheralb.arrancar()

print(coche_de_pheralb.marca)

# Encapsulación: es ocultar los detalles internos de una clase y exponer solo la interfaz pública