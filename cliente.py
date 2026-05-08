from excepciones import ClienteInvalidoError


class Cliente:

    def __init__(self, nombre, documento, correo, telefono):

        self.set_nombre(nombre)
        self.set_documento(documento)
        self.set_correo(correo)
        self.set_telefono(telefono)

    # ENCAPSULACIÓN
    def set_nombre(self, nombre):

        if not nombre.strip():
            raise ClienteInvalidoError(
                "El nombre no puede estar vacío."
            )

        self.__nombre = nombre

    def get_nombre(self):

        return self.__nombre

    def set_documento(self, documento):

        if not str(documento).isdigit():

            raise ClienteInvalidoError(
                "El documento debe ser numérico."
            )

        self.__documento = documento

    def get_documento(self):

        return self.__documento

    def set_correo(self, correo):

        if "@" not in correo or "." not in correo:

            raise ClienteInvalidoError(
                "Correo inválido."
            )

        self.__correo = correo

    def get_correo(self):

        return self.__correo

    def set_telefono(self, telefono):

        if not str(telefono).isdigit():

            raise ClienteInvalidoError(
                "Teléfono inválido."
            )

        self.__telefono = telefono

    def get_telefono(self):

        return self.__telefono

    def mostrar_info(self):

        return f"""
Cliente: {self.__nombre}
Documento: {self.__documento}
Correo: {self.__correo}
Teléfono: {self.__telefono}
"""
