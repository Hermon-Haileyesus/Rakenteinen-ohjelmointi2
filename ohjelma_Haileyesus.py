import moduuli_Haileyesus
while True:
    valinta = input("(L)istata, (k)atsella yhden henkilön tieto, (U)usi-henkilo lisätään tai (P)oistaa: ").lower().strip()
    if valinta == "l":
        moduuli_Haileyesus.kaikki_henkilot()
    elif valinta == "k":
        id_numero = int(input("Syötä ID: "))
        henkilo = moduuli_Haileyesus.hae_henkilon(id_numero)
        if henkilo :
            print(henkilo)
        else:
            print("Henkilöä ei löydy!")
    elif valinta == "u":
        id_numero = int(input("Syötä ID: "))
        etunimi = input("Syötä etunimi: ")
        sukunimi = input("Syötä sukunimi: ")
        ika = int(input("Syötä ikä: "))
        toteemi = input("Syötä toteemieläin: ")
        uusi_henkilo = {
                "id": id_numero,
                "first-name": etunimi,
                "last-name": sukunimi,
                "age": ika,
                "totem-animal": toteemi
            }
        moduuli_Haileyesus.lisaa_listaan(uusi_henkilo)
        print("henkilo on lisätty!")

    elif valinta == "p":
        id = int(input("Syötä ID, joka haluasit posista: "))
        if moduuli_Haileyesus.poista_listasta(id):
            print("Henkilön on poistettu!")
        else:
            print("Henkilöä ei löydy!")
    else:
        print("Virhellinen valinta, yritä uudelleen!")

