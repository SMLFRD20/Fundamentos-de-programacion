# 3. Leer 10 enteros, almacenarlos en una lista y determinar en qué 
# posición del arreglo está el mayor número primo leído.

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numeros = []

for i in range(10):
    numero = int(input(f"Ingresa el entero {i+1}: "))
    numeros.append(numero)

numeros_primos = [num for num in numeros if es_primo(num)]

if numeros_primos:
    mayor_primo = max(numeros_primos)
    posicion_mayor_primo = numeros.index(mayor_primo)
    print(f"El mayor número primo es {mayor_primo} y está en la posición {posicion_mayor_primo + 1} del arreglo.")
else:
    print("No se ingresaron números primos.")