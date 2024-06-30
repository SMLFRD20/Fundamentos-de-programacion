# 17. Leer números hasta que digiten 0 y determinar a cuánto es 
# igual el promedio de los números terminados en 5.
suma_terminados_en_5 = 0
cantidad_terminados_en_5 = 0
while True:
    numero = int(input("Introduce un número (introduce el 0 para terminar): "))
    if numero == 0:
        break
    if numero % 10 == 5:
        suma_terminados_en_5 += numero
        cantidad_terminados_en_5 += 1
if cantidad_terminados_en_5 > 0:
    promedio_terminados_en_5 = suma_terminados_en_5 / cantidad_terminados_en_5
    print(f"El promedio de los números terminados en 5 es: {promedio_terminados_en_5}")
else:
    print("No se introdujeron números terminados en 5.")