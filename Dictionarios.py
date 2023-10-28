# Permiten tener clave: valor
# Son cambiables, no permiten duplicados
# Desde python 3.7 son ordenados
# Permiten agregar y remover items
# Son iterables
# Poseen distintos metodos para manipular los datos
# Admiten distintos tipos de datos

usuario = {"nombre": "Pepito", "Apellido": "Perez", "Edad": 25}

print(usuario)
#Imprime las claves
print(usuario.keys())
#Imprime los valores
print(usuario.values())
#Para conocer el tamaño usamos len
print(len(usuario))
print(type(usuario))

#Buscar un item en especifico usamos get

print(usuario.get("nombre"))
print(usuario["Apellido"])

#Agregar nuevos items
usuario ["correo"] = "pepito@gmail.com"


print(usuario["correo"])
print(usuario.keys())

#Actualizar un item

usuario.update({"Correo": "pepito1234@gmail.com"})
print(usuario["correo"])

#Remover un item

"""usuario.pop("nombre")
print(usuario.keys())
usuario.popitem()
print(usuario.keys())
del usuario ["Edad"]
print(usuario.keys())"""

#Para recorrer el diccionario podemos elegir entre recorrer las claves, recorrer los valores o ambos

for x,y in usuario.items():
    print(x,y)

    #Recorrer claves

for x in usuario.keys():
    print(usuario[x])

for y in usuario.values():
    print(usuario[y])

    # Podemos tener un diccionario de diccionarios

    usuarios = {"usuario1":{"nombre":"Juan","edad":12},"usuario2":{"nombre":"Maria", "edad":15 }, "usuario3" :{"nombre": "Julia","edad":18}  }


    estudiante1 = {"nota1":4.5, "nota2":4.4}
    estudiante2 = {"nota1":4.2, "nota2":4.3}
    estudiante3 = {"nota1":4.7, "nota2":4.1}

    estudiantes ={
        "estudiante1":estudiante1,
        "estudiante2":estudiante2,
        "estudiante3":estudiante3
    }

    print(estudiantes["estudiante2"]["nota2"])