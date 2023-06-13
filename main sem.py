from utilities import unos_intervala
from clan import unos_clana, ispis_clanova
from svirka import unos_svirke, ispis_svirki
from instrument import Instrument

clanovi = []
svirke = []
instrumenti = [
        Instrument('Prim'),
        Instrument('Basprim'),
        Instrument('Harmonika'),
        Instrument('Bas'),
        Instrument('Bugarija'),
        Instrument('Bubanj'),
]

blagajna = 0

running = True
while running:
    print('-'*20)
    print('1. Unos novog clana benda')
    print('2. Unos nove svirke') # unos datuma, opisa i cijene
    print('3. Ispis svih clanova benda') # ime, prezime, instrument
    print('4. Ispis svih svirki')
    print('5. Ispis zarade') # odabir člana -> ispis njegovih informacija i zarade
    print('6. Ispis svih informacija') # ispis svih članova, njihovih zarada i stanja blagajne
    print('7. Zaustavi program')
    print('-'*20)

    akcija = unos_intervala(1,7)

    if akcija == 1:
       clanovi.append(unos_clana(len(clanovi)+1))
    elif akcija == 2:
        svirke.append(unos_svirke(len(svirke)+1))
    elif akcija == 3:
        ispis_clanova(clanovi)
    elif akcija == 4:
        ispis_svirki(svirke)
    elif akcija == 5:
        pass
    elif akcija == 6:
       pass
    elif akcija == 7:
        running = False