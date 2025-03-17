nappulat = [
    ["t", "n", "b", "q", "k", "b", "n", "t"], 
    ["p", "p", "p", "p", "p", "p", "p", "p"], 
    [".", ".", ".", ".", ".", ".", ".", "."],  
    [".", ".", ".", ".", ".", ".", ".", "."],  
    [".", ".", ".", ".", ".", ".", ".", "."],  
    [".", ".", ".", ".", ".", ".", ".", "."],  
    ["P", "P", "P", "P", "P", "P", "P", "P"],  
    ["T", "N", "B", "Q", "K", "B", "N", "T"],  
]
for nappula in nappulat:
 print("".join(nappula))
print()
def etsi_nappula(vastaus):
    sijainnit = []
    for rivi_indeksi, rivi in enumerate(nappulat):
        for sarake_indeksi, ruutu in enumerate(rivi ):
            if ruutu == vastaus:
                sijainti = chr(sarake_indeksi + ord("a")) + str(8 - rivi_indeksi)
                sijainnit.append(sijainti)
    return sijainnit
while True:
  vastaus = input("> Mitä nappulaa haluat etsiä: ").strip()
  if vastaus not in "kqbntrpKQBNTRP":
     print(f"{vastaus} ei ole nappula")
     continue
  
  sijannit = etsi_nappula(vastaus)
  if sijannit:
     print(f"{','.join(sijannit)}")
  else:
     print(f"{vastaus} ei löytynyt")
  print()
