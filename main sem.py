from utilities import unos_intervala
from clan import unos_clana, ispis_svih_clanova
from svirka import unos_svirke, ispis_svih_svirki
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
ukupna_zarada = 0

running = True
while running:
    print('-'*20)
    print('1. Unos novog clana benda')
    print('2. Unos nove svirke') # unos datuma, opisa i cijene
    print('3. Ispis svih clanova benda') # ime, prezime, instrument
    print('4. Ispis svih svirki')
    print('5. Ispis zarade') # odabir člana -> ispis njegovih informacija i zarade
    print('6. Ispis blagajne') # ispis stanja blagajne
    print('7. Zaustavi program')
    print('-'*20)

    akcija = unos_intervala(1,7)

    if akcija == 1:
       clanovi.append(unos_clana(len(clanovi)+1))
    elif akcija == 2:
        svirke.append(unos_svirke(len(svirke)+1))
        ukupna_zarada = ukupna_zarada + svirke[len(svirke)-1].cijena
    elif akcija == 3:
        ispis_svih_clanova(clanovi)
    elif akcija == 4:
        ispis_svih_svirki(svirke)
    elif akcija == 5:
        print('Odaberite clana:')
        ispis_svih_clanova(clanovi)
        odabrani_clan = unos_intervala(1, len(clanovi))
        clanovi[odabrani_clan].ispis()
        x = ukupna_zarada/len(clanovi) #pojedinacna zarada, decimalna
        y = int(x) #cijeli broj pojedinacne zarade
        z = y % 10 #ostatak od desetice
        pojedinacna_zarada = y - z #pojedinacna zarada zaokruzena na manju deseticu
        print(f'Zarada: {pojedinacna_zarada}')
    elif akcija == 6:
        stanje_blagajne = ukupna_zarada % len(clanovi)
        print(f'{stanje_blagajne}')
    elif akcija == 7:
        running = False