# 13. Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.
numero = int(input("Introduce un número entero: "))
print(f"Múltiplos de 5 entre 1 y {numero}:")
for ejercicio13 in range(1, numero + 1):
    if ejercicio13 % 5 == 0:
        print(ejercicio13)