# 7. Leer 10 números enteros, almacenarlos en una lista y determinar
#  a cuánto es igual el promedio entero de los datos de la lista.

numeros = []

for i in range(10):
    numero = int(input(f"Ingresa el entero {i+1}: "))
    numeros.append(numero)

promedio_entero = sum(numeros) // len(numeros)

print(f"El promedio entero de los datos de la lista es {promedio_entero}.")