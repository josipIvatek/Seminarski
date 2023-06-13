class Svirka:

    def __init__(self, datum, opis, cijena):
        self.__datum = datum
        self.__opis = opis
        self.__cijena = cijena


    @property
    def datum(self):
        return self.__datum

    @datum.setter
    def datum(self, datum):
        self.__datum = datum

    @property
    def opis(self):
        return self.__opis

    @opis.setter
    def opis(self, opis):
        self.__opis = opis

    @property
    def cijena(self):
        return self.__cijena

    @cijena.setter
    def cijena(self, cijena):
        self.__cijena = cijena


    def ispis(self):
        print("Informacije o svirci: ")
        print(f'\tDatum: {self.__datum}')
        print(f'\tOpis: {self.__opis}')
        print(f'\tCijena: {self.__cijena}')
