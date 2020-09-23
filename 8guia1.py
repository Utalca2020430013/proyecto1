#Personas que solicitan trabajo
n = float(input("Ingrese la cantidad de personas que solicitan trabajo: "))
m = 0
print(" ")
edades = 0
b = 2020
#Ciclo
while m < n:
    a = float(input("Ingrese año de nacimiento del solicitante: "))
    a = b - a
    print("La edad del solicitante", m + 1 , " es: ", a, " años")
    edades = edades + a
    m = m + 1
#Promedio de edades
print(" ")
print("El promedio de edad de los solicitantes es: ", edades / n, "años")
