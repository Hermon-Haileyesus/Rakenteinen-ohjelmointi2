import moduuli_pelit

def pelaa_noppa():
    arvaus = int(input("Arvaa nopan luku (1-6): "))
    tulos = moduuli_pelit.arvo_noppa()
    print(f"Noppa heitettiin: {tulos}")
    if arvaus == tulos:
        print("Onneksi olkoon, arvasit oikein!")
    else:
        print("Väärin arvattu. Yritä uudelleen!")

def pelaa_kolikko():
    arvaus = input("Arvaa kolikon tulos (kruuna/klaava): ").lower()
    tulos = moduuli_pelit.kolikon_heitto()
    print(f"Kolikon tulos oli: {tulos}")
    if arvaus == tulos:
        print("Onneksi olkoon, arvasit oikein!")
    else:
        print("Väärin arvattu!")

def pelaa_lotto():
    arvaus = []
    print("Arvaa 7 numeroa välillä 1 ja 40.")
    for i in range(7):
        arvaus.append(int(input(f"Anna {i + 1} numero: ")))
    tulos = moduuli_pelit.arvo_lotto()
    osumat = set(arvaus) & set(tulos)
    print(f"Lottorivi oli: {tulos}")
    print(f"Sait {len(osumat)} osumaa: {osumat}")

def pelaa_vakioveikkaus():
    x = int(input("Kuinka monta peliä haluat arvata? "))
    arvaus = [input(f"Anna tulos pelille {i+1} (1/X/2): ") for i in range(x)]
    tulos = moduuli_pelit.vakioveikkaus_rivi(x)
    osumat = sum(1 for a, t in zip(arvaus, tulos) if a == t)
    print(f"Arvottu rivi oli: {tulos}")
    print(f"Sait {osumat} osumaa!")

def pelaa_laivanupotus():
    x = int(input("Anna ruudukon leveys: "))
    y = int(input("Anna ruudukon korkeus: "))
    n = int(input("Anna laivojen määrä: "))
    ruudukko = moduuli_pelit.laivanupotus_ruudukko(x, y, n)
    for _ in range(3):
        arv_x = int(input("Anna arvattava x-koordinaatti: ")) - 1
        arv_y = int(input("Anna arvattava y-koordinaatti: ")) - 1
        if moduuli_pelit.koordinaattiarvo(ruudukko, arv_x, arv_y) == "X":
            print("Osuma!")
        else:
            print("Huti!")
    print("Ruudukko pelin jälkeen:")
    for rivi in ruudukko:
        print(" ".join(rivi))

def main():
    print("Tervetuloa pelaamaan!")
    print("Valitse peli:")
    print("1: Noppa")
    print("2: Kolikonheitto")
    print("3: Lotto")
    print("4: Vakioveikkaus")
    print("5: Laivanupotus")
    while True:
      valinta = int(input("Anna valintasi (1-5): "))
      if valinta == 1:
        pelaa_noppa()
      elif valinta == 2:
        pelaa_kolikko()
      elif valinta == 3:
        pelaa_lotto()
      elif valinta == 4:
        pelaa_vakioveikkaus()
      elif valinta == 5:
        pelaa_laivanupotus()
      else:
        print("Virheellinen valinta.")
        break

if __name__ == "__main__":
    main()