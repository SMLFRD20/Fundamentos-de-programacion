#Iteración de nombres que los imprime  si tienen 3 o más vocales.
vocales=("a","e","i","o","u")
nombre_usuario=input("Ingrese su nombre (solo minúsculas): ")
cont=0
for i in nombre_usuario:
  if i in vocales:
    cont+=1
    if cont>=3:
      print("Su nombre" ,nombre_usuario, "tiene tres vocales o más.")
      break