import requests

def hae_henkilot():
        url_main = "https://fakerapi.it/api/v1/persons"
        response = requests.get(url_main)
        if response.status_code == 200:
            return response.json()["data"]  
        else:
            print(f"Virhe tietojen haussa! Statuskoodi: {response.status_code}")
def listaa_kaikki(data):
    if not data:
        print("Ei ole tietoja listattavaksi!")
    else:
        for henkilo in data:
            print(f"Nimi: {henkilo['firstname']} {henkilo['lastname']}, Sähköposti: {henkilo['email']}")

def suodattu_henkilöt(data, syote):
   suodattu = []
   for henkilo in data:
       if syote in (henkilo["firstname"].lower() + " " + henkilo["lastname"].lower()):
           suodattu.append(henkilo)
   if len(suodattu) > 0:
       for henkilo in suodattu:
           print(f"Nimi: {henkilo['firstname']} {henkilo['lastname']}, Sähköposti: {henkilo['email']}")
   else:
         print(f"Ei löytynyt henkilöitä, joiden nimi sisältää '{syote}'")



