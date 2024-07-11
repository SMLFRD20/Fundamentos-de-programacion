# 2. Leer 10 enteros, almacenarlos en una lista y determinar en qué 
# posición de del arreglo está el mayor número par leído.
numeros = []

for i in range(10):
    numero = int(input(f"Ingresa el entero {i+1}: "))
    numeros.append(numero)

numeros_pares = [num for num in numeros if num % 2 == 0]

if numeros_pares:
    mayor_par = max(numeros_pares)
    posicion_mayor_par = numeros.index(mayor_par)
    print(f"El mayor número par es {mayor_par} y está en la posición {posicion_mayor_par + 1} del arreglo.")
else:
    print("No se ingresaron números pares.")
