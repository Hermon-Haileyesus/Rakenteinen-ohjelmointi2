import random

file = open("nimet.txt", "r")
lines = file.readlines()

while True:
    print()
    response = input("> (s)atunnainen rivi vai (i)käkysely? ").strip().lower()
    print()

    if response == "s":
        length = len(lines)
        rand = random.randint(0, length - 1)
        print(lines[rand].strip())

    elif response == "i":
        print("Tänä vuonna täysi-ikäiset: ")
        for line in lines:
            age = 2025 - int(line.split(" ")[1])
            if age >= 18:
                print(line.strip())