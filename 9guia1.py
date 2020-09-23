#Entrada de datos
a = float(input("Ingrese las horas que estuvo el cliente: "))
b = float(input("Ingrese cuánto desea cobrar por hora: "))
c = 0
#Transformación a entero
a = a * 10
if a % 10 == 0:
    a = a / 10
    print("Se debe cobrar: $", a * b)
else:
    c = a % 10
    a = a - c
    a = a / 10
    a = a + 1
    print("Se debe cobrar: $", a * b)
