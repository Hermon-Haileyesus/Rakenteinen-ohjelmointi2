import json
from datetime import datetime
import sys

def laske_ika(nimi, syntymapaiva):
    syntyma_dt = datetime.strptime(syntymapaiva, "%d.%m.%Y")
    tanaan = datetime.today()
    ika = tanaan.year - syntyma_dt.year

    if (syntyma_dt.month, syntyma_dt.day) > (tanaan.month, tanaan.day):
        ika -= 1

    if ika < 0:
        raise ValueError("Syntymäpäivä ei saa olla tulevaisuudessa")

    return {"nimi": nimi, "ikä": ika}

def kasittele_tiedosto(henkilo):
    
    try:
        with open("henkilöt.txt", "r", encoding="utf-8") as tiedosto:
            henkilolista = [json.loads(rivi) for rivi in tiedosto]
    except FileNotFoundError:
        vastaus = input("Tiedostoa ei löytynyt. Haluatko luoda sen? (kyllä/ei): ").strip().lower()
        if vastaus == "kyllä":
            with open("henkilöt.txt", "w", encoding="utf-8") as tiedosto:
                pass 
            return "Tiedosto luotu"
        else:
            return "Ei tiedostoa"

    if any(h["nimi"] == henkilo["nimi"] for h in henkilolista):
        return "Henkilö on jo listattu"

    with open("henkilöt.txt", "a", encoding="utf-8") as tiedosto:
        tiedosto.write(json.dumps(henkilo, ensure_ascii=False) + "\n")

    return "OK"

def main():
    while True:
        try:
            nimi = input("Anna nimi: ").strip()
            if not nimi:
                raise ValueError("Nimi ei voi olla tyhjä.")

            syntymapaiva = input("Anna syntymäpäivä (pp.kk.vvvv): ").strip()
            if not syntymapaiva:
                raise ValueError("Syntymäpäivä ei voi olla tyhjä.")

            henkilo = laske_ika(nimi, syntymapaiva)
            tulos = kasittele_tiedosto(henkilo)
            print(tulos)

        except KeyboardInterrupt:
            print("\n Poistutaan, moikka!")
            sys.exit()
        except ValueError as e:
            print(f"Virhe: {e}. Yritä uudelleen.")

if __name__ == "__main__":
    main()