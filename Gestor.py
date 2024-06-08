import random

Clave ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Longitud =int(input("Ingresa La Longitud De Tu Contraseña"))

Elemento =""
for i in range(Longitud):
    Elemento += random.choice(Clave)

print (Elemento)



















