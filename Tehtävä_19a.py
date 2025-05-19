class Leffa:
    def __init__(self, nimi: str, ohjaaja: str, pituus: int, vuosi: int, lajityyppi: str, formaatti: str = "VHS", katsottu: bool = False):
        self.nimi = nimi
        self.ohjaaja = ohjaaja
        self.pituus = pituus
        self.vuosi = vuosi
        self.lajityyppi = lajityyppi
        self.formaatti = formaatti
        self.katsottu = katsottu

    def __str__(self):
        return f"{self.nimi} ({self.vuosi}), ohjaaja: {self.ohjaaja}, pituus: {self.pituus} min, lajityyppi: {self.lajityyppi}, formaatti: {self.formaatti}, katsottu: {'Kyllä' if self.katsottu else 'Ei'}"


leffa1 = Leffa("Inception", "Christopher Nolan", 148, 2010, "Sci-Fi")
print(leffa1)
class Kahvikuppi:
    def __init__(self, materiaali: str, tilavuus: int, väri: str, onko_täynnä: bool, lämpötila: float):
        self.materiaali = materiaali  
        self.tilavuus = tilavuus  
        self.väri = väri  
        self.onko_täynnä = onko_täynnä  
        self.lämpötila = lämpötila  

    def __str__(self):
        return f"Kahvikuppi ({self.materiaali}, {self.väri}), tilavuus: {self.tilavuus} ml, lämpötila: {self.lämpötila}°C, {'täynnä' if self.onko_täynnä else 'ei täynnä'}"





kahvikuppi = Kahvikuppi("Posliini", 250, "Valkoinen", True, 75.0)

print(kahvikuppi)

