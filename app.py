# Konsolisovelluksen lopullinen pääohjelma

# Modulien ja kirjastojen lataukset
import kanta # Tietokannan käsittelyssä tarvittavat komponentit
import kysymys # Tietojen syöttämiseen liittyvät kysymisrutiinit
import luokat # Henkilö, Aikuinen ja Lapsi -luokkien määrittelyt

# Määrittely ja alustukset
tiedosto = 'painonhallinta.db' # Tietokantatiedoston määrittely

# Varsinainen ohjelma
while True:
    
    # Silmukka henkilötietojen kyselemiseen
    lisaa_henkiloita = input('Lisätäänkö uusia henkilöitä? K/e ')
    if lisaa_henkiloita.upper() != 'E':
        lisaa_henkiloita = 'K'

    while lisaa_henkiloita.upper() == 'K':

        # Kysytään henkilötiedot
        etunimi = input('etunimi: ')
        sukunimi = input('sukunimi: ')
        sukupuoli = kysymys.kysy_liukuluku('Sukupuoli nainen 0, mies 1: ', 0, 1)
        syntyma_aika = input('Syntymäaika (VVVV-KK-PP): ') 

        # Lisätään henkilö tietokantaan
        try:
            kanta.lisaa_henkilo(tiedosto, etunimi, sukunimi, sukupuoli, syntyma_aika)
        except:
            print('Tietokantaan tallennuksessa tapahtui virhe')
        
        # Kysytään halutaanko syöttää lisää henkilöitä
        lisaa_henkiloita = input('Lisätäänkö uusia henkilöitä? K/e ')
        if lisaa_henkiloita.upper() == 'E':
            break
        else:
            lisaa_henkiloita = 'K'
               

    # Silmukka mittaustietojen kyselemiseen
    lisaa_mittauksia = input('Lisätäänkö uusia mittaustuloksia? K/e ')
    while lisaa_mittauksia.upper() == 'K':
        henkilo_id = input('Anna henkilön id: ')
        pituus = kysymys.kysy_liukuluku('Pituus (cm): ', 100, 250)
        paino = kysymys.kysy_liukuluku('Paino (kg): ', 30, 200)
        
        # Lisätään mittaustulos tietokantaan
        try:
            kanta.lisaa_mittaus(tiedosto, henkilo_id, pituus, paino)
        except:
            print('Tietokantaan tallennuksessa tapahtui virhe')
        
        # Kysytään halutaanko jatkaa mittaustulosten syöttämistä
        lisaa_mittauksia = input('Lisätäänkö uusia mittaustuloksia? K/e ')
        if lisaa_mittauksia.upper() == 'E':
            break
        else:
            lisaa_mittauksia = 'K'

    # Silmukka olioiden luomiseen ja tulosten näyttämiseen
    lisaa_tuloksia = input('Lasketaanko uusia tuloksia? K/e ')
    while lisaa_tuloksia.upper() == 'K':
        henkilo_id = input('Anna henkilön id: ')
        
        # Haetaan henkilö- ja mittaustietodot tietokannan henkilon_viimeiset_tiedot-näkymästä
        tapahtui_virhe = False
        try:
            tietue = kanta.lue_viimeiset_tiedot(tiedosto, henkilo_id)
        except:
            print('Tietokannan lukemisessa tapahtui virhe')
            tapahtui_virhe = True

        if tapahtui_virhe == False:  
            etunimi = tietue[0][1]
            sukunimi = tietue[0][2]
            sukupuoli = tietue[0][3]
            pituus = tietue[0][4]
            paino =  tietue[0][5]
            ika = round(tietue[0][6])
            
        # Valitaan luodaanko aikuinen- tai lapsi-olio ja tulostetaan painoindeksi ja kehon rasvaprosentti  
        if ika < 18:
            lapsi = luokat.Lapsi(etunimi, sukunimi, pituus, paino, ika, sukupuoli)
            print('Painoindenksi on:', lapsi.painoindeksi())
            print('Kehon rasvaprosentti on:', lapsi.rasvaprosentti())
        else:
            tavoitepaino = float(input('Mikä on tavoitepaino: '))
            aikuinen = luokat.Aikuinen(etunimi, sukunimi, pituus, paino, ika, sukupuoli,tavoitepaino)
            print('Painoindenksi on:', aikuinen.painoindeksi())
            print('Kehon rasvaprosentti on:', aikuinen.rasvaprosentti())

        # Kysytään halutaanko halutaanko lisää tuloksia
        lisaa_tuloksia = input('Lasketaanko uusia tuloksia? K/e ')
        if lisaa_tuloksia.upper() == 'E':
            break
        else:
            lisaa_tuloksia = 'K'
