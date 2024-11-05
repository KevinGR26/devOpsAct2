import os
from datetime import datetime
import hashlib

# Diccionario para almacenar la relación entre el nombre del cliente y el nombre del archivo
clientes = {}

# Genera un hash único para el nombre del cliente
def generar_cliente_hash(nombre):
    return hashlib.sha256(nombre.encode()).hexdigest()

# Crea un archivo para un nuevo cliente
def crear_cliente(nombre, servicio):

    cliente_hash = generar_cliente_hash(nombre)
    archivo_path = f"./clientes/{cliente_hash}.txt"

    if not os.path.exists("clientes"):
        os.makedirs("clientes")
    
    with open(archivo_path, "w") as file:
        file.write(f"Nombre: {nombre}\n")
        file.write(f"Fecha de Registro: {datetime.now()}\n")
        file.write("Historial de Servicios:\n")
        file.write(f"- {servicio} (Fecha: {datetime.now()})\n")
    
    clientes[nombre] = archivo_path
    print(f"Archivo de cliente '{nombre}' creado con éxito.")

# Añade un servicio a un cliente existente
def agregar_servicio(nombre, servicio):

    archivo_path = clientes.get(nombre)

    if archivo_path and os.path.isfile(archivo_path):
        with open(archivo_path, "a") as file:
            file.write(f"- {servicio} (Fecha: {datetime.now()})\n")
        print(f"Servicio agregado al cliente '{nombre}'.")
    else:
        print("Cliente no encontrado.")

# Consulta la información de un cliente
def consultar_cliente(nombre):

    archivo_path = clientes.get(nombre)

    if archivo_path and os.path.isfile(archivo_path):
        with open(archivo_path, "r") as file:
            print(file.read())
    else:
        print("Cliente no encontrado.")

# Modifica la información de un cliente existente
def modificar_cliente(nombre, nuevo_servicio):
    agregar_servicio(nombre, nuevo_servicio)

# Elimina el archivo de un cliente
def eliminar_cliente(nombre):

    archivo_path = clientes.get(nombre)
    
    if archivo_path and os.path.isfile(archivo_path):
        os.remove(archivo_path)
        del clientes[nombre]
        print(f"Cliente '{nombre}' eliminado.")
    else:
        print("Cliente no encontrado.")

# Muestra una lista de todos los clientes registrados
def listar_clientes():
    print("Clientes registrados:")
    for nombre, archivo_path in clientes.items():
        print(f"- {nombre}: {archivo_path}")

# Menú para que el usuario elija la acción
def menu():
    while True:
        print("\n--- Menú de opciones ---")
        print("1. Crear nuevo cliente")
        print("2. Agregar servicio a un cliente existente")
        print("3. Consultar cliente")
        print("4. Modificar cliente")
        print("5. Eliminar cliente")
        print("6. Listar todos los clientes")
        print("7. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            servicio = input("Ingrese la descripción del servicio solicitado: ")
            crear_cliente(nombre, servicio)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del cliente: ")
            servicio = input("Ingrese la descripción del servicio solicitado: ")
            agregar_servicio(nombre, servicio)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del cliente: ")
            consultar_cliente(nombre)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del cliente: ")
            nuevo_servicio = input("Ingrese la nueva descripción del servicio: ")
            modificar_cliente(nombre, nuevo_servicio)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del cliente: ")
            eliminar_cliente(nombre)
        elif opcion == "6":
            listar_clientes()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


# Ejecutar el programa desde la función principal
if __name__ == "__main__":
    print("Bienvenido al sistema de gestión de clientes")
    menu()

