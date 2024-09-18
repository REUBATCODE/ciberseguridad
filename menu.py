import os
import subprocess

def limpiar_pantalla():
    os.system("clear")

def ejecutar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, check=True)
        return resultado
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {comando}")
        print(f"Detalles: {e}")

print("Sistema para pruebas de seguridad informatica")
print("Version 1.0")
print("Desarrollado por: Ruben Vega")

x = True

limpiar_pantalla()

while x:
    print("\nOpcion 1: Encontrar subdominios.")
    print("Opcion 2: Banner Grabbing.")
    print("Opcion 3: Wad.")
    print("Opcion 4: Escaneo de Puertos.")
    print("Opcion 5: Salir.")
    
    try:
        opcion = int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            victima = input("Ingrese el dominio: ")
            print("Encontrar subdominios")
            comando = f"python3 subdominios.py -t {victima}"
            ejecutar_comando(comando)
            input("Presione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == 2:
            victima = input("Ingrese el dominio: ")
            puerto = input("Ingrese el puerto: ")
            print("Banner Grabbing")
            comando = f"python3 bannergraby.py -t {victima} -p {puerto}"
            ejecutar_comando(comando)
            input("Presione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == 3:
            print("Wad")
            input("Presione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == 4:
            print("Escaneo de Puertos")
            input("Presione Enter para continuar...")
            limpiar_pantalla()

        elif opcion == 5:
            print("Saliendo del sistema...")
            x = False

        else:
            print("Opcion no valida, intenta de nuevo.")
    
    except ValueError:
        print("Error: Ingrese un numero valido.")
