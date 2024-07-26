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