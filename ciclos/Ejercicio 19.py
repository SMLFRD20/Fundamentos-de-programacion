# 19. Leer un número entero y mostrar en pantalla su tabla de multiplicar.
numero = int(input("Introduce un número entero: "))
print(f"Tabla de multiplicar del {numero}:")
for ejercicio19 in range(1, 11):
    resultado = numero * ejercicio19
    print(f"{numero} x {ejercicio19} = {resultado}")