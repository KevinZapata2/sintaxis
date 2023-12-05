# sumar la cantidad de vocales o que tenga la cadena de texto

# cadena = "otorrinolaringologo"
# print(len(cadena))
# suma = 0
#operacion de pertenencia,

# for letra in cadena:
#     if letra == "o":
#         suma += 1 # suma = suma +1
# print(suma)
# print(f"la letra 'o' se encuentra en {cadena} {suma} veces")
# print("la letra 'o' se encuentra en {} {} veces".format(cadena,suma))
#teniendo en cuenta la posicion(indice) de cada letra.
# s= 0
# for i in range(len(cadena)): #rango es de 0 a 19(19 es la cantidad de elemento de la cadena)
#     if cadena[i] == "o":
#         s += 1
        
# print(s)

#solicitar alusuario numeros al ingresar, luego en un ciclo pedir que ingrese numero al azar, evaluar la cantidad de numero impares ingresados

cantidad_numeros = int(input("Ingrese la cantidad de números a evaluar: "))
numeros_impares = 0

for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero % 2 != 0:
        numeros_impares += 1

print(f"La cantidad de números impares ingresados es: {numeros_impares}")