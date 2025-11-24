from datos import Persona,consultar_impar, consultar_todas, consultar_por_tarjeta,eliminar_persona, editar_persona

def mostrar_impares():
    datos = consultar_impar()
    if not datos:
        print("\nNo hay personas con tarjeta IMPAR.\n")
        return
    for persona in datos.values():
        print(persona)

def mostrar_todas():
    datos = consultar_todas()
    if not datos:
        print("\nNo hay personas registradas.\n")
        return
    for persona in datos.values():
        print(persona)

def buscar_por_tarjeta():
    try:
        numero = int(input("Ingrese el número de tarjeta: "))
        persona = consultar_por_tarjeta(numero)
        if persona:
            print("\nPersona encontrada:\n", persona)
        else:
            print("\nNo existe una persona con esa tarjeta.\n")
    except ValueError:
        print("Número inválido.")

def eliminar():
    try:
        numero = int(input("Ingrese el número de tarjeta de la persona a eliminar: "))
        mensaje = eliminar_persona(numero)
        print("\n→", mensaje, "\n")
    except ValueError:
        print("Número inválido.")
        
def editar():
    try:
        numero = int(input("Ingrese el número de tarjeta de la persona a editar: "))
        nombre = input("Nuevo Nombre: ")
        edad = int(input("Nueva Edad: "))
        correo = input("Nuevo Correo: ")
        ciudad = input("Nueva Ciudad: ")
        tarjeta = int(input("Nuevo Número de tarjeta (IMPAR): "))

        nueva_persona = Persona(nombre, edad, correo, ciudad, tarjeta)
        mensaje = editar_persona(numero, nueva_persona)
        print("\n→", mensaje, "\n")
    except ValueError:
        print("Número inválido.")

