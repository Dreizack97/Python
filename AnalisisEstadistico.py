#Progama que calcule la media, varianza y desviación estandar, de los datos que introduzca el usuario.

import math

datos = []
sumatoria = 0
sumatoria_cuadrados = 0
noDatos = int(input("¿Cuántos datos deseas introducir?: "))

for i in range(noDatos):
    dato = float(input(f"Introduce el valor {i + 1}: "))
    sumatoria += dato
    sumatoria_cuadrados += dato ** 2
    datos.append(dato)

#Media
media = sumatoria / noDatos
print("La media es: ", media)

# Varianza
varianza = (sumatoria_cuadrados / noDatos) - (media ** 2)
print("La varianza es: ", varianza)

#Desviación estandar
desviacion_estandar = math.sqrt(varianza)
print("La desviación estándar es: ", desviacion_estandar)