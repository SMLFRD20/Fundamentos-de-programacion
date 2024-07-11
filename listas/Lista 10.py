# 10. Leer 10 números enteros, almacenarlos en una lista. Luego leer un 
# entero y determinar cuántos divisores exactos tiene este último
#  número entre los valores almacenados en la lista.

def contar_divisores(numero, lista):
    count = 0
    for num in lista:
        if num != 0 and numero % num == 0:
            count += 1
    return count

numeros = []

for i in range(10):
    numero = int(input(f"Ingresa el entero {i+1}: "))
    numeros.append(numero)

otro_numero = int(input("Ingresa otro entero para contar sus divisores entre los números almacenados: "))

cantidad_divisores = contar_divisores(otro_numero, numeros)

print(f"El número {otro_numero} tiene {cantidad_divisores} divisores exactos entre los números almacenados en la lista.")