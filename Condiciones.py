print("Introduce la temperatura actual:")
temperatura = float(input())

print("¿Cuanto dinero tienes?")
dinero = int(input())

if (temperatura >= 27 and dinero >= 5):
    print("Compra un helado.")
    dinero -= 5

print("Tu cambio es: " + str(dinero))
print("Adios")