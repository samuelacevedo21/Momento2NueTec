

dias_semana=("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")

print(type(dias_semana))

#Son inmutables
#Contienen distintos tipos de datos
#Si se requiere añadir algo a una tupla se debe convertir primero a una lista
#Se puede acceder a la tupla indicando el indice de la misma, el cual comienza desde cero
#Si queremos recorrer la tupla usamos el ciclo for
#Podemos hacer joins entre tuplas
#Para conocer el tamaño usamos la funcion len(dias_semana)
#print(dir(dias_semana))
#Las tuplas permiten datos duplicados

print(len(dias_semana))

print(dias_semana[0])
print(dias_semana[1])
print(dias_semana[2])
print(dias_semana[3])
print(dias_semana[4])
print(dias_semana[5])
print(dias_semana[6])

#Podemos hacer slicing indicando el rango que queremos imprimir
print(dias_semana[:7])
print(dias_semana[0:])
print(dias_semana[-1:])
print(dias_semana[:-1])
print(dias_semana[2:5])

#Para recorrer la tupla usamos for

#for i in range(len(dias_semana)):
    #print(dias_semana[i]) #para recorrer a la inversa podemos realizar -i

    #para cambiar algun valor de la tupla o añadir debemos convertirla a una lista:

dias_semana_lista = list(dias_semana)

print(type(dias_semana_lista))

dias_semana_lista.append("festivo")

print(dias_semana_lista[0:])

dias_semana_lista.pop()

print(dias_semana_lista[:8])

dias_semana=tuple(dias_semana_lista)

print(type(dias_semana))