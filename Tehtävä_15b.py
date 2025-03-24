def tulosta_syote(arg):
    print(arg)
syote = input("> Anna syöte: ").strip()
tulosta_syote(syote)

#ohjelma 2
def tulosta_listasta(i):
    lista = ["Twitter", "Facebook", "Instagram", "Twitch", "TikTok", "Discord", "Snapchat"]
    i = int(i)
    if 0 <i <= len(lista):
      print(lista[i-1])
    else:
       print("some ei löydy!")   

while True:
  syote = input("> Anna numero (quit = lopetta): ")
  if syote.lower( )== "quit":
     break
  else:
   tulosta_listasta(syote)
  
  
#ohjelma 3
def tulosta_kirjain(sana, numero):
   kirjain = sana[int(numero)-1]
   print(f"{numero}:s kirjain: {kirjain}")
  
sana = input(" > Anna sana: "). strip()
numero = input(" > Anna numero: ").strip()
tulosta_kirjain(sana, numero)

#ohjelma 4
def peli(x, y):
   for rivi in range(1, 6):
      for sarake in range(1, 6):
         if rivi == y and sarake == x:
            print("X", end="")
         else:
            print(".", end="")
      print()
while True:
  x = int(input("Anna x-koordinaatti(1 - 5): "))
  y = int(input("Anna y-koordinaatti(1 - 5): "))
  peli(x, y)