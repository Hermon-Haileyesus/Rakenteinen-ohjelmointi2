try:
        tiedostonimi = input("Syötä tiedoston nimi: ").strip()
        
        if not tiedostonimi: 
            raise ValueError("Virhe: Tiedoston nimi ei voi olla tyhjä!")
        
        with open(tiedostonimi, "r", encoding="utf-8") as file:
            rivit = file.readlines()

except FileNotFoundError:
        print(f"Virhe: Tiedostoa '{tiedostonimi}' ei löytynyt.")
except ValueError as e:
        print(e)
else:
    if rivit:  
            print(f"Ensimmäinen rivi: {rivit[0].strip()}")
            print(f"Viimeinen rivi: {rivit[-1].strip()}")
    else:
            print("Tiedosto on tyhjä.")

