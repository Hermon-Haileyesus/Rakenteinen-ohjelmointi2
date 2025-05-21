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
           valinta = input("\nValitse toiminto (L)uo lemmikki, (N)äyttää listan, (V)alitse lemmikki (Ctrl C): ").strip().lower()

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
