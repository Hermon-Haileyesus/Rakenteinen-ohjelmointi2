# Initialize the chessboard
board = [
    ["t", "n", "b", "q", "k", "b", "n", "t"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["T", "N", "B", "Q", "K", "B", "N", "T"],
]

# Function to print the board
def print_board():
    luku = 8
    for row in board:
        print(f"{" ".join(row)} {luku}")
        luku = luku - 1
    print("a b c d e f g h")

# Function to parse moves
def parse_move(move):
    if len(move) == 4:  # Expects moves in algebraic notation, e.g., "e2e4"
        src_col, src_row = ord(move[0]) - ord("a"), 8 - int(move[1]) #The  function converts a character into its Unicode code point (an integer). For example:
        dest_col, dest_row = ord(move[2]) - ord("a"), 8 - int(move[3])
        return (src_row, src_col), (dest_row, dest_col)
    else:
        return None

# Function to check legality of the move (basic implementation)
def is_legal_move(piece, start, end):
    sr, sc = start
    er, ec = end
    if piece.lower() == "p":  # Example for pawns
        return (er == sr - 1) and (ec == sc)  # Simplified logic for single-step forward
    elif piece.lower() in "rnbqk":  # Extend rules for other pieces
        return True  # Placeholder, implement specific rules here
    return False

# Main game loop
def main():
    print_board()
    while True:
        move = input("Enter your move in algebraic notation (e.g., e2e4): ").strip()
        parsed_move = parse_move(move)
        if parsed_move:
            start, end = parsed_move
            piece = board[start[0]][start[1]]
            if piece == ".":
                print("No piece at the starting position.")
                continue
            if is_legal_move(piece, start, end):
                # Perform the move
                board[end[0]][end[1]] = piece
                board[start[0]][start[1]] = "."
                print_board()
                # Check for game end (if king is captured)
                if piece.lower() == "k":
                    print("Game over!")
                    break
            else:
                print("Illegal move.")
        else:
            print("Invalid input. Use algebraic notation.")

main()