#Calculador de Gastos

Comida = int(50)
entretenimiento = float(29.9)
Transporte = int(10)

print(f"Total gastado = {Comida + entretenimiento + Transporte}")

#Conversor de Edad a Dias

Edad = int(16)
Año = int(365)

print(f"Has vivido {Edad * Año} dias!")

#Calculador de Salario

nombre  = input("Cual es tu nombre? > ")
Salario = int(input("Tu salario >  "))
bonus = int(200)

Total = Salario + bonus

print(f"Tu salario total es {Total}")

#Mayoria de edad

Edad = int(input("Cual es tu edad? >  "))

if Edad >= 18:
    print("Eres mayor de edad!")

elif Edad < 18:
    print("Eres menor de edad")

else:
    print("Error! Pon algo valido")

#intercambio

A = float(input("Cual es el numero de A? >   "))
B = float(input("Cual es el numero de B? >   "))

A = A + B
B = A - B
A = A - B

print(f"A = {A} B = {B}")

#Promedio de notas

Nota1 = float(19.5)
Nota2 = float(13.5)
Nota3 = float(12.2)
Nota4 = float(5.5)
Nota5 = float(10.2)
Nota6 = float(19.9)

Total = Nota1 + Nota2 + Nota3 + Nota4 + Nota5 + Nota6

if Total < 30:
 print(f"Has fallado! Tu total de nota es {Total}")
 print("Necesitas almenos 30 puntos para pasar!")

elif Total >= 30:
   print(f"Has pasado! tu total de notas es {Total}")

else:
   print("No hay un numero de notas con el que pueda trabajar!")
   print("Lo siento")

print("Tareas terminadas")