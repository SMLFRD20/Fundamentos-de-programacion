# Leer dos números enteros y si la diferencia es par, mostrar la suma de los dígitos.
# Si la diferencia es un primo menor que 10, mostrar el producto de los números.
# Si la diferencia termina en 4, mostrar los dígitos por separado.
def suma_digitos(num):
    return sum(int(digit) for digit in str(num))
def es_primo(num):
    if num < 2:
        return False
    def es_primo(num):
        if num < 2:
            return False
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
diferencia = abs(num1 - num2)
condiciones_cumplidas = False
if diferencia % 2 == 0:
    suma_total_digitos = suma_digitos(num1) + suma_digitos(num2)
    print(f"La suma de los dígitos de {num1} y {num2} es: {suma_total_digitos}")
    condiciones_cumplidas = True
if diferencia < 10 and es_primo(diferencia):
    producto = num1 * num2
    print(f"El producto de {num1} y {num2} es: {producto}")
    condiciones_cumplidas = True
if str(diferencia)[-1] == '4':
    print(f"Los dígitos de {num1} son: ", end="")
    for digit in str(num1):
        print(digit, end=" ")
    print(f"\nLos dígitos de {num2} son: ", end="")
    for digit in str(num2):
        print(digit, end=" ")
    condiciones_cumplidas = True
if not condiciones_cumplidas:
    print("Ninguna de las condiciones se cumple.")
