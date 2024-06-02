# Realizar un programa que calcule el promedio de notas de un estudiante
nombre_estudiante = input("Ingrese el nombre del estudiante:")
Nota_1 = int(input("Ingrese la primera nota:"))
Nota_2 = int(input("Ingrese la segunda nota:"))
Nota_3 = int(input("Ingrese la tercera nota:"))
Resultado = (Nota_1 + Nota_2 + Nota_3) / 3
if Resultado <= 69:
    print(nombre_estudiante, "tiene un promedio de 1.0 y reprobó")

elif Resultado >= 70 and Resultado <= 79:
    print(nombre_estudiante, "tiene un promedio de 2.0 y aprobó")

elif Resultado >= 80 and Resultado <= 89:
    print(nombre_estudiante, "tiene un promedio de 3.0 y aprobó")

elif Resultado >= 90 and Resultado <= 100:
    print("¡Felicidades!",nombre_estudiante, "tiene un promedio de 4.0 y aprobó")
