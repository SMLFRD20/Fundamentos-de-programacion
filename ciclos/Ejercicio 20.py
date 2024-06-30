# 20. Leer un número entero y calcular a cuánto es igual la sumatoria de todas 
# las factoriales de los números comprendidos entre 1 y el número leído.
from math import factorial
numero = int(input("Introduce un número entero: "))
sumatoria_factoriales = 0
for i in range(1, numero + 1):
    sumatoria_factoriales += factorial(i)
print(f"La sumatoria de las factoriales de los números de 1 a {numero} es: {sumatoria_factoriales}")