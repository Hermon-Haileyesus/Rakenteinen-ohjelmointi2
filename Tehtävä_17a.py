
    
numerot = []
while True:
    try:
       luku = (input("Anna luku: "))
       if not luku:
           print("Syöte ei voi olla tyhjä!")
           continue
       luku = float(luku)
       numerot.append(luku)
       print(f"Suurin luku: {max(numerot)}")
       print(f"Pienin luku: {min(numerot)}")
       print(f"Lukujen keskiarvo: {sum(numerot) / len(numerot):.2f}")
    except ValueError:
        print("Virheellinen syöte, yritä uudelleen!")
    
    