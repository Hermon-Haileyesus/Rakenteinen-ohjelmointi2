import requests

def hae_henkilotiedot(maara):
    try:
      
        url = f"https://fakerapi.it/api/v1/persons?_quantity={maara}"
        response = requests.get(url)
        
        response.raise_for_status()
        data = response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Virhe: {e}")
        return None
    else:
        return data["data"]
    finally:
        print("Tiedonhaku suoritettu.")

def tallenta_palaute():
    palaute = input("Anna palautetta ohjelmasta: ")
    try:
        with open("palaute.txt", "a", encoding="utf-8") as file:
            file.write(palaute + "\n")
    except Exception as e:
        print(f"Virhe palautteen tallentamisessa: {e}")
    finally:
        print("Kiitos palautteesta!")

def main():
        try:
            syote = input("Syötä henkilöiden lukumäärä (1-50): ").strip()
            
            if not syote:
                raise ValueError("Syöte ei voi olla tyhjä!")
            
            maara = int(syote)
            
            if not 1 <= maara <= 50:
                raise ValueError("Syötteen tulee olla välillä 1 - 50!")
            
            henkilo_tieto = hae_henkilotiedot(maara)
            
            
        except ValueError as e:
            print(f"Virhe: {e}")
        else:
            if henkilo_tieto:
                print("\nHaetut henkilöt:")
                for henkilo in henkilo_tieto:
                    print(f"{henkilo['firstname']} {henkilo['lastname']}, sähköposti: {henkilo['email']}")
        finally:
             tallenta_palaute()

if __name__ == "__main__":
    main()