import locale
import datetime
locale.setlocale(locale.LC_TIME, "fi_FI")

def paivan_viikonpaiva(paivan):
    try:
        paivan = paivan.split(".")
        paiva = int(paivan[0])
        kuukausi = int( paivan[1])
        vuosi = int(paivan[2])
        paivamaara = datetime.datetime(vuosi,kuukausi,paiva)
        return paivamaara.strftime("%A")  
    except ValueError:
        return "Virheellinen päivämäärä!"

def vuoden_paivat(year, viikonpaiva):
        viikonpaiva = viikonpaiva.lower()
        paivat = []
        alku = datetime.datetime(year, 1, 1)
        loppu = datetime.datetime(year, 12, 31)
        nykyinen = alku
        while nykyinen <= loppu:
            if nykyinen.strftime("%A") == viikonpaiva:
                paivat.append(nykyinen.strftime("%d.%m.%Y"))
            nykyinen += datetime.timedelta(days=1)
        return paivat
        