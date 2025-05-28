import json
from pynput import keyboard
import threading
import os

TIEDOSTO_NIMI = "ruokalista.txt"
PAIVAT = ["ma", "ti", "ke", "to", "pe"]

def lataa_ruokalista():
    try:
        with open(TIEDOSTO_NIMI, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def tallenna_ruokalista(ruokalista):
    with open(TIEDOSTO_NIMI, "w", encoding="utf-8") as file:
        json.dump(ruokalista, file, indent=4, ensure_ascii=False)

def lisää_ruoka(päivä, ruoka1, ruoka2, juoma, jälkkäri,ruokalista): 
    if päivä in ["ma", "ti", "ke", "to", "pe"]:
        if päivä in ruokalista:
            vastaus = input(f"{päivä.capitalize()} on jo olemassa. Haluatko muokata sitä? (k/e): ").lower()
            if vastaus != "k":
                print("Ei muutoksia tehty.")
                return
        else:
            ruokalista[päivä] = {}  # Luo päivän vain, jos sitä ei vielä ole

        # Päivitä vain annettuja arvoja, säilyttäen vanhat tiedot jos niitä ei muuteta
        ruokalista[päivä]["ruoka1"] = ruoka1 or ruokalista[päivä].get("ruoka1", "")
        ruokalista[päivä]["ruoka2"] = ruoka2 or ruokalista[päivä].get("ruoka2", "")
        ruokalista[päivä]["juoma"] = juoma or ruokalista[päivä].get("juoma", "")
        ruokalista[päivä]["jälkkäri"] = jälkkäri or ruokalista[päivä].get("jälkkäri", "")

        tallenna_ruokalista(ruokalista)
        print(f"Ruokalista päivälle {päivä} päivitetty!")
    else:
        print("Virheellinen päivä.")


def print_ruokalista(ruokalista, päivä=None):
    if päivä:
        lista = ruokalista.get(päivä)
        if lista:
            print(f"{päivä}:")
            for ruoka, arvo in lista.items():
                print(f"{ruoka}: {arvo}")
            print()
        else:
            print(f"Päivää {päivä} ei löydy.")
    else:
        for päivä, lista in ruokalista.items():
            print_ruokalista(ruokalista, päivä)
def esc_listener():
    """Background thread to detect ESC key press."""
    def on_press(key):
        if key == keyboard.Key.esc:
            print("\nESC key pressed! Exiting program...")
            os._exit(0)


    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    threading.Thread(target=esc_listener, daemon=True).start()

    ruokalista = lataa_ruokalista()

    while True:
        toiminto = input("(l)isää ruoka vai (h)ae ruokat ja paina (Esc) lopetaan ohjelma: ").strip().lower()

        if toiminto == "l":
            päivä = input("Anna päivä (ma, ti, ke, to, pe): ").strip().lower()
            if päivä in PAIVAT:
                ruoka1 = input("Anna ruoka 1: ")
                ruoka2 = input("Anna ruoka 2: ")
                juoma = input("Anna juoma: ")
                jälkkäri = input("Anna jälkkäri: ")
                lisää_ruoka(päivä, ruoka1, ruoka2, juoma, jälkkäri, ruokalista)
        
        elif toiminto == "h":
            valinta = input("Minkä päivän ruokalista (ma, ti, ke, to, pe, viikko): ").strip().lower()
            if valinta in PAIVAT:
                print_ruokalista(ruokalista, valinta)
            elif valinta == "viikko":
                print_ruokalista(ruokalista)

if __name__ == "__main__":
    main()