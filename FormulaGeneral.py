import math

a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))
c = int(input("Introduce el valor de c: "))

if a != 0:
    vs = abs(b*b - 4*a*c)

    x1 = (-b + math.sqrt(vs)) / (2*a)
    x2 = (-b - math.sqrt(vs)) / (2*a)

    print("Valor de X1: ", x1)
    print("Valor de X2: ", x2)
else:
    input("Valor de a no válido.") 