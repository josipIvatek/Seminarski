class Clan:

    def __init__(self, ime, prezime, instrument):
        self.__ime = ime
        self.__prezime = prezime
        self.__instrument = instrument

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    @property
    def instrument(self):
        return self.__instrument

    @instrument.setter
    def instrument(self, instrument):
        self.__instrument = instrument

    def ispis(self):
      print("Informacije o clanu benda: ")
      print(f'\tIme: {self.__ime}')
      print(f'\tPrezime: {self.__prezime}')
      print(f'\tinstrument: {self.__instrument}')

