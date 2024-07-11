# 9. Leer 10 números enteros, almacenarlos en una lista y calcular la factorial
#  a cada uno de los números leídos almacenándolos en otra lista.

def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

numeros = []

for i in range(10):
    numero = int(input(f"Ingresa el entero {i+1}: "))
    numeros.append(numero)

factoriales = [factorial(num) for num in numeros]

print("Lista de números ingresados:", numeros)
print("Lista de factoriales:", factoriales)