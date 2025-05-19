from pynput import keyboard

tekstit = {
    '1': "Partridge in a pear tree",
    '2': "Two french hens",
    '3': "Three turtle doves",
    '4': "Four calling birds",
    '5': "FIVE GOLD RINGS",
    '6': "Six geese-a-laying",
    '7': "Seven swans-a-swimming",
    '8': "Eight maids-a-milking",
    '9': "Nine ladies dancing",
    '0': "Joulu on peruttu!"
}

def käsittele_näppäin(näppäin):
    try:
        if näppäin.char in tekstit:
            print(tekstit[näppäin.char])
    except AttributeError:
        if näppäin == keyboard.Key.esc:  
            print("ESC painettu - ohjelma päättyy.")
            return False  
        
with keyboard.Listener(on_press=käsittele_näppäin) as kuuntelija:
    kuuntelija.join()  