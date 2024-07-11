# 8. Leer 10 números enteros, almacenarlos en una lista
#  y determinar cuántos números negativos hay.

numeros = []

for i in range(10):
    numero = int(input(f"Ingresa el entero {i+1}: "))
    numeros.append(numero)

conteo_negativos = sum(1 for num in numeros if num < 0)

print(f"Hay {conteo_negativos} números negativos en la lista.")