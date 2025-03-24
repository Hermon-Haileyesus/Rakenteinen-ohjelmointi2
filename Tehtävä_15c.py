#ohjelma 1
mark = "Ford"
model = "Escort"
def paikalliset_muuttuja():
    mark = input("> Anna merkki: ").strip()
    model = input("> Anna malli: ").strip()
    print("Paikalliset muuttujat:")
    print(f"mark: {mark}")
    print(f"model: {model}")

paikalliset_muuttuja()
print("Globaalit muuttujat:")
print(f"mark: {mark}")
print(f"model: {model}")

print("ohjelma 2 ") # ohjelma 2

def globaali_muuttuja():
    global mark
    global model
    mark = input("> Anna merkki: ").strip()
    model = input("> Anna malli: ").strip()
globaali_muuttuja()
print("Globaalit muuttujat:")
print(f"mark: {mark}")
print(f"model: {model}")