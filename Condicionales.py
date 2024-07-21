# elif - Entra en else cuando ningún if anterior se ha cumplido.
#       Si usamos if en vez de elif entrará en else cuando no s ecumpla el if más cercano

#   if
#       elif
#   else

nota = int(input("Introduce nota: "))

if nota < 5:
    print("Insuficiente")
elif nota < 6:
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")

# Switch no existe en python. Alternativas: Diccionario, concatenar comparaciones, and y or, in

#Concatenar if
edad = int(input("Introduce edad: "))
if 0 < edad < 100:
    print("Edad válida")
else:
    print("Edad incorrecta. Introduzca un valor entre 0 y 100")

# in
usuario = input("Introduce usuario: ")
if usuario in ("Juan", "Luis", "Pepe"):
    print("Usuario existente")
else:
    print("El usuario no existe")