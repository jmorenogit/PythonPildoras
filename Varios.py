# la función input() detiene el flujo del programa en espera de introducir por teclado
# la entrada la considera string por lo que hay que convertir si queremos un número con int()
var= input("Escribe aquí: ")

print(var)

#Concatenar distintos tipos de datos
#Python es fuertemente tipado. Es necesario convertir tipos para concatenar
numero = 5
print("texto " + str(numero))

#Transformar mayúsculas - minúsculas
#lower()
#upper()
texto = "HoLa QUE taL"
print(texto)
minus = texto.lower() #muy utilizado antes de comparar textos
print("En minúsculas: " + minus)