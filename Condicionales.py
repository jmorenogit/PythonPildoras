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
