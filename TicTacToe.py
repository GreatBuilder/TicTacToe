import random

# Initialize all spots as empty
spots = {i: ' ' for i in range(1, 10)}

def draw_grid(spots):
    grid = f"""|{spots[1]}|{spots[2]}|{spots[3]}|
|{spots[4]}|{spots[5]}|{spots[6]}|
|{spots[7]}|{spots[8]}|{spots[9]}|"""
    print(grid)

# All winning combinations
winning_combos = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
    [1, 5, 9], [3, 5, 7]              # diagonals
]

def find_two_in_a_row(spots, symbol):
    for combo in winning_combos:
        values = [spots[i] for i in combo]
        if values.count(symbol) == 2 and values.count(' ') == 1:
            return combo[values.index(' ')]
    return None

def check_winner(spots, symbol):
    for combo in winning_combos:
        if all(spots[i] == symbol for i in combo):
            return True
    return False

# Start game
game_over = False
turn_count = 0

draw_grid(spots)

while not game_over:
    turn_count += 1

    if turn_count % 2 == 1:
        # Player's turn
        try:
            player_input = int(input("Select a number (1-9) to place your X: "))
            while player_input not in range(1, 10) or spots[player_input] != ' ':
                player_input = int(input("Invalid or taken! Choose another (1-9): "))
        except ValueError:
            print("Enter a valid number.")
            continue
        spots[player_input] = "X"
    else:
        # Computer's turn
        move = find_two_in_a_row(spots, 'O')  # Try to win
        if move is None:
            move = find_two_in_a_row(spots, 'X')  # Try to block
        if move is None:
            empty_spots = [i for i, v in spots.items() if v == ' ']
            move = random.choice(empty_spots)
        print(f"Computer chooses spot {move}")
        spots[move] = "O"

    draw_grid(spots)

    # Check winner
    if check_winner(spots, 'X'):
        print("You win!")
        game_over = True
    elif check_winner(spots, 'O'):
        print("Computer wins!")
        game_over = True
    elif turn_count == 9:
        print("It's a tie!")
        game_over = True
