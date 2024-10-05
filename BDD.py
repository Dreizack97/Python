#Programa para conectarse a una base de datos MySQL con Python

import mysql.connector
import sys

try:
    mysql_conexion = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "4dministrador",
        database = "ModeloBD"
    )
except mysql.connector.Error as error:
    print("Error: ", format(error))
    sys.exit(1)

# Crear el cursor para ejecutar queries
cursor = mysql_conexion.cursor()

# Datos del cliente
idCliente = 991
nombreCliente = "Jorge Eduardo"
apellidoContacto = "Silva Prieto"
nombreContacto = "Jorge Silva"
telefono = "4621806090"
direccion1 = "Bernalejo"
ciudad = "Irapuato"
estado = "GTO"
codigoPostal = "36833"
pais = "México"
limiteCredito = 85000

# Query para insertar los datos
query = ("INSERT INTO clientes "
         "(idCliente, nombreCliente, apellidoContacto, nombreContacto, telefono, direccion1, ciudad, estado, codigoPostal, pais, limiteCredito) "
         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

# Ejecutar la query con los datos
cursor.execute(query, (idCliente, nombreCliente, apellidoContacto, nombreContacto, telefono, direccion1, ciudad, estado, codigoPostal, pais, limiteCredito))

# Query mostrar cliente creado
cursor.execute("SELECT IdCliente, nombreContacto, telefono FROM clientes WHERE IdCliente = 991")

print(f"{'IdCliente':<10} {'Nombre Contacto':<30} {'Teléfono':<15}")
print("-" * 60)

# Imprimir los resultados con formato de tabla
for (IdCliente, nombreContacto, telefono) in cursor:
    print(f"{IdCliente:<10} {nombreContacto:<30} {telefono:<15}")

print("\n")

# Query para consultar clientes
cursor.execute("SELECT IdCliente, nombreContacto, telefono FROM clientes LIMIT 5")

print(f"{'IdCliente':<10} {'Nombre Contacto':<30} {'Teléfono':<15}")
print("-" * 60)

# Imprimir los resultados con formato de tabla
for (IdCliente, nombreContacto, telefono) in cursor:
    print(f"{IdCliente:<10} {nombreContacto:<30} {telefono:<15}")

print("\n")

# Query para actualizar cliente
cursor.execute("UPDATE clientes SET telefono = '4620000000' WHERE IdCliente = '114'")

# Query para eliminar cliente creado
cursor.execute("DELETE FROM clientes WHERE IdCliente = '991'")

mysql_conexion.commit()

# Query mostrar cliente creado
cursor.execute("SELECT IdCliente, nombreContacto, telefono FROM clientes WHERE IdCliente = 991")

print(f"{'IdCliente':<10} {'Nombre Contacto':<30} {'Teléfono':<15}")
print("-" * 60)

print("\n")

# Imprimir los resultados con formato de tabla
for (IdCliente, nombreContacto, telefono) in cursor:
    print(f"{IdCliente:<10} {nombreContacto:<30} {telefono:<15}")

# Query para mostrar clientes
cursor.execute("SELECT IdCliente, nombreContacto, telefono FROM clientes LIMIT 5")

print(f"{'IdCliente':<10} {'Nombre Contacto':<30} {'Teléfono':<15}")
print("-" * 60)

# Imprimir los resultados con formato de tabla
for (IdCliente, nombreContacto, telefono) in cursor:
    print(f"{IdCliente:<10} {nombreContacto:<30} {telefono:<15}")

# Cerrar la conexión
cursor.close()
mysql_conexion.close()