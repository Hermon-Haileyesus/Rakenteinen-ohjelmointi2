class Känny:
    def __init__(self, merkki: str, malli: str, vuosi: int, akku: int = 100):
        self.merkki = merkki
        self.malli = malli
        self.vuosi = vuosi
        self.akku = akku

    def someta(self):
        if self.akku > 0:
            self.akku = max(self.akku - 10, 0)
            return True
        return False

    def tubeta(self):
        
        if self.akku > 0:
            self.akku = max(self.akku - 20, 0)
            return True
        return False

    def lataa(self):
        if self.akku < 100:
            self.akku = min(self.akku + 30, 100)
            return True
        return False

    def __str__(self):
        return f"Känny: {self.merkki} {self.malli} ({self.vuosi}), Akku: {self.akku}%"

känny = Känny("Apple", "iPhone 13", 2021)
print(känny)

känny.someta()
print(f"Akku someilun jälkeen: {känny.akku}%")

känny.tubeta()
print(f"Akku tubettamisen jälkeen: {känny.akku}%")

känny.lataa()
print(f"Akku lataamisen jälkeen: {känny.akku}%")

class Tiev24N:
    def __init__(self, tunti: str, tila: int, opettaja: str):
        self.tunti = tunti
        self.tila = tila  
        self.opettaja = opettaja  

    def onko_opettaja(self, ope: bool):
         
        if ope:
            print(f"Tänään {self.opettaja} on paikalla ")
        else:
            print(f"Tänään {self.opettaja} ei ole paikalla ")


    def täytä(self, opiskelijän_määrä: int):
    
        if opiskelijän_määrä<= self.tila:
            print(f"Luokassa oleva tietokoneen määrä on riittävä {opiskelijän_määrä} opiskelijälle .")
        else:
            print(f"Liian paljon opiskelijöitä! {self.tila} tietokonetta määrä ei riitä  {opiskelijän_määrä} opiskelijälle .")

    def __str__(self):
        return f"Juhannuskukkulassa Tiev24N maanatain tunti: {self.tunti}, Tietokoneen määrä luokassa: {self.tila}, opettajan nimi: {self.opettaja}"


opinto = Tiev24N("Rakenteinen_ohjelmointi", 20, "Waaramäki")
print(opinto)

opinto.onko_opettaja(False)
opinto.täytä(25)
