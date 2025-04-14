import tehtävä16_moduuli

data =tehtävä16_moduuli.hae_henkilot()

while True:
    valinta = input(" (L)istaa kaikki henkilöt , (S)uodata henkilöt nimen perusteella tai 'quit'='lopetta': ").lower()
    if valinta == "l":
        tehtävä16_moduuli.listaa_kaikki(data)
    elif valinta == "s":
        syote = input("Anna merkkijono: ").lower()
        tehtävä16_moduuli.suodattu_henkilöt(data, syote)
    elif valinta == "quit" or valinta == "lopetta":
        break
    else:
        print("vrihellinen syöte, yritä uudelleen!")