#BUCLES

#------
# FOR |
#------

#Recorrer string
for i in "textoarrecorrer": #se repite tantas veces como caracteres tenga la cadena
    print(i, end="")

print("")

#Tipo Range - Python2 range función - Python3 range tipo
for i in range(5): #crea un array de 5 números
    print(i)

print("------------")
for i in range (5,50,3): #(inicio, fin, saltos)
    print (i)

#continue   -   salta a la siguiente vuelta del bucle. Vuelve al principio del flujo del bucle
#Ej para no contar espacios en blanco
contador=0
for i in "Jose Manuel":
    if i == " ":
        continue
    contador+=1
print (f"nº caracteres en José Manuel: {contador}")

#pass devuelve null y no ejecuta el bucle

#else entra al terminar las vueltas
#EJ comprobar @
email=input("Introduce email: ")
for i in email:
    if i=="@":
        arroba=True
        print("El email incluye @")
        break;
else:
    arroba=False
    print("Falta la @")



#--------
# WHILE |
#--------

# While condición:
#   var incremento
#   break; opcional
