from Persona import Persona
from datos import agregar_persona
from listapersonas import mostrar_impares, mostrar_todas, buscar_por_tarjeta, eliminar,editar

def menu():
    while True:
        print("""
========= MENÚ =========
1. Agregar persona (solo tarjeta IMPAR)
2. Consultar personas IMPAR
3. Consultar TODAS
4. Buscar por número de tarjeta
5. Editar persona
6. Eliminar persona
7. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                correo = input("Correo: ")
                ciudad = input("Ciudad: ")
                tarjeta = int(input("Número de tarjeta (IMPAR): "))

                persona = Persona(nombre, edad, correo, ciudad, tarjeta)
                mensaje = agregar_persona(persona)
                print("\n→", mensaje, "\n")

            except Exception as e:
                print("Error:", e)

        elif opcion == "2":
            mostrar_impares()

        elif opcion == "3":
            mostrar_todas()

        elif opcion == "4":
            buscar_por_tarjeta()
            
        elif opcion == "5":
            editar()

        elif opcion == "6":
            eliminar()
            break

        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.\n")

menu()

