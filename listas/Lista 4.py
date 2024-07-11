# 4. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos
#  números de los almacenados en dicho arreglo comienzan en dígito primo

def es_digito_primo(digito):
    return digito in {2, 3, 5, 7}

def obtener_primer_digito(numero):
    return int(str(abs(numero))[0])

numeros = []

for i in range(10):
    numero = int(input(f"Ingresa el entero {i+1}: "))
    numeros.append(numero)

conteo_digitos_primos = sum(1 for num in numeros if es_digito_primo(obtener_primer_digito(num)))

print(f"{conteo_digitos_primos} números comienzan con un dígito primo.")