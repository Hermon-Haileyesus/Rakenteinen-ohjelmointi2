class Ajoneuvo:
    def __init__(self, merkki: str, nopeus: int):
        self.merkki = merkki
        self.nopeus = nopeus  # km/h

    def kiihdytä(self, määrä: int):
        """Lisää nopeutta."""
        self.nopeus += määrä
        print(f"{self.merkki} kiihdytti, uusi nopeus: {self.nopeus} km/h")

    def hidasta(self, määrä: int):
        """Vähentää nopeutta."""
        self.nopeus = max(self.nopeus - määrä, 0)
        print(f"{self.merkki} hidasti, uusi nopeus: {self.nopeus} km/h")

    def __str__(self):
        return f"Ajoneuvo: {self.merkki}, Nopeus: {self.nopeus} km/h"
class Auto(Ajoneuvo):
    def __init__(self, merkki: str, nopeus: int, polttoaine: str):
        super().__init__(merkki, nopeus)
        self.polttoaine = polttoaine  # Esim. Bensiini, Diesel, Sähkö

    def tankkaa(self):
        """Tankkaa auton."""
        print(f"{self.merkki} tankattu! Polttoaine: {self.polttoaine}")

    def __str__(self):
        return f"Auto: {self.merkki}, Nopeus: {self.nopeus} km/h, Polttoaine: {self.polttoaine}"
class Polkupyörä(Ajoneuvo):
    def __init__(self, merkki: str, nopeus: int, vaihteet: int):
        super().__init__(merkki, nopeus)
        self.vaihteet = vaihteet

    def vaihda_vaihdetta(self, uusi_vaihde: int):
        """Vaihda pyörän vaihdetta."""
        self.vaihteet = uusi_vaihde
        print(f"{self.merkki}: Vaihde vaihdettu, nyt käytössä {self.vaihteet} vaihdetta.")

    def __str__(self):
        return f"Polkupyörä: {self.merkki}, Nopeus: {self.nopeus} km/h, Vaihteet: {self.vaihteet}"

auto1 = Auto("Toyota", 0, "Bensiini")
print(auto1)
auto1.kiihdytä(50)
auto1.tankkaa()
pyörä1 = Polkupyörä("Trek", 0, 21)
print(pyörä1)
pyörä1.vaihda_vaihdetta(7)
pyörä1.kiihdytä(15)


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
class VerkkoKurssi(Tiev24N):
    def __init__(self, tunti: str, tila: int, opettaja: str, alusta: str):
        super().__init__(tunti, tila, opettaja)
        self.alusta = alusta  

    def linkki(self):
        """Palauttaa kurssin osallistumislinkin."""
        print(f"Osallistu kurssille {self.tunti} käyttämällä alustaa {self.alusta}.")

    def __str__(self):
        return f"Verkkokurssi: {self.tunti}, Opettaja: {self.opettaja}, Alusta: {self.alusta}"


class LaboratorioKurssi(Tiev24N):
    def __init__(self, tunti: str, tila: int, opettaja: str, ohjelmat: list):
        super().__init__(tunti, tila, opettaja)
        self.ohjelmat = ohjelmat  

    def käytössä_ohjelmat(self):
        """Näyttää, mitä ohjelmistoja käytetään kurssilla."""
        print(f"Tällä laboratoriokurssilla ({self.tunti}) käytetään seuraavia ohjelmistoja: {', '.join(self.ohjelmat)}")

    def __str__(self):
        return f"Laboratoriokurssi: {self.tunti}, Opettaja: {self.opettaja}, Käytössä olevat ohjelmistot: {', '.join(self.ohjelmat)}"
    


verkko = VerkkoKurssi("Python-ohjelmointi", 30, "Lehtonen", "Moodele")
print(verkko)
verkko.linkki()

labra_kurssi = LaboratorioKurssi("Tietokonearkkitehtuuri", 20, "Waaramäki", ["Python", "VirtualBox", "Linux Terminal"])
print(labra_kurssi)
labra_kurssi.käytössä_ohjelmat()