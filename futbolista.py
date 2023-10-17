from deportista import Deportista


class Futbolista(Deportista):
    _listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, años, golesMarcados, tarjetasRojas, piernaHabil):
        super().__init__(nombre, edad, altura, sexo, "Futbol", años)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)

    def __str__(self):
        cadena = "Mi nombre es " + self.getNombre() + " soy profesional en el deporte " + self.getDeporte() + " Tengo " + str(
            self.getEdad()) + " años de edad y llevo " + str(self._añosPracticando) + " años en el deporte"

    def setTarjetasRojas(self, tarjetas):
        self._tarjetasRojas = tarjetas

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setGolesMarcados(self, goles):
        self._golesMarcados = goles

    def getGolesMarcados(self):
        return self._golesMarcados

    def setPiernaHabil(self, pierna):
        self._piernaHabil = pierna

    def getPiernaHabil(self):
        return self._piernaHabil

    @classmethod
    def setListaFutbolistas(cls, futbolistas):
        cls._listaFutbolistas = futbolistas

    @classmethod
    def getListaFutbolistas(cls):
        return cls._listaFutbolistas
