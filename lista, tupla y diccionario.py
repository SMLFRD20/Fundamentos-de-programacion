print("\n\n----- Primera Parte -----\n\n")

numeros = [1, 3, 4, 6, 7, 7, 6, 12, 24, 78, 100, 123]
print("Lista:", numeros)

multiplos_de_tres = [num for num in numeros if num % 3 == 0]
print("\nLista filtrada (Solo los múltiplos de 3):", multiplos_de_tres)

print("\n\n----- Segunda Parte -----\n\n")

suma = sum(numeros)
producto = 1
for num in numeros:
    producto *= num

print(f"El producto es: {producto}\nLa suma es: {suma}\nLa media es: {suma / len(numeros)}")

print("\n\n----- Tercera Parte -----\n\n")

dias_semana = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6: "Viernes"}
print("----- Diccionarios -----\n\n")
print("Días de la semana (mal formateados):", dias_semana)

dias_semana[7] = "Domingo"
dias_semana[6] = "Sábado"
print("Días de la semana (arreglados):", dias_semana)

print("\n\n----- Listas -----\n\n")
print("Acceder a los elementos del 6 al penúltimo:", numeros[5:-1])
numeros[5] = 10000
print("Lista modificada (6to elemento es 10000):", numeros)

print("\n\n----- Tuplas -----\n\n")
tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 10)
print("Tupla:", tupla_numeros)
print("Segundo elemento de la tupla:", tupla_numeros[1])