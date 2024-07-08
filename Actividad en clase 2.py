dato = "oso; perro; 10; 5; son animales."

elementos = dato.split('; ')

resto = elementos[4].split(' ', 1)

animal1 = elementos[0]
animal2 = elementos[1]
cantidad2 = elementos[2]
cantidad1 = elementos[3]
frase = f"{animal1} y {animal2} son {resto[1]}"

def es_palindromo(palabra):
    return palabra == palabra[::-1]

print(f"{animal1} {'es' if es_palindromo(animal1) else 'no es'} un palíndromo")
print(f"{animal2} {'es' if es_palindromo(animal2) else 'no es'} un palíndromo")
print(f"tenemos {cantidad1} {animal1}s")
print(f"tenemos {cantidad2} {animal2}s")
print(frase)