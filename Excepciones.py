#EXCEPCIONES
#son errores que ocurren en tiempo de ejecución. La sintaxis es correcta, pero ha ocurrido "algo inesperado".

#Captura o control de excepción
#Permite seguir con la ejecución despues de un error inesperado
#TRY código que se ejecuta si no hay error
#EXCEPT si hay error. Se puede utilizar sin nombre de error para captura genérica
#FINALLY se ejecuta siempre haya o no error. Util para cerrar conexión con Base Datos. El programa no cae si no hay except, pero hay finally
#RAISE se utiliza para lanzar excepciones propias


#Calculadora
def sumar(num1,num2):
  return num1+num2
def restar(num1,num2):
  return num1-num2
def multiplicar(num1,num2):
  return num1*num2
def dividir(num1,num2):
  try: #Capturar error división por cero
    return num1/num2
  except ZeroDivisionError:
    print("No se puede dividir entre cero")
    return "Infinito"

print("Calculadora python v1.0")

continuar=True
while continuar==True:

  print("Calculadora python v1.0")
  
  while True: #pedir valores hasta que sean correctos
    try: #captura ValueError si se introduce texto
      num1=int(input("Introduzca numero 1: "))
      num2=int(input("Introduzca numero 2: "))
      break
    except ValueError:
      print("Valor introducido incorrecto")

  while True:#valores entre 1 y 4
    try:
      op=int(input("1 sumar, 2 restar, 3 multiplicar, 4 dividir: "))
      if op<5 and op>0:
        break
      else:
        raise ValueError #lanzamos error si la elección no está entre 1 y 4
    except ValueError:
      print("Error: indique un nº de operación correcto")
      continue#salta a la siguiente iteración y no realiza operaciones
  
  if op==1:
    print("Resultado ",num1,"+",num2,"=",sumar(num1,num2))
  if op==2:
    print("Resultado ",num1,"-",num2,"=",restar(num1,num2))
  if op==3:
    print("Resultado ",num1,"x",num2,"=",multiplicar(num1,num2))
  if op==4:
    print("Resultado ",num1,":",num2,"=",dividir(num1,num2))

  while True: #bucle hasta que se introduzca s o n
      detener=input("Desea realizar otra operación (S/N)")
      if detener.lower()=="n":#salir del programa
        print("Bye...")
        continuar=False
        break
      elif detener.lower()=="s":#realizar otra operación
        break
