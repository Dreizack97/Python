#Resolución de un sistema de ecuaciones de 3 por 3 por el método de determinantes.

print("Introduce los coeficientes de la matriz A (3x3):")
A = []

for i in range(3):
    fila = []
    for j in range(3):
        coef = float(input(f"Introduce el coeficiente a[{i}][{j}]: "))
        fila.append(coef)
    A.append(fila)

print("Introduce los términos independientes del vector B (3x3):")
B = []

for i in range(3):
    term = float(input(f"Introduce el término independiente b[{i}]: "))
    B.append(term)

determinante = A[0][0] * ((A[1][1] * A[2][2]) - (A[1][2] * A[2][1])) - A[0][1] * ((A[1][0] * A[2][2]) - (A[1][2] * A[2][0])) + A[0][2] * ((A[1][0] * A[2][1]) - (A[1][1] * A[2][0]))
determinante_x = B[0] * ((A[1][1] * A[2][2]) - (A[1][2] * A[2][1])) - A[0][1] * ((B[1] * A[2][2]) - (A[1][2] * B[2])) + A[0][2] * ((B[1] * A[2][1]) - (A[1][1] * B[2]))
determinante_y = A[0][0] * ((B[1] * A[2][2]) - (A[1][2] * B[2])) - B[0] * ((A[1][0] * A[2][2]) - (A[1][2] * A[2][0])) + A[0][2] * ((A[1][0] * B[2]) - (B[1] * A[2][0]))
determinante_z = A[0][0] * ((A[1][1] * B[2]) - (B[1] * A[2][1])) - A[0][1] * ((A[1][0] * B[2]) - (B[1] * A[2][0])) + B[0] * ((A[1][0] * A[2][1]) - (A[1][1] * A[2][0]))
print("Determinante: ", determinante)
print("Determinante X: ", determinante_x)
print("Determinante Y: ", determinante_y)
print("Determinante Z: ", determinante_z)

if determinante_x == 0 or determinante_y == 0 or determinante_z == 0:
    print("El sistema no tiene solución.")
elif determinante == 0:
    print("El sistema tiene un número infinito de soluciones.")
else:
    #Calculo de la variable X
    x = determinante_x / determinante
    print("El valor de X = ", x)

    #Calculo de la variable Y
    y = determinante_y / determinante
    print("El valor de Y = ", y)

    #Calculo de la variable Z
    z = determinante_z / determinante
    print("El valor de Z = ", z)