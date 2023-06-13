from .svirka import Svirka
from utilities import unos_datuma, unos_cijelog_pozitivnog_broja

def unos_svirke(redni_broj):

    datum = unos_datuma('Uesite dan svirke: ')
    opis = input(f'Unesite opis {redni_broj} svirke: ')
    cijena = unos_cijelog_pozitivnog_broja(f'Unesite cijenu {redni_broj} svirke: ')

    return Svirka(datum, opis, cijena)