# Función de Saludo
def saludo(nombre):
    return f"Hola, {nombre}!"
print(saludo("Ana"))

# -------------------------

# Función de Suma
def suma(a, b):
    return a + b
print(suma(3, 5))

# -------------------------

# Área de un Rectángulo
def area_rectangulo(ancho, alto):
    return ancho * alto
print(area_rectangulo(4, 5))

# -------------------------

# Número Par o Impar
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
print(es_par_o_impar(7))

# -------------------------

# Conversión de Grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(celsius_a_fahrenheit(25))

# -------------------------

# Máximo de Tres Números
def maximo_de_tres(a, b, c):
    return max(a, b, c)
print(maximo_de_tres(3, 7, 5))

# -------------------------

# Palíndromo
def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]
print(es_palindromo("Anita lava la tina"))

# -------------------------

# Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# -------------------------

# Contar Vocales
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador
print(contar_vocales("Hola Mundo"))

# -------------------------

# Números Primos
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
print(es_primo(29))