file = open("nimet.txt", "r")
lines = file.readlines()

while True:
    print()
    response = input("> (i)käkysely vai (k)irjainkysely ").strip().lower()
    print()

    if response == "i":
        print("Tänä vuonna täysi-ikäiset: ")
        for line in lines:
            age = 2023 - int(line.split(" ")[1])
            if age >= 18:
                print(line.strip())
    
    elif response == "k":
        count = 0
        ageSum = 0
        chars = ""
        char = ""
        while True:
            char = input("> Anna kirjain tai 'hae': ").strip().lower()
            if char == "hae":
                break
            chars += char[0]
        method = input("> Etsitäänkö nimet, joissa on (k)aikki kirjaimet, (j)oku kirjaimista vai (e)i mikään kirjaimista? ").strip().lower()
        print()
        for line in lines:
            words = line.split(" ")
            all = True
            some = False
            none = True
            for c in chars:
                found = c in words[0] or c.upper() in words[0]
                all = all and found
                some = some or found
                none = none and not found
            if (method == 'k' and all) or (method == 'j' and some) or (method == 'e' and none):
                print(words[0] + ":", 2023 - int(words[1]) )
                count += 1
                ageSum += 2023 - int(words[1])
        if count > 0:
            print("Keskimääräinen ikä: ", ageSum / count)
        else:
            print("Nimiä ei löytynyt!")