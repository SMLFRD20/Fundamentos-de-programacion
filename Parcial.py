def capturar_notas():
    estudiantes = []

    while True:
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")
        matricula = input("Ingrese la matrícula del estudiante (formato: 24-1234): ")

        notas = []
        for i in range(1, 5):
            nota = float(input(f"Ingrese la nota {i}: "))
            while nota < 0 or nota > 100:
                print("La nota debe estar entre 0 y 100.")
                nota = float(input(f"Ingrese la nota {i}: "))
            notas.append(nota)

        promedio = sum(notas) / len(notas)

        if promedio <= 69:
            resultado = "1.0 y reprobó"
        elif 70 <= promedio <= 79:
            resultado = "2.0 y aprobó"
        elif 80 <= promedio <= 89:
            resultado = "3.0 y aprobó"
        elif 90 <= promedio <= 100:
            resultado = "4.0 y aprobó"

        estudiantes.append((nombre_estudiante, matricula, promedio, resultado))

        print(f"{nombre_estudiante} ({matricula}) tiene un promedio de {resultado}")

        otra_vez = input("¿Desea ingresar otro estudiante? (s/n): ")
        if otra_vez.lower() != 's':
            break

    print("\nPromedios de los estudiantes capturados:")
    for estudiante in estudiantes:
        nombre, matricula, promedio, resultado = estudiante
        print(f"{nombre} ({matricula}): {promedio:.2f} - {resultado}")

    print("Captura de datos finalizada.")

capturar_notas()