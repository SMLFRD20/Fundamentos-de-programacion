# 10. Leer un número entero y determinar a cuánto es igual la 
# suma de todos los enteros comprendidos entre 1 y el número leído.
numero = int(input("Introduce un número entero: "))
suma_enteros = 0
for ejercicio10 in range(1, numero + 1):
    suma_enteros += ejercicio10
print(f"La suma de todos los enteros comprendidos entre 1 y {numero} es: {suma_enteros}")