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
  while True:
    valinta = input("> Anna myytävän tuotteen id tai nimi, varasto tai 'valmis': ").strip().lower()
    if valinta == "valmis":
     if ostoslista:
        print("\nMyydyt tuotteet:")
        kaikki_hintasumma = 0
        for ostos in ostoslista:
            hintasumma = ostos["hinta"] * ostos["maara"]
            kaikki_hintasumma += hintasumma
            print(f"{ostos['tuote']}: {ostos['maara']} kpl, yhteensä {hintasumma}€")
        print(f"Ostokset yhteensä: {kaikki_hintasumma}€ \n")
        while True:
          maksamista = input("(m)aksa tai (p)eruuta: ").strip().lower()
          if maksamista == "m":
             print("Tuotteet maksettu!")
             ostoslista.clear()
             break

          elif maksamista == "p":
             print("Ostoskori tyhjennetty!")
             ostoslista.clear()
             break
    elif valinta == "varasto":
        print("\nTuotteet varastossa:")
        tuotteet_id =[]
        for tuote in tuotteet:
            print(f"{tuote['id']} {tuote['tuote']} {tuote['varastosaldo']} kpl")
            tuotteet_id.append(tuote['id'])
        while True:
            vastaus = input("> (p)alaa, (t)ilaa tai (l)isää: ").strip().lower()
            if vastaus == "p":
                break
            elif vastaus == "t":
                tilattava_id = input("> Anna tilattavan tuotteen id: ").strip()
                if tilattava_id in tuotteet_id:
                    while True:
                      tilausmaara =input("> Anna tilattava määrä: ").strip()
                      if int(tilausmaara):
                        print("\nTuotteet varastossa:")
                        for tuote in tuotteet:
                            if tilattava_id == tuote['id']:
                                uusiMaara = int(tilausmaara) + int( tuote['varastosaldo'])
                                print(f"{tuote['id']} {tuote['tuote']} {uusiMaara} kpl")
                            else:
                             print(f"{tuote['id']} {tuote['tuote']} {tuote['varastosaldo']} kpl")
                        break    
            elif vastaus == "l":
                uusi_nimi = input("> Anna uuden tuotteen nimi: ").strip().capitalize()
                if uusi_nimi:
                    uusi_hinta = input(f" > Anna tuotteen {uusi_nimi} hinta: ").strip()
                    uusi_varastosaldo = input(f" > Anna tuotteen {uusi_nimi} varastosaldo: ").strip()
                    uusi_id = "000" + str(len(tuotteet) + 1)
                    
                    
                    uusi_tuote={
                                   "id": uusi_id,
                                   "tuote": uusi_nimi,
                                   "hinta": uusi_hinta,
                                   "varastosaldo": uusi_varastosaldo
                                }
                    tuotteet.append(uusi_tuote)
                    for tuote in tuotteet:
                       print(f"{tuote['id']} {tuote['tuote']} {tuote['varastosaldo']} kpl")


                    

    else: 
        tuote = next((tuote for tuote in tuotteet if tuote["id"] == valinta or tuote["tuote"].lower() == valinta.lower()), None)
        if not tuote:
                print("Tuotetta ei löydy!")
                continue

            
        while True:
                maara = int(input("Kuinka monta myydään? "))
                if maara <= 0 or maara > tuote["varastosaldo"]:
                   print(f" Varastossa on vain {tuote['varastosaldo']}.")
                else:
                     break
               
             

        
        ostos = {
                "id": tuote["id"],
                "tuote": tuote["tuote"],
                "hinta": tuote["hinta"],
                "maara": maara
            }
        ostoslista.append(ostos)
        
   
      
      

