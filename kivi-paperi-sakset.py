def get_choice(player):
    
    choice = ""
    while choice not in ["kivi", "paperi", "sakset"]:
        choice = input(f"Pelaaja {player}, valitse aseesi (kivi, paperi, sakset): ").strip().lower()
    return choice

def determine_winner(player1, player2):
    if player1 == player2:
        return "Tasapeli!"
    
    winning_combinations = {
        "kivi": "sakset",
        "paperi": "kivi",
        "sakset": "paperi"
    }
    
    return "Pelaaja 1 voitti!" if winning_combinations[player1] == player2 else "Pelaaja 2 voitti!"

while True:
    player1_choice = get_choice(1)
    player2_choice = get_choice(2)

    print(determine_winner(player1_choice, player2_choice))

    again = ""
    while again not in ["k", "e"]:
        again = input("Haluatko pelata uudestaan? (k/e): ").strip().lower()
    
    if again == "e":
        break