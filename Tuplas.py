#TUPLAS
#Son listas inmutables. No permiten añadir, mover o eliminar
#Permiten extraer a una nueva tupla
#Tambíen permiten comprobar si existe un elemento
#En las actuales versiones de python su pueden hacer busquedas(index)

#Ventajas: más rápidas, menos espacio en memoria,mejor para recorrer, formatea strings, clave diccionario(listas no)

miTupla=("Pepe", "Juan","Pepe", "Luis") #Paréntesis opcional

miLista=list(miTupla) #convertir tupla en lista

miTupla=tuple(miLista) #convertir lista en tupla

print(miTupla.count("Pepe")) #cuantas veces existe un elemento

print(len(miTupla)) #longitud

#empaquetado de tupla escribirla sin paréntesis
miTupla="Pepe", "Juan","Pepe", "Luis"

#desempaquetado de tupla para asignar a variables
var1,var2,var3,var4=miTupla
print(var1+var2+var3+var4)

