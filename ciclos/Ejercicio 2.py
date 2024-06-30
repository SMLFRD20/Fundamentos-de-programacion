# 2. Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.
numero = int(input("Introduce un número entero: "))
for ejercicio2 in range(1, numero + 1):
    if ejercicio2 % 2 == 0:
        print(ejercicio2)