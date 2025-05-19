class Tuote:
    def __init__(self, tuote_id: int, hinta: float, varasto: int, nimi: str):
        self.tuote_id = tuote_id
        self.hinta = hinta
        self.varasto = varasto
        self.nimi = nimi

    def osta(self, määrä: int):
        
        if määrä > self.varasto:
            print(f"Ei tarpeeksi varastossa! Vain {self.varasto} jäljellä.")
            return None
        self.varasto -= määrä
        return self.varasto,  määrä * self.hinta

    def tilaa(self, määrä: int):
        
        self.varasto += määrä
        return self.varasto

    def __str__(self):
        return f"Tuote: {self.nimi}, ID: {self.tuote_id}, Hinta: {self.hinta}€, Varasto: {self.varasto} kpl"

class Vaate(Tuote):
    def __init__(self, tuote_id: int, hinta: float, varasto: int, nimi: str, tyyppi: str, väri: str, merkki: str, koko: str):
        super().__init__(tuote_id, hinta, varasto, nimi)
        self.tyyppi = tyyppi
        self.väri = väri
        self.merkki = merkki
        self.koko = koko

    def __str__(self):
        return f"Vaate: {self.merkki} {self.tyyppi}, Väri: {self.väri}, Koko: {self.koko}, Hinta: {self.hinta}€, Varasto: {self.varasto} kpl"
class Juoma(Tuote):
    def __init__(self, tuote_id: int, hinta: float, varasto: int, nimi: str, koko: int, valmistaja: str, prosentti: int):
        super().__init__(tuote_id, hinta, varasto, nimi)
        self.koko = koko  
        self.valmistaja = valmistaja
        self.prosentti = prosentti  

    def __str__(self):
        return f"Juoma: {self.nimi} ({self.koko}ml), Valmistaja: {self.valmistaja}, {self.prosentti}%, Hinta: {self.hinta}€, Varasto: {self.varasto} kpl"
    
paita = Vaate(101, 29.90, 50, "T-paita", "T-paita", "Sininen", "Nike", "M")
print(paita)
uusi_varasto, hinta = paita.osta(2)
print(f"Kokonaishinta: {hinta}€ ja Varastossa jäljelee paita määrä: {uusi_varasto} kpl")
print("Uusi varasto:", paita.tilaa(10))
mehu = Juoma(202, 2.50, 100, "Appelsiinimehu", 500, "Tropicana", 0)
print(mehu)
uusi_varasto, hinta =  mehu.osta(3)
print(f"kokonaishinta: {hinta}€ ja Varastossa jäljelee paita määrä: {uusi_varasto} kpl")
print("Uusi varasto:", mehu.tilaa(20))