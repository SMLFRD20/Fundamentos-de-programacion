# 6. Leer un número entero de tres dígitos y mostrar todos los enteros 
# comprendidos entre 1 y cada uno de los dígitos.
numero = int(input("Introduce un número entero de tres dígitos: "))
if 100 <= numero <= 999:
    centena = numero // 100
    decena = (numero // 10) % 10
    unidad = numero % 10
    print("Dígitos del número:", centena, decena, unidad)
    print(f"Enteros comprendidos entre 1 y {centena}:")
    for ejercicio6 in range(1, centena + 1):
        print(ejercicio6, end=' ')
    print()
    print(f"Enteros comprendidos entre 1 y {decena}:")
    for ejercicio6 in range(1, decena + 1):
        print(ejercicio6, end=' ')
    print()
    print(f"Enteros comprendidos entre 1 y {unidad}:")
    for ejercicio6 in range(1, unidad + 1):
        print(ejercicio6, end=' ')
    print()
else:
    print("El número introducido no es un entero de tres dígitos.")
