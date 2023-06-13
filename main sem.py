from utilities import unos_intervala
from clan import unos_clana
from svirka import unos_svirke

clanovi = []
svirke = []
instrumenti = [prim, basprim, harmonika, bas, bugarija, bubanj]
blagajna = 0

running = True
while running:
    print('-'*20)
    print('1. Unos novog clana benda')
    print('2. Unos nove svirke') # unos datuma, opisa i cijene
    print('4. Ispis svih clanova benda') # ime, prezime, instrument
    print('5. Ispis zarade') # odabir člana -> ispis njegovih informacija i zarade
    print('6. Ispis svih informacija') # ispis svih članova, njihovih zarada i stanja blagajne
    print('7. Zaustavi program.')
    print('-'*20)

    akcija = unos_intervala(1,7)

    if akcija == 1:
       clanovi.append(unos_clana(len(clanovi)+1))
    elif akcija == 2:
        svirke.append(unos_svirke(len(svirke)+1))
    elif akcija == 3:
        pass#prodaje.append(unos_prodaje(korisnici, kategorije, len(prodaje)+1))
    elif akcija == 4:
        pass #ispis_svih_korisnika(korisnici)
    elif akcija == 5:
        pass #ispis_svih_kategorija(kategorije)
    elif akcija == 6:
        pass #ispis_svih_prodaja(prodaje)
    elif akcija == 7:
        running = False
