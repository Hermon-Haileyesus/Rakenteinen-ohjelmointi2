import moduuli_Hermon
print(f"Vuosi on {moduuli_Hermon.vuosi}")
numero = int(input("Anna numeron: ")) - 1
if 0 < numero <= len(moduuli_Hermon.ruoat):
    print(f"{moduuli_Hermon.ruoat[numero]}")
else:
    print("Virhellinen numero, valitse numeron (1-5)")

sana = input("Anna sana: ")
luku = int(input("Anna numero: "))
tulos = moduuli_Hermon.toista(sana, luku)
print(f"Toiston tulos: {tulos}")
