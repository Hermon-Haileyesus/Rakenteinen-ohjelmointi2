import Hermon_moduuli
while True:
    valinta = input("pelaako (n)oppaa, (k)olikonheittoa, (l)ottoa, (v)akioveikkausta , (la)ivanupotusta ('quit' ='lopetta'): ").strip().lower()
    if valinta == "n":
        vastaus = int(input("Arvaa luvun väliltä 1 - 6: " ))
        oikea_vastaus = Hermon_moduuli.noppa_peli()
        if vastaus == oikea_vastaus:
            print(f"Noppa näyttää {oikea_vastaus}, arvoit oikein !")
        else:
            print(f"Noppa näyttää {oikea_vastaus}, arvoit väärin !")
    elif valinta == "k":
        vastaus = input("Arvaa (kruuna/klaava): ").strip().lower()
        oikea_vastaus = Hermon_moduuli.kolikonheitto().lower()
        if vastaus == oikea_vastaus:
            print(f"kolikko näyttää {oikea_vastaus}, arvoit oikein !")
        else:
            print(f"kolikko näyttää {oikea_vastaus}, arvoit väärin !")
    elif valinta == "l":
        vastaus = list(map(int, input("Anna 7 numeroa väliltä 1 - 40, eroteltu pilkulla ").split(",")))
        oikea_vastaus = Hermon_moduuli.lotto_peli()
        osumat = set(vastaus) & set(oikea_vastaus)
        if len(osumat) > 0:
            print(f"Arvottu lottorivi:{oikea_vastaus} ja osumien määrä on {len(osumat)}")
        else:
            print(f"Arvottu lottorivi:{oikea_vastaus} ja Valitettavasti et saanut yhtään osumaa!")
    elif valinta == "v":
        maara = int("kuinka monta matsia haluaa arvata: ")
        vastaus = [input(f"Anna tulos {i+1} (1/X/2): ").strip() for i in range(maara)]
        oikea_vastaus = Hermon_moduuli.vakioveikkaus(maara)
        osumat = sum([1 for i in range(maara) if vastaus[i] == oikea_vastaus[i]])
        print(f"Tulosrivi: {oikea_vastaus}")
        print(f"Osumia: {osumat}")
    elif valinta == "la":
        leveys = int(input("Ruudukon leveys: "))
        korkeus = int(input("Ruudukon korkeus: "))
        laivat = int(input("Laivojen määrä: "))
        ruudukko = Hermon_moduuli.luo_ruudukko(leveys, korkeus, laivat)
        
        for _ in range(3):
          x = int(input("Anna x-koordinaatti: "))
          y = int(input("Anna y-koordinaatti: "))
          merkki = Hermon_moduuli.koordinaatti(ruudukko, x, y)
          print("Osui!" if merkki == "X" else "Ei osunut.")
        
        for rivi in ruudukko:
          print(" ".join(rivi))

    elif valinta == "quit":
        break
    else:
        print("Virheellinen valinta!")






    
    

      



    

            
