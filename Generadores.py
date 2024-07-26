#Generadores
#Estructuras que extraen valores de una función y los almacenan en objetos iterables que se pueden recorrer
#Estos valores se almacenan de uno en uno
#Suspensión de estado: cada vez que se almacena un valor, el generador permanece en pausa la iteración hasta que se solicite el siguiente.

#yield: se utiliza en lugar de return

#Ventajas:
# - más eficientes que las funciones. No hay que crear la lista completa ni reservar espacio en memoria
# - listas valores infinitos
# - devuelve de uno en uno

#Sintaxis
# def generadorNombre():
#   yield objetoDevuelto
#   return (opcional)

#Ej: generar pares hasta un límite que indicado
#Sin generador
def funcionPares(limite):    
    num=1
    miLista=[]#no hace falta con generador
    while num<limite:
        miLista.append(num*2)# yield con generador
        num+=1
    return miLista#no hace falta con generador

print("Lista de pares usando función")
limite = int(input("Introduzca cantidad de pares: "))
listaPares = funcionPares(limite)
print(listaPares)

#Con generador
def generaPares(limite):    
    num=1
    while num<limite:
        yield num*2
        num+=1

print("Lista de pares usando generador")
limite = int(input("Introduzca cantidad de pares: "))
listaPares = generaPares(limite)
#al ser objeto iterable no se puede imprimir directamente, hay que recorrelo
for i in listaPares:
    print(i,end=", ") 
