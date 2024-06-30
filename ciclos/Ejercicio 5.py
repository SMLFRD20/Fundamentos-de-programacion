# 5. Leer dos números y mostrar todos los números terminados en 4 
# comprendidos entre ellos.
numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))
if numero1 > numero2:
    numero1, numero2 = numero2, numero1
for ejercicio5 in range(numero1, numero2 + 1):
    if ejercicio5 % 10 == 4:
        print(ejercicio5)