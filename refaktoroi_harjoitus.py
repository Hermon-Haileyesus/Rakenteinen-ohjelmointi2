import random

def print_board(board):
    for row in board:
        print("".join(row))
    print()

def check_winner(board):
    
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]

    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '.':
            return board[0][col]

    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        return board[0][2]

    return None 

def check_draw(board):
    return all(cell != '.' for row in board for cell in row)


board = [['.','.','.'],
         ['.','.','.'],
         ['.','.','.']]

print_board(board)

game_over = False

while not game_over:
    
    empty_cell = False
    while not empty_cell:
        try:
            coords = input("Anna kaksi koordinaattia 0-2 pilkulla eroteltuna: ")
            
            if coords.lower() == 'q':  
                 print("Peli lopetettu.")
                 game_over = True
                 exit()  


            user_x, user_y = coords.split(',')
            user_x = int(user_x)
            user_y = int(user_y)
        
            if 0 <= user_x <= 2 and 0 <= user_y <= 2: 
              if board[user_y][user_x] == '.':
                board[user_y][user_x] = 'X'
                empty_cell = True
              else:
                print("Valittu ruutu on jo käytössä. Yritä uudelleen.")
            else:
              print("Koordinaattien tulee olla välillä 0-2. Yritä uudelleen.")
        except ValueError:
            print("Virheellinen syöte! Anna kaksi numeroa pilkulla eroteltuna.")
    

    print_board(board)
    
    winner = check_winner(board)
    if winner:
        print(f"{winner} voitti pelin!")
        game_over = True
        break

    if check_draw(board):
        print("Tasapeli!")
        break

    
    empty_cell = False
    while not empty_cell:
        bot_x = random.randint(0, 2)
        bot_y = random.randint(0, 2)
        if board[bot_y][bot_x] == '.':
            board[bot_y][bot_x] = 'O'
            empty_cell = True
    
    print_board(board)
    
    winner = check_winner(board)
    if winner:
        print(f"{winner} voitti pelin!")
        game_over = True
        break

    if check_draw(board):
        print("Tasapeli!")
        break