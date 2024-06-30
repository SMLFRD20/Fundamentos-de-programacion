# 16. Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor
#  que los y primeros múltiplos de 5 para valores de x y y leídos.
x = int(input("Introduce el valor de x (número de primeros múltiplos de 2 a promediar): "))
y = int(input("Introduce el valor de y (número de primeros múltiplos de 5 a comparar): "))
suma_multiplos_2 = 0
for ejercicio16 in range(1, x + 1):
    multiplo = 2 * ejercicio16
    suma_multiplos_2 += multiplo
promedio_multiplos_2 = suma_multiplos_2 / x
suma_multiplos_5 = 0
for ejercicio16 in range(1, y + 1):
    multiplo = 5 * ejercicio16
    suma_multiplos_5 += multiplo
if promedio_multiplos_2 > suma_multiplos_5:
    print(f"El promedio de los primeros {x} múltiplos de 2 ({promedio_multiplos_2}) es mayor que la suma de los primeros {y} múltiplos de 5 ({suma_multiplos_5}).")
else:
    print(f"El promedio de los primeros {x} múltiplos de 2 ({promedio_multiplos_2}) no es mayor que la suma de los primeros {y} múltiplos de 5 ({suma_multiplos_5}).")