
#Los conjuntos son mutables
#son desordenados, cuando se llama no se tiene certeza en el orden en que los mostrará
#no son indexados
#no permite datos duplicados

vocales= {"a","e","i","o","u"}
print(len(vocales))
print(type(vocales))    

#Para recorrer los conjuntos se usa in

for i in vocales :
    print(vocales)
print("----------------------------------")

   

    
for i in vocales :
    print(vocales)
print("----------------------------------")


    
for i in vocales :
    print(vocales)
print("----------------------------------")



#Tienen el metodo add y remove

vocales.add("@")

for i in vocales :
    print(vocales)

#Podemos remover

vocales.remove("@")
for i in vocales :
    print(vocales)