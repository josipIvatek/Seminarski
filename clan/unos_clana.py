from .clan import Clan
from utilities import unos_intervala

def unos_clana(redni_broj):

    ime = input(f'Unesite ime {redni_broj}. clana benda: ').capitalize()
    prezime = input(f'Unesite prezime {redni_broj}. clana bena: ').capitalize()
    print('Odaberite instrument:')
    print('\t1. Prim')
    print('\t2. Basprim')
    print('\t3. Harmonika')
    print('\t4. Bas')
    print('\t5. Bugarija')
    print('\t6. Bubanj')
    instrument = unos_intervala(1,6)

    return Clan(ime, prezime, instrument)