#1. Leer 10 enteros, almacenarlos en una lista y determinar en qué 
# posición del arreglo está el mayor número leído.
numeros = []

for i in range(10):
    numero = int(input(f"Ingresa el entero {i+1}: "))
    numeros.append(numero)

mayor_numero = max(numeros)
posicion_mayor = numeros.index(mayor_numero)

print(f"El mayor número es {mayor_numero} y está en la posición {posicion_mayor + 1} del arreglo.")