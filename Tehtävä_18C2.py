from pynput import keyboard
import os


koko = 5
x, y = koko // 2, koko // 2 

def piirrä_ruudukko():
    os.system("cls") 
    for i in range(koko):
        for j in range(koko):
            if i == y and j == x:
                print("O", end="")
            else:
                print(".", end="")
        print() 

def käsittele_näppäin(näppäin):
    global x, y
    if näppäin == keyboard.Key.esc:  
        print("ESC painettu - ohjelma päättyy.")
        return False  

    if näppäin == keyboard.Key.up and y > 0:
        y -= 1
    elif näppäin == keyboard.Key.down and y < koko - 1:
        y += 1
    elif näppäin == keyboard.Key.left and x > 0:
        x -= 1
    elif näppäin == keyboard.Key.right and x < koko - 1:
        x += 1

    piirrä_ruudukko()  

piirrä_ruudukko()


with keyboard.Listener(on_press=käsittele_näppäin) as kuuntelija:
    kuuntelija.join()