#Realizar un programa que capture los resultados por equipo del deporte de su 
#preferencia y al final los imprima en pantalla.
equipos = {}
while True:
    nombre_equipo = input("Ingrese el nombre de un equipo de pelota: ")
    victorias = int(input(f"Ingrese las victorias para {nombre_equipo}: "))
    derrotas = int(input(f"Ingrese las derrotas para {nombre_equipo}: "))
    equipos[nombre_equipo] = (victorias, derrotas)
    otro_equipo = input("¿Desea ingresar otro equipo? (si/no): ")
    if otro_equipo.lower() != "si":
        break
print("\nResultados de los equipos:")
for equipo, resultados in equipos.items():
    victorias, derrotas = resultados
    print(f"{equipo}: {victorias} victorias, {derrotas} derrotas")