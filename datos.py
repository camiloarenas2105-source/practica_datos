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





