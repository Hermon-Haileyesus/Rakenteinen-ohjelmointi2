class Elain:
    def __init__(self, nimi, lempiruoka, syntymavuosi):
        self.nimi = nimi
        self.lempiruoka = lempiruoka
        self.syntymavuosi = syntymavuosi

    def kakkaa(self):
        return "Hyi yäk"


class Koira(Elain):
    def __init__(self, nimi, lempiruoka, syntymavuosi, kuolan_maara):
        super().__init__(nimi, lempiruoka, syntymavuosi)
        self.kuolan_maara = kuolan_maara

    def hauku(self):
        return "Hau"


class Chihuahua(Koira):
    def hauku(self):
        return "Väyväyväyväyväy"

    def tarise(self):
        return "täritäri"


class Puudeli(Koira):
    def __init__(self, nimi, lempiruoka, syntymavuosi, kuolan_maara, pehmeys):
        super().__init__(nimi, lempiruoka, syntymavuosi, kuolan_maara)
        self.pehmeys = pehmeys


class Kissa(Elain):
    def __init__(self, nimi, lempiruoka, syntymavuosi, karvan_maara, kynsien_teravyys):
        super().__init__(nimi, lempiruoka, syntymavuosi)
        self.karvan_maara = karvan_maara
        self.kynsien_teravyys = kynsien_teravyys

    def kehraa(self):
        return "Purr"


class Papukaija(Elain):
    def __init__(self, nimi, lempiruoka, syntymavuosi, vari):
        super().__init__(nimi, lempiruoka, syntymavuosi)
        self.vari = vari

    def puhu(self):
        return "Polli tahtoo keksin"

    def lenna(self):
        return "Flap flap"