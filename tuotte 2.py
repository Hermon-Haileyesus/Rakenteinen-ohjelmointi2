# Kassaohjelma käyttäen tuotteet-listaa
tuotteet = [
    {
        "id": "0001",
        "tuote": "Vasara",
        "hinta": 10,
        "varastosaldo": 3
    },
    {
        "id": "0002",
        "tuote": "Pora",
        "hinta": 15,
        "varastosaldo": 7
    },
    {
        "id": "0003",
        "tuote": "Saha",
        "hinta": 7,
        "varastosaldo": 10
    },
    {
        "id": "0004",
        "tuote": "Ruuvimeisseli",
        "hinta": 12,
        "varastosaldo": 4
    },
    {
        "id": "0005",
        "tuote": "Jakoavain",
        "hinta": 18,
        "varastosaldo": 6
    },
    {
        "id": "0006",
        "tuote": "Taltta",
        "hinta": 3,
        "varastosaldo": 9
    }
]

while True:
    ostoslista = []
    print("Anna myytävän tuotteen id tai nimi, tai 'valmis':")

    while True:
        syote = input("> ")

        if syote.lower() == "valmis":
            # Näytä ostoskori
            if ostoslista:
                print("\nMyydyt tuotteet:")
                kokonaissumma = 0
                for ostos in ostoslista:
                    summa = ostos["hinta"] * ostos["maara"]
                    kokonaissumma += summa
                    print(f"{ostos['tuote']}: {ostos['maara']} kpl, yhteensä {summa}€")
                print(f"\nOstokset yhteensä: {kokonaissumma}€")

                # Kysy maksutapahtuma
                while True:
                    maksuvalinta = input("\n(m)aksa tai (p)eruuta: ").lower()
                    if maksuvalinta == "m":
                        print("Tuotteet maksettu!")
                        break
                    elif maksuvalinta == "p":
                        print("Ostoskori tyhjennetty!")
                        ostoslista.clear()
                        break
                    else:
                        print("Virheellinen valinta! Valitse 'm' tai 'p'.")
                break
            else:
                print("Ostoskori on tyhjä!")
                break

        else:
            # Hae tuote id:n tai nimen perusteella
            tuote = next((tuote for tuote in tuotteet if tuote["id"] == syote or tuote["tuote"].lower() == syote.lower()), None)
            if not tuote:
                print("Tuotetta ei löydy!")
                continue

            # Kysy määrä
            while True:
                try:
                    maara = int(input("Kuinka monta myydään? "))
                    if maara <= 0 or maara > tuote["varastosaldo"]:
                        print(f"Virheellinen määrä! Varastossa on vain {tuote['varastosaldo']}.")
                    else:
                        break
                except ValueError:
                    print("Syötä kelvollinen numero.")

            # Lisää ostoslistaan
            ostos = {
                "id": tuote["id"],
                "tuote": tuote["tuote"],
                "hinta": tuote["hinta"],
                "maara": maara
            }
            ostoslista.append(ostos)
            print(f"{tuote['tuote']} lisätty ostoskoriin!")
