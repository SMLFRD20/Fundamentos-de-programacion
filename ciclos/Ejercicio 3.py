# 3. Leer un número entero y mostrar todos los divisores exactos 
# del número comprendidos entre 1 y el número leído.
numero = int(input("Introduce un número entero: "))
for ejercicio3 in range(1, numero + 1):
    if numero % ejercicio3 == 0:
        print(ejercicio3)