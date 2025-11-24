from Persona import Persona

# Diccionario: clave = número de tarjeta, valor = Persona
personas_impar = {}

def agregar_persona(persona: Persona):
    if persona.tarjeta % 2 != 0:
        personas_impar[persona.tarjeta] = persona
        return "Persona agregada a la lista IMPAR."
    else:
        return "El número de tarjeta es PAR. No se permite registrar personas con tarjeta PAR."

def consultar_impar():
    return personas_impar

def consultar_todas():
    return personas_impar  # Solo hay impares en este sistema

def consultar_por_tarjeta(num_tarjeta: int):
    # Solo busca en impares
    return personas_impar.get(num_tarjeta, None)


def eliminar_persona(num_tarjeta: int):
    if num_tarjeta in personas_impar:
        del personas_impar[num_tarjeta]
        return "Persona eliminada correctamente."
    return "No existe una persona con esa tarjeta IMPAR."

def editar_persona(num_tarjeta: int, nueva_persona: Persona):
    if num_tarjeta in personas_impar:
        personas_impar[num_tarjeta] = nueva_persona
        return "Persona editada correctamente."
    return "No existe una persona con esa tarjeta IMPAR."







