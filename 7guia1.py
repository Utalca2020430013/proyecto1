a = float(input("Ingrese cuánto desea pagar por hora trabajada: "))
b = float(input("Ingrese las horas trabajadas el día lunes: "))
c = float(input("Ingrese las horas trabajadas el día martes: "))
d = float(input("Ingrese las horas trabajadas el día miércoles: "))
e = float(input("Ingrese las horas trabajadas el día jueves: "))
f = float(input("Ingrese las horas trabajadas el día viernes: "))
g = float(input("Ingrese las horas trabajadas el día sábado: "))
print(" ")
mayor = 0
menor = 0

#Cálculo de mayor y menor sueldo
b = b * a
print("El día lunes ganó: $", b)

if b > mayor:
    mayor = b
    menor = b

c = c * a
print("El día martes ganó: $", c)

if c > mayor:
    mayor = c
if c < menor:
    menor = c

d = d * a
print("El día miércoles ganó: ", d)

if d > mayor:
    mayor = d
if d < menor:
    menor = d

e = e * a
print("El día jueves ganó: ", e)

if e > mayor:
    mayor = e
if e < menor:
    menor = e

f = f * a
print("El día viernes ganó: ", f)

if f > mayor:
    mayor = f
if f < menor:
    menor = f

g = g * a
print("El día sábado ganó: ", g)

if g > mayor:
    mayor = g
if g < menor:
    menor = g
print(" ")

#Suma total de la semana
sueldo = b + c + d + e + f + g

print("El sueldo al final de la semana es de: $", sueldo)
print(" ")
print("El saldo mayor de la semana fue: $", mayor)
print("")
print("El saldo menor de la semana fue: $", menor)
