x = []
y = []
z = []
r = []

def formatear(valor, variable):
    if valor > 1:
        return f"+{valor}{variable}"
    elif valor < -1:
        return f"{valor}{variable}"
    elif valor == 1:
        return f"+{variable}"
    elif valor == -1:
        return f"-{variable}"
    else:
        return ""

for i in range(1, 4):
    valorX = int(input(f"Introduce el valor de X en la ecuación {i}: "))
    x.append(valorX)

    valorY = int(input(f"Introduce el valor de Y en la ecuación {i}: "))
    y.append(valorY)

    valorZ = int(input(f"Introduce el valor de Z en la ecuación {i}: "))
    z.append(valorZ)

    valorR = int(input(f"Introduce el resultado de la ecuación {i}: "))
    r.append(valorR)

    print("")

print("Sistema de ecuaciones: ")
for i in range(3):
    termX = formatear(x[i], "X")
    termY = formatear(y[i], "Y")
    termZ = formatear(z[i], "Z")

    if termX.__contains__("+"):
        termX = termX.removeprefix("+")

    print(f"Ecuación {i + 1}: {termX}{termY}{termZ}={r[i]}")

def resolver_ecuaciones(x, y, z, r):
    # Paso 1: Despejar X de la primera ecuación
    def obtener_x(y_val, z_val):
        return (r[0] - y[0] * y_val - z[0] * z_val) / x[0]

    # Paso 2: Crear las ecuaciones resultantes para Y y Z
    def eq4(y_val, z_val):
        return x[1] * obtener_x(y_val, z_val) + y[1] * y_val + z[1] * z_val - r[1]

    def eq5(y_val, z_val):
        return x[2] * obtener_x(y_val, z_val) + y[2] * y_val + z[2] * z_val - r[2]

    # Buscar la solución
    for y_val in range(-100, 100):
        for z_val in range(-100, 100):
            if abs(eq4(y_val, z_val)) < 1e-5 and abs(eq5(y_val, z_val)) < 1e-5:
                x_val = obtener_x(y_val, z_val)
                return x_val, y_val, z_val

    return None

# Ejecutar la función de resolución
solucion = resolver_ecuaciones(x, y, z, r)
if solucion:
    x_sol, y_sol, z_sol = solucion
    print("\nSolución:")
    print(f"x = {x_sol}")
    print(f"y = {y_sol}")
    print(f"z = {z_sol}")
else:
    print("\nNo se encontró solución o el sistema es inconsistente.")