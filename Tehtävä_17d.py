import sys
def prosessoi_lista(merkkijono):
    try:
        arvot = merkkijono.split(',')
        
        luvut = []
        
        for arvo in arvot:
            arvo = arvo.strip()
            if '.' in arvo:
                raise ValueError("Syöte sisältää desimaalilukuja, vain kokonaisluvut sallittuja.")
            luku = int(arvo)
            if luku < 0:
                raise ValueError("Syöte sisältää negatiivisia lukuja.")
            luvut.append(luku)
        
        luvut.sort()
        return luvut
    except ValueError as e:
        print(f"Virhe: {e}")
        return None
    

def main():
   
    try:
        syote = input("Anna pilkulla eroteltu lista positiivisia kokonaislukuja: ")
        tulos = prosessoi_lista(syote)

        if tulos is not None:
            print(f"Järjestetty lista: {tulos}")
        else:
            print("Syötteessä oli virhe, yritä uudelleen.")
    except KeyboardInterrupt:
        print("\nPoistutaan ohjelmasta.")
        sys.exit()
    
if __name__ == "__main__":
    main()
""""def prosessoi_lista(merkkijono):
    
    try:
        # Muunnetaan merkkijono listaksi
        arvot = merkkijono.split(',')
        
        # Muutetaan arvot kokonaisluvuiksi ja tarkistetaan positiivisuus
        luvut = [int(arvo.strip()) for arvo in arvot if arvo.strip().isdigit()]
        
        if len(luvut) != len(arvot):
            raise ValueError("Kaikki arvot eivät ole positiivisia kokonaislukuja.")

        # Järjestetään luvut suuruusjärjestykseen
        luvut.sort()

        return luvut

    except ValueError as e:
        print(f"Virhe: {e}")
        return None
        
        
        tai
        
        def prosessoi_lista(merkkijono):
   
    try:
        arvot = merkkijono.split(',')
        luvut = []
        virheet = []

        for arvo in arvot:
            arvo = arvo.strip()

            if '.' in arvo:
                virheet.append(f"Desimaaliluku havaittu: {arvo}")
                continue  # Skip further processing for this value

            if arvo.lstrip('-').isdigit():
                luku = int(arvo)
                if luku < 0:
                    virheet.append(f"Negatiivinen luku havaittu: {arvo}")
                else:
                    luvut.append(luku)
            else:
                virheet.append(f"Virheellinen arvo: {arvo}")

        if virheet:
            raise ValueError("Syöte ei kelpaa:\n" + "\n".join(virheet))

        luvut.sort()
        return luvut

    except ValueError as e:
        print(f"Virhe: {e}")
        return None"""
