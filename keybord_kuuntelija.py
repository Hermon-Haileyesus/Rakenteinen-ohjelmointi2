from pynput import keyboard

def käsittele_näppäin(näppäin):
    print(f"Näppäin painettu: {näppäin}")
    if näppäin == keyboard.Key.esc:  # Stop listener when ESC is pressed
        return False

# Listener runs inside the `with` block and waits for input
with keyboard.Listener(on_press=käsittele_näppäin) as kuuntelija:
    kuuntelija.join()

print("Ohjelma päättyi!")  # This line runs ONLY after listener stops


"""import threading
from pynput import keyboard
import time

stop_event = threading.Event()

def käsittele_näppäin(näppäin):
    print(f"Näppäin painettu: {näppäin}")
    if näppäin == keyboard.Key.esc:
        stop_event.set()  # Set flag to stop loop

# Start listener
kuuntelija = keyboard.Listener(on_press=käsittele_näppäin)
kuuntelija.start()

# Loop until stop flag is set
while not stop_event.is_set():
    print("Tallennetaan lokitiedostoon...")
    time.sleep(5)
print("Ohjelma päättyi!")  # Program exits gracefully"""


""""from pynput import keyboard
import time

def käsittele_näppäin(näppäin):
    global kuuntelija
    print(f"Näppäin painettu: {näppäin}")
    if näppäin == keyboard.Key.esc:  # When ESC is pressed, stop listener
        kuuntelija.stop()
        return False  # Stop the listener cleanly

# Start listener in a separate thread
kuuntelija = keyboard.Listener(on_press=käsittele_näppäin)
kuuntelija.start()

# Run a loop that exits when listener stops
while kuuntelija.is_alive():  # Keep looping while listener is running
    print("Tallennetaan lokitiedostoon...")
    time.sleep(5)

print("Ohjelma päättyi!")  # Program ends after listener stops"""
