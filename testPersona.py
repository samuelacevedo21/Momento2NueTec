#from Persona import Persona
from Persona import Persona

persona1 = Persona(id=None, nombre=None, apellido=None, correo=None, contraseña=None)

persona1.id = "1"

print(persona1.id)

persona1.registrar()
persona1.ver_registro()