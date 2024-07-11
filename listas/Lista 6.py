# 6. Leer 10 números enteros, almacenarlos en una lista y determinar
#  en qué posiciones se encuentran los números con más de 3 dígitos.

numeros = []

for i in range(10):
    numero = int(input(f"Ingresa el entero {i+1}: "))
    numeros.append(numero)

posiciones_digitos = [i for i, num in enumerate(numeros) if len(str(abs(num))) > 3]

if posiciones_digitos:
    print(f"Los números con más de 3 dígitos se encuentran en las posiciones: {', '.join(str(pos + 1) for pos in posiciones_digitos)}")
else:
    print("No hay números con más de 3 dígitos.")