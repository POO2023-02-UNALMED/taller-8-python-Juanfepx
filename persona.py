class Persona():
    def __init__(self, nombre, edad, altura, sexo):
        self._edad = edad
        self._nombre = nombre
        self._sexo = sexo
        self._altura = altura

    def setEdad(self, edad):
        self._edad = edad

    def getEdad(self):
        return self._edad

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setSexo(self, sexo):
        self._sexo = sexo

    def getSexo(self):
        return self._sexo

    def setAltura(self, altura):
        self._altura = altura

    def getAltura(self):
        return self._altura
