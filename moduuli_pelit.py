import random

def arvo_noppa():
    return random.randint(1, 6)

def arvo_lotto():
    return random.sample(range(1, 41), 7)

def kolikon_heitto():
    return random.choice(["kruuna", "klaava"])

def vakioveikkaus_rivi(x):
    return [random.choice(["1", "X", "2"]) for _ in range(x)]

def tulo_rivi(x, n):
    rivi = ["X"] * n + ["O"] * (x - n)
    random.shuffle(rivi)
    return rivi

def laivanupotus_ruudukko(x, y, n):
    ruudukko = [["O" for _ in range(x)] for _ in range(y)]
    laivat = random.sample(range(x * y), n)
    for paikka in laivat:
        ruudukko[paikka // x][paikka % x] = "X"
    return ruudukko

def koordinaattiarvo(ruudukko, x, y):
    return ruudukko[y][x]