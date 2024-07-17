#Diccionarios
#Permiten almacenar datos asociados a una clave. Asociación clave:valor
#Similar a un array asociativo en PHP
#Puede almacenar cualquier tipo incluso listas, tuplas u otro diccionario
#El orden es indiferente

miDiccionario={"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}

print(miDiccionario["España"])
print(miDiccionario)

#añadir elementos
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

#modificar
miDiccionario["Italia"]="Roma"
print(miDiccionario)

#eliminar
del miDiccionario["Reino Unido"]
print(miDiccionario)

#claves con tupla
miTupla=("España", "Francia", "Reino unido", "Alemania")
miDiccionario={miTupla[0]:"Madrid", miTupla[1]:"París", miTupla[2]:"Londres", miTupla[3]:"Berlín"}
print(miDiccionario)

#almacenar tupla
miDiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}
print(miDiccionario["anillos"])

#almacenar otro diccionario
miDiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario["anillos"])

#obtener claves
print(miDiccionario.keys())

#obtener valores
print(miDiccionario.values())

#longitud
print(len(miDiccionario))