a = float (input("Ingrese el valor de su primera prenda: "))
b = float (input("Ingrese el valor de su segunda prenda: "))
c = float (input("Ingrese el valor de su tercera prenda: "))
d = float
# Aplicación de descuentos
if a > 10000:
    a = (a * 85) / 100
    print("El precio final de su primera prenda es de: $", a)
elif a <= 10000:
    a = (a * 92) / 100
    print("El precio final de su primera prenda es de: $", a)

if b > 10000:
    b = (b * 85) / 100
    print("El precio final de su segunda prenda es de: $", b)
elif b <= 10000:
    b = (b * 92) / 100
    print("El precio final de su segunda prenda es de: $", b)

if c > 10000:
    c = (c * 85) / 100
    print("El precio final de su tercera prenda es de: $", c)
elif a <= 10000:
    c = (c * 92) / 100
    print("El precio final de su tercera prenda es de: $", c)

# Valor total de la compra
d = a + b + c
print("El total de su compra con el descuento aplicado es de: $", d)
