#Ohjelma 1
def sum(ekaluku, toinenluku):
    if ekaluku and toinenluku:
        summa = ekaluku + toinenluku
        return summa
def substract(ekaluku, toinenluku):
    if ekaluku and toinenluku:
        lasku = ekaluku - toinenluku
        return lasku
def multiply(ekaluku, toinenluku):
    if ekaluku and toinenluku:
        tulos = ekaluku * toinenluku
        return tulos
def divide(ekaluku, toinenluku):
    if ekaluku and toinenluku:
        jakolasku = ekaluku / toinenluku
        return jakolasku
while True:
    ekaluku = int(input("> Anna ensimmäinen numero: "))
    toinenluku = int(input("> Anna toinen numero: "))
    valinta = input("> Laske (y)hteen, (v)ähennä, (k)erro vai (j)aa (quit=lopetta):  ").strip().lower()
    if  valinta=="quit":
        break
    elif valinta == "j":
        print(f"{ekaluku} / {toinenluku} = {divide(ekaluku,toinenluku)}")
    elif valinta == "k":
        print(f"{ekaluku} x {toinenluku} = {multiply(ekaluku,toinenluku)}")
    elif valinta== "v":
        print(f"{ekaluku} - {toinenluku} = {substract(ekaluku,toinenluku)}")
    elif valinta == "y":
        print(f"{ekaluku} + {toinenluku} = {sum(ekaluku,toinenluku)}")
    else:
        print("Virhellinen vaninta")
print()
#ohjelma 2
def sana_kasitelu(sanat):
    if len(sanat) >1:
        return ",".join(sanat[:-1]) +" ja " + sanat[-1]
    else:
        return sanat[0]

    
maara =int(input("> Kuinka monta sanaa käsitellään? "))
sanat =[]
for i in range(maara):
    sana = input("> Anna sana: ").strip()
    sanat.append(sana)
print(sana_kasitelu(sanat))

print()
#ohjelma 3
name="Henri" 
age=25
def changename(new_name):
    global name
    if isinstance(new_name, str) and new_name.strip() and not new_name.isdigit():
        name = new_name
        return True
    else:
     return False

def changeage(new_age):
    global age
    if  new_age.isdigit():
        age = new_age
        return True
    else:
       return False
while True:
    print(f"\n{name} on {age}-vuotias.")
    choice = input("Haluatko muuttaa (i)kää vai (n)imeä? ").strip().lower()
    if choice == "i":
        new_age = input("Syötä uusi ikä: ").strip()
        if changeage(new_age):
            print("OK.")
        else:
            print("Iän pitää olla numero!")
    elif choice == "n":
        new_name = input("Syötä uusi nimi: ").strip()
        if changename(new_name):
            print("OK.")
        else:
            print("Nimen pitä olla merkijono!")
    else:
        print("Virhellinen syöte, yritä uudestaan!")



