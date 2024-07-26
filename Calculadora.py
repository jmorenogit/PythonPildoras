def sumar(num1,num2):
  return num1+num2
def restar(num1,num2):
  return num1-num2
def multiplicar(num1,num2):
  return num1*num2
def dividir(num1,num2):
  return num1/num2

op=1
while op!=0:
  print("Calculadora python v1.0")
  op=input("0 salir, 1 sumar, 2 restar, 3 multiplicar, 4 dividir: ")
  op=int(op)
  if op<5 and op>0:
    num1=input("Introduzca numero 1: ")
    num1=int(num1)
    num2=input("Introduzca numero 2: ")
    num2=int(num2)

    if op==1:
      print("Resultado ",num1,"+",num2,"=",sumar(num1,num2))
    if op==2:
      print("Resultado ",num1,"-",num2,"=",restar(num1,num2))
    if op==3:
      print("Resultado ",num1,"x",num2,"=",multiplicar(num1,num2))
    if op==4:
      print("Resultado ",num1,":",num2,"=",dividir(num1,num2))

  else:
    if op==0:
      print("Bye...")
    else:
      print("opción inválida")


