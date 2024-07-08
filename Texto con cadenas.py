# Sergio Lugo 24-0951
# Leer un texto y realizar las siguientes operaciones:
print("\n" + "-"*60 + "\n")
texto = input("Introduce un texto: ")
print("\n" + "-"*60 + "\n")

# 1) Retornar todo el texto en mayúsculas
mayusculas = texto.upper()
print("1) Texto en mayúsculas:", mayusculas)
print("\n" + "-"*60 + "\n")

# 2) Retornar todo el texto en minúsculas
minusculas = texto.lower()
print("2) Texto en minúsculas:", minusculas)
print("\n" + "-"*60 + "\n")

# 3) Retornar los dos primeros caracteres del texto
dos_primeros_caracteres = texto[:2]
print("3) Los dos primeros caracteres:", dos_primeros_caracteres)
print("\n" + "-"*60 + "\n")

# 4) Retornar los dos últimos caracteres del texto
dos_ultimos_caracteres = texto[-2:]
print("4) Los dos últimos caracteres:", dos_ultimos_caracteres)
print("\n" + "-"*60 + "\n")

# 5) Retornar la cantidad de veces que se repite el último caracter
ultimo_caracter = texto[-1] if texto else ""
repeticiones = texto.count(ultimo_caracter)
print("5) Cantidad de veces que se repite el último carácter:", repeticiones)
print("\n" + "-"*60 + "\n")

# 6) Retornar el texto invertido
invertido = texto[::-1]
print("6) Texto invertido:", invertido)
print("\n" + "-"*60 + "\n")

# Nota para el profesor: No sabía si los códigos iban en archivos 
# separados o todos juntos en un mismo archivo, así que lo hice en 
# un único archivo, separados por lineas para mayor facilidad.