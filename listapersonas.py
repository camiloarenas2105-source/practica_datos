from datos import consultar_impar, consultar_todas, consultar_por_tarjeta

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

