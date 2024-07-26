#Comentario
nombre="Manu"
print(nombre)

#En python todo son objetos
print("Tipo: ",type(nombre))

#Triple comilla para incluir saltos de línea
mensaje="""Mensaje con 
3 saltos 
de linea"""
print(mensaje)

#Funciones: predefinidas(incluídas con el lenguaje), propias(creadas posteriormente)
def miFuncion(num1, num2):
  if num1>num2:
    return print("El numero 1 es mayor")
  else:
    return print("El numero 2 es mayor")

num1=input("Introduzca numero 1: ")
num2=input("Introduzca numero 2: ")

miFuncion(num1,num2)

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

#modificar final de línea con print
print("texto", end="") #sin salto de línea. Podemos introducir espacio u otro caracter
print("seguido")

#print función tipo f
print (f"saludo: {minus}")