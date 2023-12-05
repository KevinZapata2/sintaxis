#COLECCIONES
#Almacenar una cantidad de elementos en una variable.
"""
listas= [] arreglos mutables, se pueden cambiar
tuplas= () arrelgos inmutables
diccionarios= {clave:valor}
"""
#Listas

"""
mutables: agregar, eliminar, modificar elementos.
cada elemento va separado por ","
metodos: append(), insert(), pop(), remove(), count(), sum(), sort(),
sort(reverse=), index(), zip().
se puede almacenar cualquier tipo de dato    
"""

Deportes = ["Baloncesto", "Futbol", "Natacion", "Patinaje", "voleibol"]
#Longitud listas:
#Cuantos elementos tiene la lista
# print(len(Deportes))
#acceder a un elemento de la lista
#acceder al deporte Futbol.
# print(Deportes[1])
#agregar elementos a la lista
#append(): que agrega elementos a la lista a la ultima posicion
#insert(): agrega elementos a la lista en la posicion especifica
#agregar temer en la ultima posicion
# Deportes.append("tennis")
# print(Deportes)
# Deportes.insert(2, "Natacion_Artistica")
# print(Deportes)
#Tenemos una lista numerica, y dos listas vacias una llamada multiplos de 2 y la otra llamada multiplos de 3 y 5. Evaluar los elementos de la lista a ver si son multiplos de 2 , 3 y 5 y alamacenarlos en la lista correspondiente

# valores = [2,3,4,5,6,10,15,40,45,89,93,7,30,18,1009,75]

# multiplos2 = []
# multiplos3_5 = []

# for numero in valores:
#     if numero % 2 == 0:
#         multiplos2.append(numero)
#     if numero % 3 == 0 and numero % 5 == 0: 
#         multiplos3_5.append(numero)

# print("Lista de múltiplos de 2:", multiplos2)
# print("Lista de múltiplos de 3 y 5:", multiplos3_5)

#eliminar elementos de la lista:
#pop()
#Remove()
# Deportes.pop(3)
# Deportes.remove("Baloncesto")
# Deportes.clear()
# print(Deportes)

#index(): son muestra la posicion que este algun elemento

valores = [2,3,4,5,6,10,15,40,45,89,93,7,18,1009,75,2]

# posicion = valores.index(15)
# print(posicion)

#sum(): sumar los elementos de la lista

# suma = sum(valores)
# print(suma)
#min(), max()
#numero mayor y menor de la lista

print(f"El numero mayor de la lista es {max(valores)}\n El numero menor de la lista es {min(valores)}")
