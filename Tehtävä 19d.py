import lemmikit
import sys

lemmikit_lista = []

def luo_lemmikki():
    print("Valitse lemmikin tyyppi: ")
    print("1. Koira")
    print("2. Chihuahua")
    print("3. Puudeli")
    print("4. Kissa")
    print("5. Papukaija")

    valinta = input("Syötä numero: ")
    nimi = input("Anna lemmikille nimi: ")
    lempiruoka = input("Mikä on lemmikin lempiruoka? ")
    syntymavuosi = int(input("Anna lemmikin syntymävuosi: "))
    """#Loop for numeric inputs with exception handling
while True:
    try:
        syntymavuosi = int(input("Anna lemmikin syntymävuosi: "))
        kuolan_maara = int(input("Kuinka paljon chihuahua kuolaa? "))
        break  # Lopettaa silmukan, jos molemmat syötteet ovat kelvollisia
    except ValueError:
        print("Virheellinen syöte! Molempien arvojen tulee olla numeroita. Yritä uudelleen.")

# Loop for string inputs to prevent empty values
while True:
    nimi = input("Anna lemmikille nimi: ").strip()
    if nimi:
        break
    print("Lemmikin nimi ei voi olla tyhjä! Yritä uudelleen.")

while True:
    lempiruoka = input("Mikä on lemmikin lempiruoka? ").strip()
    if lempiruoka:
        break
    print("Lempiruoka ei voi olla tyhjä! Yritä uudelleen.")"""

    if valinta == "1":
        kuolan_maara = int(input("Kuinka paljon koira kuolaa? "))
        lemmikki = lemmikit.Koira(nimi, lempiruoka, syntymavuosi, kuolan_maara)
    elif valinta == "2":
        kuolan_maara = int(input("Kuinka paljon chihuahua kuolaa? "))
        lemmikki = lemmikit.Chihuahua(nimi, lempiruoka, syntymavuosi, kuolan_maara)
    elif valinta == "3":
        kuolan_maara = int(input("Kuinka paljon puudeli kuolaa? "))
        pehmeys = int(input("Kuinka pehmeä puudeli on asteikolla 1-10? "))
        lemmikki = lemmikit.Puudeli(nimi, lempiruoka, syntymavuosi, kuolan_maara, pehmeys)
    elif valinta == "4":
        karvan_maara = int(input("Kuinka paljon kissalla on karvaa? "))
        kynsien_teravyys = int(input("Kuinka terävät kynnet ovat asteikolla 1-10? "))
        lemmikki = lemmikit.Kissa(nimi, lempiruoka, syntymavuosi, karvan_maara, kynsien_teravyys)
    elif valinta == "5":
        vari = input("Mikä on papukaijan väri? ")
        lemmikki = lemmikit.Papukaija(nimi, lempiruoka, syntymavuosi, vari)
    else:
        print("Virheellinen valinta.")
        return

    lemmikit_lista.append(lemmikki)
    print(f"{lemmikki.nimi} on luotu!")
def luo_lemmikki():
    print("Valitse lemmikin tyyppi: ")
    print("1. Koira")
    print("2. Chihuahua")
    print("3. Puudeli")
    print("4. Kissa")
    print("5. Papukaija")

    valinta = input("Syötä numero: ").strip()
    nimi = input("Anna lemmikille nimi: ").strip()
    lempiruoka = input("Mikä on lemmikin lempiruoka? ").strip()
    
    try:
        syntymavuosi = int(input("Anna lemmikin syntymävuosi: "))
    except ValueError:
        print("Virheellinen syöte! Syntymävuoden tulee olla numero.")
        return

    if valinta == "1":
        try:
            kuolan_maara = int(input("Kuinka paljon koira kuolaa? "))
        except ValueError:
            print("Virheellinen syöte! Kuolan määrän tulee olla numero.")
            return
        lemmikki = lemmikit.Koira(nimi, lempiruoka, syntymavuosi, kuolan_maara)

    elif valinta == "2":
        try:
            kuolan_maara = int(input("Kuinka paljon chihuahua kuolaa? "))
        except ValueError:
            print("Virheellinen syöte! Kuolan määrän tulee olla numero.")
            return
        lemmikki = lemmikit.Chihuahua(nimi, lempiruoka, syntymavuosi, kuolan_maara)

    elif valinta == "3":
        try:
            kuolan_maara = int(input("Kuinka paljon puudeli kuolaa? "))
            pehmeys = int(input("Kuinka pehmeä puudeli on asteikolla 1-10? "))
        except ValueError:
            print("Virheellinen syöte! Kuolan määrän ja pehmeyden tulee olla numero.")
            return
        lemmikki = lemmikit.Puudeli(nimi, lempiruoka, syntymavuosi, kuolan_maara, pehmeys)

    elif valinta == "4":
        try:
            karvan_maara = int(input("Kuinka paljon kissalla on karvaa? "))
            kynsien_teravyys = int(input("Kuinka terävät kynnet ovat asteikolla 1-10? "))
        except ValueError:
            print("Virheellinen syöte! Karvan määrän ja kynsien terävyyden tulee olla numero.")
            return
        lemmikki = lemmikit.Kissa(nimi, lempiruoka, syntymavuosi, karvan_maara, kynsien_teravyys)

    elif valinta == "5":
        vari = input("Mikä on papukaijan väri? ").strip()
        lemmikki = lemmikit.Papukaija(nimi, lempiruoka, syntymavuosi, vari)

    else:
        print("Virheellinen valinta. Valitse numero 1-5.")
        return

    lemmikit_lista.append(lemmikki)
    print(f"{lemmikki.nimi} on luotu!")
def listaa_lemmikit():
    if not lemmikit_lista:
        print("\nEi lemmikkejä luotuna.")
        return
    
    for i, lemmikki in enumerate(lemmikit_lista):
        tiedot = f"{i + 1}. {lemmikki.__class__.__name__}, Nimi: {lemmikki.nimi},  Lempiruoka: {lemmikki.lempiruoka}, Syntymävuosi: {lemmikki.syntymavuosi}"
        
        if isinstance(lemmikki, lemmikit.Koira):  
            tiedot += f", Kuolan määrä: {lemmikki.kuolan_maara}"
        elif isinstance(lemmikki, lemmikit.Kissa):
            tiedot += f", Karvan määrä: {lemmikki.karvan_maara}, Kynsien terävyys: {lemmikki.kynsien_teravyys}"
        elif isinstance(lemmikki, lemmikit.Papukaija):
            tiedot += f", Väri: {lemmikki.vari}"
        elif isinstance(lemmikki, lemmikit.Puudeli):
            tiedot += f", Pehmeys: {lemmikki.pehmeys}"

        print(tiedot)

def valitse_lemmikki():
    listaa_lemmikit()
    valinta = int(input("Valitse lemmikin numero: ")) - 1
    if valinta < 0 or valinta >= len(lemmikit_lista):
        print("Virheellinen valinta.")
        return
    lemmikki = lemmikit_lista[valinta]

    if isinstance(lemmikki, lemmikit.Chihuahua):  
      lemmikki.hauku()
      lemmikki.tarise()  
    elif isinstance(lemmikki, lemmikit.Koira):  
      lemmikki.hauku()
    elif isinstance(lemmikki, lemmikit.Papukaija):  
       lemmikki.puhu()
    elif isinstance(lemmikki, lemmikit.Kissa):  
      lemmikki.kehraa()



    


while True:
  try:
           valinta = input("\nValitse toiminto (L)uo lemmikki, (N)äyttää listan, (V)alitse lemmikki. (Ctrl C): ").strip().lower()

           if valinta == "l":
              luo_lemmikki()
           elif valinta == "n":
             listaa_lemmikit()
           elif valinta == "v":
             valitse_lemmikki()

           else:
            print("Virheellinen valinta.")

  except KeyboardInterrupt:
      print("\n Poistutaan, moikka!")
      sys.exit()
