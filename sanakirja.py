sanakirja = {"auto":"car", "tietokone":"computer","vasara":"hammer","tammikuu":"january","helmikuu":"february",
             "toukokuu":"may", "veitsi":"knif", "haarukka":"fork","maanantai":"monday", "perjantai":"friday"}
def etsi_sana(sana):
    
   if sana in sanakirja:
        print(f'"{sana}" on "{sanakirja[sana]}"!')
   elif sana in sanakirja.values():
        for avain, arvo in sanakirja.items():
            if arvo == sana:
                print(f'"{sana}" on suomeksi "{avain}"!')
        
   else:
        print(f"{sana} ei löydy!")

def lisaa_sana(lahtosana, kohdesana):
    sanakirja[lahtosana] = kohdesana



while True:
    valinta = input("> Haluatko (h)akea vai (l)isätä sanan? ").strip().lower()
    if valinta == "h":
        sana = input("> Anna sana: ").strip().lower()
        etsi_sana(sana)
    elif valinta == "l":
        lahtosana = input("> Anna sana lähtökielellä: ").strip().lower()
        kohdesana =  input("> Anna sana kohdekielellä:").strip().lower()
        lisaa_sana(lahtosana,kohdesana)
    else:
        print("Virhellinen syöte, yrittää uudelleen!")
