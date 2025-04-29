import sys
numerot = []
while True:
    try:
       luku = (input("Anna luku: "))
       if not luku:
          raise ValueError("Syöte ei voi olla tyhjä!")
    
       luku = float(luku)
       numerot.append(luku)
       print(f"Suurin luku: {max(numerot)}")
       print(f"Pienin luku: {min(numerot)}")
       print(f"Lukujen keskiarvo: {sum(numerot) / len(numerot):.2f}")
    except ValueError as e:
        print(f"Virheellinen syöte, {e}")
    except KeyboardInterrupt:
           print('\nPoistutaan ...')
           sys.exit()
    
    