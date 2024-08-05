# Sergio Lugo 24-0951
# Trabajo final - Parte I: Juego de aventura de toma de decisiones.

import time

# Introducción
def mostrar_intro():
    intro = [
        "Te despiertas en un motel desolado...\n",
        f"{nombre_jugador}: \"¿Qué... ha pasado?\" murmuras confundido.\n",
        "El sonido de los caminantes en la distancia te regresa a la realidad de tu mundo.",
        "Un mundo marchito, consumido por una plaga,", 
        "que ha borrado todo rastro de esperanza que alguna vez tuviste.\n",
        "Las paredes del motel, tu actual refugio,",
        "ahora están impregnadas de un moho verdoso y un olor a podrido.\n",
        "Tienes que encontrar suministros y un refugio seguro.\n",
        "A tu lado se encuentran tus amigos:",
        "Alice, una joven aprendiz de enfermera",
        "y tu mejor amigo Jordan, que yace herido en el regazo de Alice,\n",
        "su respiración entrecortada y susurros de dolor llaman la atención de los caminantes.\n",
        "Su vida pende de un hilo, y la responsabilidad de su supervivencia recae sobre ti.\n",
        "Cada decisión que tomes podría ser la última.\n"
    ]
    
    for oracion in intro:
        print(oracion)
        time.sleep(2)

import random

# Variables
nombre_jugador = input("Por favor, ingresa tu nombre: ")
salud_jugador = 100
suministros = 5.0
inventario = {"botiquín": 1, "agua": 2, "comida": 3}
contador_decisiones = 0
amigos = ("Alice", "Jordan")
ubicaciones_visitadas = set()

# Estado del jugador
def mostrar_estado():
    print(f"\nEstado de {nombre_jugador}:")
    print(f"Salud: {salud_jugador}")
    print(f"Suministros: {suministros}")
    print("Inventario:")
    for item, cantidad in inventario.items():
        print(f"  {item.capitalize()}: {cantidad}")
    print(f"Ubicaciones visitadas: {', '.join(ubicaciones_visitadas)}\n")

# Escena 1
def escena_1():
    global salud_jugador, suministros, contador_decisiones
    print("Te encuentras en un mundo postapocalíptico lleno de estos caminantes.")
    print("Tienes que decidir rápidamente qué hacer.\n")
    decision = input("¿Quieres buscar suministros (1) o explorar una nueva ubicación (2)?\n ")
    
    if decision == "1":
        suministros += 1
        inventario["comida"] += 1
        print("\nHas encontrado suministros adicionales.\n")
    elif decision == "2":
        salud_jugador -= 10
        print("\nTe encontraste con un caminante y te hirieron. Salud disminuida en 10.\n")
    
    contador_decisiones += 1
    ubicaciones_visitadas.add("Inicio")
    mostrar_estado()
    escena_2()

# Escena 2
def escena_2():
    global salud_jugador, suministros, contador_decisiones
    
    print("Estás con tu amigo herido, Bob. Los caminantes se acercan.\n")
    decision = input("¿Quieres dejar a Bob atrás (1) o intentar salvarlo (2)? \n")
    
    if decision == "1":
        print("\nDecides dejar a Bob atrás. Continuas solo.\n")
    elif decision == "2":
        salud_jugador -= 20
        suministros -= 1
        inventario["botiquín"] -= 1
        print("\nIntentas salvar a Bob, pero te hieren nuevamente. Salud disminuida en 20 y suministros en 1.\n")
    
    contador_decisiones += 1
    ubicaciones_visitadas.add("Encuentro con Bob")
    mostrar_estado()
    escena_3()

# Escena 3
def escena_3():
    global salud_jugador, suministros, contador_decisiones
    print("Has llegado al refugio, pero está infestado de caminantes.\n")
    decision = input("¿Quieres luchar (1) o huir (2)? \n")
    
    if decision == "1":
        if suministros >= 2:
            suministros -= 2
            print("\nLuchas valientemente y logras despejar el refugio.\n")
        else:
            salud_jugador -= 30
            print("\nLuchas, pero te hieren gravemente. Salud disminuida en 30.\n")
    elif decision == "2":
        salud_jugador -= 10
        print("\nHuyes rápidamente, pero sufres heridas menores. Salud disminuida en 10.\n")
    
    contador_decisiones += 1
    ubicaciones_visitadas.add("Refugio")
    mostrar_estado()
    final()

# Final del juego
def final():
    global salud_jugador, contador_decisiones
    if salud_jugador > 0:
        print("Has sobrevivido... Por ahora.\n")
        print("Continuará.\n")
    else:
        print("No lograste sobrevivir. Fin del juego.\n")
    print(f"Tomaste {contador_decisiones} decisiones en total.\n")

# Iniciar juego
print(f"Bienvenido, {nombre_jugador}.\n")
mostrar_intro()
escena_1()
