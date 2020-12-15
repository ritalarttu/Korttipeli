from graphics import *
from kortti import *
import random

# VAKIOT
PAIKKA1X = 50
PAIKKA2X = 350
PAIKKA3X = 650
PAIKKA4X = 950
PAIKKA5X = 1250
PAIKKAY = 350
PAIKAN_LEVEYS = 200
PAIKAN_KORKEUS = 300
NAPIN_KORKEUS = 50
NAPIN_LEVEYS = 100
PAIKKA_JAKOX = 1100
PAIKKA_TUPLAUSX = 100
PAIKKA_PANOSX = 350
PAIKKA_NAPPIY = 750
ALKU_RAHA = 10
ALKU_PANOS = 1
JAKO = 6
PANOS = 8

# Kertoimet
VARISUORA_KERROIN = 20
NELJASAMAA_KERROIN = 15
VARI_KERROIN = 10
SUORA_KERROIN = 5
TAYSKASI_KERROIN= 4
KOLMESAMAA_KERROIN = 3
KAKSIPARIA_KERROIN = 2

# Voittotekstit
VARISUORA_TEKSTI = 'Sait värisuoran'
NELJASAMAA_TEKSTI = 'Sait neljä samaa'
VARI_TEKSTI = 'Sait värin'
SUORA_TEKSTI = 'Sait suoran'
TAYSKASI_TEKSTI = 'Sait täyskäden'
KOLMESAMAA_TEKSTI = 'Sait kolme samaa'
KAKSIPARIA_TEKSTI = 'Sait kaksi paria'
EIVOITTOA_TEKSTI = 'Ei voittoa'


# APUFUNKTIOITA
# Piirtää napin ja piirtää tekstin annettuun paikkaan
def piirra_nappi(kulmaX, kulmaY, teksti):
    nappi = Rectangle(Point(kulmaX, kulmaY), Point(kulmaX + NAPIN_LEVEYS, kulmaY + NAPIN_KORKEUS))
    nappi.draw(win)
    msg = Text(Point(kulmaX + 35, kulmaY + 20), teksti)
    msg.draw(win)

# Piirtää kortin ja piirtää kulmaan arvon ja maan annettuun paikkaan
def piirra_kortti(kulmaX, kulmaY, kortin_tieto):
    kortti = Rectangle(Point(kulmaX, kulmaY), Point(kulmaX + PAIKAN_LEVEYS, kulmaY + PAIKAN_KORKEUS))
    kortti.draw(win)
    msg = Text(Point(kulmaX+35, kulmaY+20), '{} {}' .format(kortin_tieto.anna_maa(), kortin_tieto.anna_arvo()))
    msg.draw(win)
    korttipaikat.append(kortti)
    return

# Kirjottaa annetun tekstin annettuun kohtaan
def piirra_teksti(kulmaX, kulmaY, teksti):
    msg = Text(Point(kulmaX, kulmaY), '{}' .format(teksti))
    msg.draw(win)
    
# Tarkastaa onko annettu koordinaatti jonkun kortin tai napin sisällä ja palauttaa kohteen nimen tai tyhjan
def tarkasta_koordinaatti(piste):
    if piste.x > PAIKKA1X and piste.x < PAIKKA1X + PAIKAN_LEVEYS and piste.y > PAIKKAY and piste.y < PAIKKAY + PAIKAN_KORKEUS:
        return 1
    elif piste.x > PAIKKA2X and piste.x < PAIKKA2X + PAIKAN_LEVEYS and piste.y > PAIKKAY and piste.y < PAIKKAY + PAIKAN_KORKEUS:
        return 2
    elif piste.x > PAIKKA3X and piste.x < PAIKKA3X + PAIKAN_LEVEYS and piste.y > PAIKKAY and piste.y < PAIKKAY + PAIKAN_KORKEUS:
        return 3
    elif piste.x > PAIKKA4X and piste.x < PAIKKA4X + PAIKAN_LEVEYS and piste.y > PAIKKAY and piste.y < PAIKKAY + PAIKAN_KORKEUS:
        return 4
    elif piste.x > PAIKKA5X and piste.x < PAIKKA5X + PAIKAN_LEVEYS and piste.y > PAIKKAY and piste.y < PAIKKAY + PAIKAN_KORKEUS:
        return 5
    elif piste.x > PAIKKA_JAKOX and piste.x < PAIKKA_JAKOX + NAPIN_LEVEYS and piste.y > PAIKKA_NAPPIY and piste.y < PAIKKA_NAPPIY + NAPIN_KORKEUS:
        return 6
    elif piste.x > PAIKKA_TUPLAUSX and piste.x < PAIKKA_TUPLAUSX + NAPIN_LEVEYS and piste.y > PAIKKA_NAPPIY and piste.y < PAIKKA_NAPPIY + NAPIN_KORKEUS:
        return 7
    elif piste.x > PAIKKA_PANOSX and piste.x < PAIKKA_PANOSX + NAPIN_LEVEYS and piste.y > PAIKKA_NAPPIY and piste.y < PAIKKA_NAPPIY + NAPIN_KORKEUS:        
        return 8    
    else:
        return 0

# Tehdään alku näyttö
def alku_grafiikat():
    piirra_teksti(750, 500, 'VALITSE PANOS JA PAINA JAKO')
    piirra_nappi(PAIKKA_PANOSX, PAIKKA_NAPPIY, 'PANOS')
    piirra_nappi(PAIKKA_JAKOX, PAIKKA_NAPPIY, 'JAKO')
    piirra_teksti(1000, 75, 'PANOS: {}' .format(panos))
    piirra_teksti(1200, 75, 'RAHA: {}' .format(raha))
        
# Piirretään pelilaudalle tarvittavat grafiikat
def grafiikat(raha, panos):
    piirra_kortti(PAIKKA1X, PAIKKAY, pakka[0])
    piirra_kortti(PAIKKA2X, PAIKKAY, pakka[1])
    piirra_kortti(PAIKKA3X, PAIKKAY, pakka[2])
    piirra_kortti(PAIKKA4X, PAIKKAY, pakka[3])
    piirra_kortti(PAIKKA5X, PAIKKAY, pakka[4])
    piirra_nappi(PAIKKA_JAKOX, PAIKKA_NAPPIY, 'JAKO')
    piirra_nappi(PAIKKA_TUPLAUSX, PAIKKA_NAPPIY, 'TUPLAUS')
    piirra_nappi(PAIKKA_PANOSX, PAIKKA_NAPPIY, 'PANOS')
    piirra_teksti(1200, 75, 'RAHA: {}' .format(raha))
    piirra_teksti(1000, 75, 'PANOS: {}' .format(panos))

# Funktiolle annetaan suuri/pieni ja palauttaa onnistuiko tuplaus
# EI OLE KÄYTÖSSÄ
def tuplaus(vastaus):
    lista = luo_pakka()

    if vastaus == 'suuri':
        if lista[0].anna_arvo > 7:
            return True and lista[0]
    elif vastaus == 'pieni':
        if lista[0].anna_arvo < 7:
            return True and lista[0]
    else:
        return False and lista[0]

def tyhjenna_ruutu(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def onko_varisuora():
    return onko_vari() and onko_suora()
    

def onko_vari():
    for n in range(1,5):
        if not pakka[0].anna_maa() == pakka[n].anna_maa():
            return False
    return True

def onko_suora():
    # Tarkistaa onko 2 samaa jos on niin suora ei ole mahdollinen
    for n in range(0,4):
        for m in range(n+1,5):
            if pakka[n].anna_arvo() == pakka[m].anna_arvo():
                return False
    pienin = 0
    suurin = 0
    for n in range(0,5):
        if pakka[n].anna_arvo() < pienin or pienin == 0:
            pienin = pakka[n].anna_arvo()
        if pakka[n].anna_arvo() > suurin or suurin == 0:
            suurin = pakka[n].anna_arvo()
    if pienin + 4 == suurin:
        return True
    else:
        return False

def onko_tayskasi():
    a = 0
    b = 0
    for n in range(0,5):
        if pakka[n].anna_arvo() == a or a == 0:
            a = pakka[n].anna_arvo()
        elif pakka[n].anna_arvo() == b or b == 0:
            b = pakka[n].anna_arvo()
        else:
            return False
    return not onko_4samaa()

def onko_4samaa():
    for n in range(0,2):
        for m in range(n+1,3):
            for l in range(m+1,4):
                for k in range(l+1,5):
                    if pakka[n].anna_arvo() == pakka[m].anna_arvo() == pakka[l].anna_arvo() == pakka[k].anna_arvo():
                        return True
    return False

def onko_3samaa():
    for n in range(0,3):
        for m in range(n+1,4):
            for l in range(m+1,5):
                if pakka[n].anna_arvo() == pakka[m].anna_arvo() == pakka[l].anna_arvo():
                    return True
    return False

# Tarkastaa löytyykö 2 paria ja palauttaa true / false
def onko_2paria():
    onko_pareja = 0
    # Käydään läpi kaikki mahdolliset parit ja etsitään samoja kortin arvoja
    for n in range(0,4):
        for m in range(n+1,5):
            if pakka[n].anna_arvo() == pakka[m].anna_arvo():
                onko_pareja = onko_pareja + 1
    # Jos löytyi yli 1 paria, palautetaan true
    if onko_pareja > 1:
        return True
    else:
        return False

# Tarkistetaan löytyykö voittoja. Aloitetaan isoimmista voitoista        
def tarkasta_voitot():
    if onko_varisuora():
        print ('värisuora') # X 20
        return VARISUORA_KERROIN, VARISUORA_TEKSTI
    elif onko_4samaa():
        print ('neljä samaa') # X 15
        return NELJASAMAA_KERROIN, NELJASAMAA_TEKSTI
    elif onko_tayskasi():
        print('täyskäsi') # X 10
        return TAYSKASI_KERROIN, TAYSKASI_TEKSTI
    elif onko_vari():
        print ('väri') # X 5
        return VARI_KERROIN, VARI_TEKSTI
    elif onko_suora():
        print ('suora') # X 4
        return SUORA_KERROIN, SUORA_TEKSTI
    elif onko_3samaa():
        print ('kolmoset') # X 3
        return KOLMESAMAA_KERROIN, KOLMESAMAA_TEKSTI
    elif onko_2paria():
        print('2 paria') # X 2
        return KAKSIPARIA_KERROIN, KAKSIPARIA_TEKSTI
    else:
        print('ei voittoja')
        return 0, EIVOITTOA_TEKSTI

# Luodaan uusi 52 kortin pakka ja sekoitetaan se
def luo_pakka():
    pakka = [] # Kaikki pakan kortit
    maat = ['pata', 'risti', 'ruutu', 'hertta']

    # Luodaan pakkaan kaikki kortit (ei jokereita)
    for n in range(0,4):
        for m in range(2,15):
            pakka.append(Kortti(maat[n], m))

    # Sekoitetaan pakka
    random.shuffle(pakka)
    return pakka



################
# PÄÄOHJELMA ALKAA TÄSTÄ
################

# Määritetään ikkuna
win = GraphWin('Test', 1500, 1000)

#Luodaan loputon silmukka
while True:
    # Pelaajan rahamäärä
    raha = ALKU_RAHA
    panos = ALKU_PANOS

    # Peli alkaa
    jako_painettu = 0
    while jako_painettu != 1:
        alku_grafiikat()
        hKoord = win.getMouse()
        painettu_kohde = tarkasta_koordinaatti(hKoord)
        if painettu_kohde == JAKO:
            jako_painettu = 1
        elif painettu_kohde == PANOS:
            if panos == 5 or panos == raha:
                panos = ALKU_PANOS
                tyhjenna_ruutu(win)
            else:
                panos = panos + 1
                tyhjenna_ruutu(win)
            
    tyhjenna_ruutu(win)

    # Silmukka jossa kierretään koko pelin ajan
    while True:
        # Katsotaan onko rahaa
        if raha == 0:
            break
        # Katsotaan ettei panos ole liian iso
        if panos > raha:
            panos = raha

        # Yleiset muuttujat
        korttipaikat = [] # Tähän tallennetaan korttipaikkoja kuvaavat nelikulmiot
        lukitut_kortit = [0, 0, 0, 0, 0] # Kortit jotka lukitaan merkitään 1, muut kortit vaihdetaan

        pakka = luo_pakka()

        ##### DEBUG KOODIA, POISTA!
        #pakka[0] = Kortti(maat[0], 14)
        #pakka[1] = Kortti(maat[0], 13)
        #pakka[2] = Kortti(maat[0], 12)
        #pakka[3] = Kortti(maat[0], 11)
        #pakka[4] = Kortti(maat[0], 10)

        raha = raha - panos
        
        # Piirretään pelilaudalle tarvittavat grafiikat
        grafiikat(raha, panos)
        piirra_teksti(750, 250, 'Lukitse haluamasi kortit')

        jako_painettu = 0

        # Ensimmäinen jako
        while jako_painettu != 1:
            hKoord = win.getMouse()
            painettu_kohde = tarkasta_koordinaatti(hKoord)
            
            # Kortin lukitseminen ja vapauttaminen
            if painettu_kohde > 0 and painettu_kohde < JAKO:
                if lukitut_kortit[painettu_kohde - 1] == 0:
                    lukitut_kortit[painettu_kohde - 1] = 1
                    korttipaikat[painettu_kohde - 1].setOutline('red')
                else:
                    lukitut_kortit[painettu_kohde - 1] = 0
                    korttipaikat[painettu_kohde - 1].setOutline('black')    
            
            
            # Jako-nappia painettu
            elif painettu_kohde == JAKO:
                for n in range(0, 5):
                    if lukitut_kortit[n] == 0:
                        pakka[n] = pakka[n + 5]
                tyhjenna_ruutu(win)
                grafiikat(raha, panos)
                jako_painettu = 1
                


        jako_painettu = 0

        # Kertoo pelaajalle mikä voitto tuli ja antaa voittosumman
        voitto_kerroin, voitto_teksti = tarkasta_voitot()
        raha = raha + panos * voitto_kerroin
        tyhjenna_ruutu(win)
        grafiikat(raha, panos)
        piirra_teksti(750, 250, voitto_teksti)

        # Uusi jako
        while jako_painettu != 1:
            hKoord = win.getMouse()
            painettu_kohde = tarkasta_koordinaatti (hKoord)
        # Panos nappia painettu    
            if painettu_kohde == PANOS:
                if panos == 5 or panos == raha:
                    panos = ALKU_PANOS
                    tyhjenna_ruutu(win)
                    grafiikat(raha, panos)
                else:
                    panos = panos + 1
                    tyhjenna_ruutu(win)
                    grafiikat(raha, panos)

            elif painettu_kohde == 7:
                tuplaus('suuri')
                
            # Jako-nappia painettu
            elif painettu_kohde == 6:
                jako_painettu = 1
            piirra_teksti(750, 250, voitto_teksti)
        tyhjenna_ruutu(win)
    # Peli loppu
    tyhjenna_ruutu(win)
