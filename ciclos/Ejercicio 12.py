# 12. Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.
numero = int(input("Introduce un número entero de tres dígitos: "))
if 100 <= numero <= 999:
    numero_str = str(numero)
    if '1' in numero_str:
        print(f"El número {numero} sí contiene el dígito '1'.")
    else:
        print(f"El número {numero} no contiene el dígito '1'.")
else:
    print("El número introducido no tiene tres dígitos.")