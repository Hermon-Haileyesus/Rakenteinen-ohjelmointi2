henkilot = [
     { "id": 0, "first-name": "Darth", "last-name": "Vader", "age": 45, "totem-animal": "ankannokkaeläin"},

     { "id": 1, "first-name": "Harry", "last-name": "Potter", "age": 13, "totem-animal": "hirvi"}
]
def kaikki_henkilot():
    for henkilo in henkilot:
        print(henkilo)
def hae_henkilon(numero):
    for henkilo in henkilot:
        if henkilo["id"] == numero:
            return henkilo
    return None
def lisaa_listaan(henkilo):
     henkilot.append(henkilo)
def poista_listasta(id_numero):
    for henkilo in henkilot:
        if henkilo["id"] == id_numero:
            henkilot.remove(henkilo)
            return True
    return False

