# 11. Leer un número entero de dos dígitos y mostrar en 
# pantalla todos los enteros comprendidos entre un dígito y otro.
numero = int(input("Introduce un número entero de dos dígitos: "))
if 10 <= numero <= 99:
    decena = numero // 10
    unidad = numero % 10
    inicio = min(decena, unidad)
    fin = max(decena, unidad)
    print(f"Enteros comprendidos entre {inicio} y {fin}:")
    for ejercicio11 in range(inicio, fin + 1):
        print(ejercicio11, end=' ')
    print()
else:
    print("El número introducido no tiene dos dígitos.")