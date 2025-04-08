import random
def noppa_peli():
    return random.randint(1,6)
def lotto_peli():
    return random.sample(range(1,41), 7)
def kolikonheitto():
    return random.choice(["kruuna", "klaava"])
def vakioveikkaus(x):
    return [random.choice(["1", "X", "2"]) for _ in range(x)]
def lista_XO(x,n):
     lista = ["X"] * n + ["O"] * (x - n)
     random.shuffle(lista)
     return lista
def luo_ruudukko(x, y, n):
    elementit =  ["X"] * n + ["O"] * (x * y - n)
    random.shuffle(elementit)  
    ruudukko = [elementit[i * x:(i + 1) * x] for i in range(y)]
    return ruudukko
def koordinaatti(ruudukko, x, y):
   if 0 <= y < len(ruudukko) and 0 <= x < len(ruudukko[0]):
       return ruudukko[y][x]
   else:
       return None



    

