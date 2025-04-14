import Tehtävä16d_moduuli

def main():
    paivan = input("Anna päivämäärä (suomalaisessa formaatissa esim. 15.9.2023): ")
    viikonpaiva = Tehtävä16d_moduuli.paivan_viikonpaiva(paivan)
    print(f"Päivämäärän {paivan} viikonpäivä on: {viikonpaiva}")

    year = int(input("Anna vuosi: "))
    viikonpaiva = input("Anna viikonpäivä: ")
    paivat = Tehtävä16d_moduuli.vuoden_paivat(year, viikonpaiva)
    if len(paivat) > 0 :
        print(f"Vuoden {year} kaikki päivät, jotka ovat {viikonpaiva}:")
        for paiva in paivat:
            print(paiva)
    else:
        print("Virhellinen syöte!")

if __name__ == "__main__":
    main()