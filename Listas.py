#LISTAS
#Las listas son similares a los arrays en otros lenguajes
#nombreLista=[elem1 ,elem2]

#Imprimir listas
miLista=["Pepe","Juan","Luis","Maria"]
print (miLista[:]) #toda la lista
print (miLista) #toda la lista
print (miLista[2]) #posición 2
print (miLista[1:3]) #inicio 1 incluído fin 3 excluído
print (miLista[-2]) #Empieza a contar desde la última posición que equivale a -1
print (miLista[2:]) #desde 2 hasta el final

#Añadir
miLista.append("Rodrigo") #al final
miLista.insert(2,"Alberto") #en posición 2
miLista.extend(["Ernesto","Eva"]) #varios al final
print ("Añadiendo nombres: " + str(miLista))

#Devolver índice
print(miLista.index("Juan")) #devuelve su índice. Si varios elementos son iguales devuelve el índice del primero que encuentre

#Comprobar si existe en la lista
print("Maria" in miLista) #devuelve true or false

#Almacenar datos de distinto tipo
otraLista=["Juana",5,True,78.35]
print(otraLista)

#Borrar elementos
miLista.remove("Rodrigo")
miLista.pop() #elimina el último
print(miLista)

#Unir listas
miLista3=miLista + otraLista
print(miLista3)

#Repetir Lista
repetirLista=["elem1","elem2"] * 3
print(repetirLista)