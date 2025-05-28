from pynput import mouse



def käsittele_hiiri_siirto(x, y):
    print(f"Hiiri siirtyi koordinaattiin: ({x}, {y})")

def hiiren_painallus(painike):
    
    print(f"Hiiren painike {painike} painettu")
    
    if painike == mouse.Button.right:  # Stop on right-click
        print("Oikea hiiren painike painettu - lopetetaan ohjelma.")
        return False

def hiiren_vapautus(painike):
    print(f"Hiiren painike {painike} vapautettu")  # Should now show correctly


def käsittele_hiiri_rulla(x, y):
    print(f"Hiiri rullattu ({x}, {y}) suuntaan")

# Käynnistä kuuntelija
hiiren_kuuntelija = mouse.Listener(
    on_move=käsittele_hiiri_siirto,
    on_press=hiiren_painallus,
    on_release=hiiren_vapautus,
    on_scroll=käsittele_hiiri_rulla
)
hiiren_kuuntelija.start()

# Pidä ohjelma käynnissä
hiiren_kuuntelija.join()