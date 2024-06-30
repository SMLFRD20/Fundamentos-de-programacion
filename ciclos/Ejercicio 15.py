# 15. Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.
suma_multiplos = 0
for ejercicio15 in range(1, 21):
    multiplo = 3 * ejercicio15
    suma_multiplos += multiplo
print(f"La suma de los primeros 20 múltiplos de 3 es: {suma_multiplos}")