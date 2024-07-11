# 5. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición
#  se encuentra el número primo con mayor cantidad de dígitos pares.

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_digitos_pares(numero):
    return sum(1 for digito in str(abs(numero)) if int(digito) % 2 == 0)

numeros = []

for i in range(10):
    numero = int(input(f"Ingresa el entero {i+1}: "))
    numeros.append(numero)

numeros_primos = [num for num in numeros if es_primo(num)]

if numeros_primos:
    max_digitos_pares = -1
    numero_primo_max_pares = None
    posicion_max_pares = -1
    
    for num in numeros_primos:
        digitos_pares = contar_digitos_pares(num)
        if digitos_pares > max_digitos_pares:
            max_digitos_pares = digitos_pares
            numero_primo_max_pares = num
            posicion_max_pares = numeros.index(num)

    print(f"El número primo con mayor cantidad de dígitos pares es {numero_primo_max_pares} y está en la posición {posicion_max_pares + 1} del arreglo.")
else:
    print("No se ingresaron números primos.")