class Persona:
    def __init__(self, nombre: str, edad: int, correo: str, ciudad: str, tarjeta: int):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.ciudad = ciudad
        self.tarjeta = tarjeta

    # ===== GETTERS =====
    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def correo(self):
        return self._correo

    @property
    def ciudad(self):
        return self._ciudad

    @property
    def tarjeta(self):
        return self._tarjeta

    # ===== SETTERS =====
    @nombre.setter
    def nombre(self, valor):
        if valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor

    @edad.setter
    def edad(self, valor):
        if valor <= 0:
            raise ValueError("La edad debe ser mayor que 0.")
        self._edad = valor

    @correo.setter
    def correo(self, valor):
        if "@" not in valor:
            raise ValueError("Correo inválido.")
        self._correo = valor

    @ciudad.setter
    def ciudad(self, valor):
        if valor.strip() == "":
            raise ValueError("La ciudad no puede estar vacía.")
        self._ciudad = valor

    @tarjeta.setter
    def tarjeta(self, valor):
        if valor <= 0:
            raise ValueError("El número de tarjeta debe ser mayor a 0.")
        self._tarjeta = valor

    def __str__(self):
        return (f"\nNombre: {self._nombre}\nEdad: {self._edad}\nCorreo: {self._correo}"
                f"\nCiudad: {self._ciudad}\nTarjeta: {self._tarjeta}\n")



