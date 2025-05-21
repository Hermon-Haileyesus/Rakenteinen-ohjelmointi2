import tkinter as tk
from tkinter import messagebox
import lemmikit
import datetime
import datetime

import datetime

def validate_year():
    """Validates the pet's birth year and prevents infinite looping."""
    current_year = datetime.datetime.now().year
    syntymavuosi = vuosi_entry.get().strip()

    if not syntymavuosi.isdigit():
        messagebox.showerror("Virhe", "Syötä vain numeroita!")
        vuosi_entry.delete(0, tk.END)  # Clear wrong input
        return None  # Return None instead of looping

    syntymavuosi = int(syntymavuosi)

    if 1900 <= syntymavuosi <= current_year:
        return syntymavuosi  # Success!
    else:
        messagebox.showerror("Virhe", f"Syntymävuosi pitää olla välillä 1900-{current_year}.")
        vuosi_entry.delete(0, tk.END)
        return None

lemmikit_lista = []

def luo_lemmikki():
    tyyppi = tyyppi_var.get()
    nimi = nimi_entry.get()
    lempiruoka = ruoka_entry.get()
    syntymavuosi = validate_year()
    if not nimi or not lempiruoka or syntymavuosi is None:
        return


    try:
        if tyyppi == "Koira":
            kuolan_maara = int(extra_entry.get())
            lemmikki = lemmikit.Koira(nimi, lempiruoka, syntymavuosi, kuolan_maara)
        elif tyyppi == "Chihuahua":
            kuolan_maara = int(extra_entry.get())
            lemmikki = lemmikit.Chihuahua(nimi, lempiruoka, syntymavuosi, kuolan_maara)
        elif tyyppi == "Puudeli":
            kuolan_maara = int(extra_entry.get())
            pehmeys = int(extra_entry2.get())
            lemmikki = lemmikit.Puudeli(nimi, lempiruoka, syntymavuosi, kuolan_maara, pehmeys)
        elif tyyppi == "Kissa":
            karvan_maara = int(extra_entry.get())
            kynsien_teravyys = int(extra_entry2.get())
            lemmikki = lemmikit.Kissa(nimi, lempiruoka, syntymavuosi, karvan_maara, kynsien_teravyys)
        elif tyyppi == "Papukaija":
            vari = extra_entry.get()
            lemmikki = lemmikit.Papukaija(nimi, lempiruoka, syntymavuosi, vari)
        else:
            messagebox.showerror("Virhe", "Tuntematon eläinlaji.")
            return

        lemmikit_lista.append(lemmikki)
        messagebox.showinfo("Onnistui", f"Lemmikki {nimi} luotu onnistuneesti!")
        nimi_entry.delete(0, tk.END)
        ruoka_entry.delete(0, tk.END)
        vuosi_entry.delete(0, tk.END)
        extra_entry.delete(0, tk.END)
        extra_entry2.delete(0, tk.END)


    except ValueError:
        messagebox.showerror("Virhe", "Syötä kelvolliset arvot!")

def listaa_lemmikit():
    if not lemmikit_lista:
        messagebox.showinfo("Lemmikit", "Ei lemmikkejä tallennettuna.")
        return

    tiedot_lista = []
    
    for i, lemmikki in enumerate(lemmikit_lista):
        tiedot = f"{i + 1}. {lemmikki.__class__.__name__}, Nimi: {lemmikki.nimi},  Lempiruoka: {lemmikki.lempiruoka}, Syntymävuosi: {lemmikki.syntymavuosi}"
        
        if isinstance(lemmikki, lemmikit.Koira):
            tiedot += f", Kuolan määrä: {lemmikki.kuolan_maara}"
        elif isinstance(lemmikki, lemmikit.Kissa):
            tiedot += f", Karvan määrä: {lemmikki.karvan_maara}, Kynsien terävyys: {lemmikki.kynsien_teravyys}"
        elif isinstance(lemmikki, lemmikit.Papukaija):
            tiedot += f", Väri: {lemmikki.vari}"
        elif isinstance(lemmikki, lemmikit.Puudeli):
            tiedot += f", Pehmeys: {lemmikki.pehmeys}"

        tiedot_lista.append(tiedot)

    messagebox.showinfo("Lemmikit", "\n".join(tiedot_lista))
    



def suorita_toiminto():
    valittu_nimi = valinta_entry.get().strip()
    if not valittu_nimi:
        messagebox.showerror("Virhe", "Valitse ensin lemmikki!")
        return


    lemmikki = next((l for l in lemmikit_lista if l.nimi == valittu_nimi), None)
    if not lemmikki:
        messagebox.showerror("Virhe", "Lemmikkiä ei löytynyt.")
        return

    # Debugging - Print class type
    #print(f"Lemmikin tyyppi: {lemmikki.__class__.__name__}")

    toiminto = ""
    if isinstance(lemmikki, lemmikit.Koira):
        toiminto = lemmikki.hauku()
    elif isinstance(lemmikki, lemmikit.Kissa):
        toiminto = lemmikki.kehraa()
    elif isinstance(lemmikki, lemmikit.Papukaija):
        toiminto = lemmikki.puhu()

    if toiminto:
        messagebox.showinfo("Toiminto", toiminto)
    else:
        messagebox.showerror("Virhe", "Ei toimintoa saatavilla.")
    valinta_entry.delete(0, tk.END)

# **Tkinter UI Setup**
root = tk.Tk()
root.title("Lemmikkien hallinta")

# **Perustiedot**
tk.Label(root, text="Lemmikin nimi").grid(row=0, column=0)
nimi_entry = tk.Entry(root)
nimi_entry.grid(row=0, column=1)

tk.Label(root, text="Lempiruoka").grid(row=1, column=0)
ruoka_entry = tk.Entry(root)
ruoka_entry.grid(row=1, column=1)

tk.Label(root, text="Syntymävuosi").grid(row=2, column=0)
vuosi_entry = tk.Entry(root)
vuosi_entry.grid(row=2, column=1)

# **Lemmikin tyyppi**
tk.Label(root, text="Lemmikin tyyppi").grid(row=3, column=0)
tyyppi_var = tk.StringVar(root)
tyyppi_var.set("Koira")
tyyppi_menu = tk.OptionMenu(root, tyyppi_var, "Koira", "Chihuahua", "Puudeli", "Kissa", "Papukaija")
tyyppi_menu.grid(row=3, column=1)

# **Extra fields (conditionally shown)**
extra_label = tk.Label(root, text="Lisätieto")
extra_entry = tk.Entry(root)

extra_label2 = tk.Label(root, text="Toinen lisätieto")
extra_entry2 = tk.Entry(root)

# **Function to dynamically show fields**
def update_extra_fields(*args):
    tyyppi = tyyppi_var.get()
    
    extra_label.grid_remove()
    extra_entry.grid_remove()
    extra_label2.grid_remove()
    extra_entry2.grid_remove()
    
    if tyyppi in ["Koira","Chihuahua", "Puudeli", "Kissa", "Papukaija"]:
        extra_label.grid(row=4, column=0)
        extra_entry.grid(row=4, column=1)
    if tyyppi in ["Puudeli", "Kissa"]:
        extra_label2.grid(row=5, column=0)
        extra_entry2.grid(row=5, column=1)

tyyppi_var.trace("w", update_extra_fields)

# **Buttons**
tk.Button(root, text="Luo lemmikki", command=luo_lemmikki).grid(row=6, column=0, columnspan=2)
tk.Button(root, text="Listaa lemmikit", command=listaa_lemmikit).grid(row=7, column=0, columnspan=2)

tk.Label(root, text="Valitse lemmikin nimi").grid(row=8, column=0)
valinta_entry = tk.Entry(root)
valinta_entry.grid(row=8, column=1)

tk.Button(root, text="Suorita toiminto", command=suorita_toiminto).grid(row=9, column=0, columnspan=2)

# **Run Tkinter main loop**
root.mainloop()