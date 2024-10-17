def print_board(board):
    print()
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('__|___|__')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('__|___|__')
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print('  |   |  ')
    print()

def print_instructions():
    print("Welcome to Tic-Tac-Toe!")
    print("Players take turns to place their marks (X or O) on the board.")
    print("Enter a number from 1 to 9 to make your move.")
    print("Enter 'q' at any time to quit the game.")
    print("Here's the board layout with positions:")
    print(" 1 | 2 | 3 ")
    print("---------")
    print(" 4 | 5 | 6 ")
    print("---------")
    print(" 7 | 8 | 9 ")
    print()
    print("The winner of the set will be the player who wins the most games out of 10.")

def check_winner(board):
    winning_combinations = [
        (7, 8, 9),
        (4, 5, 6),
        (1, 2, 3),
        (7, 4, 1),
        (8, 5, 2),
        (9, 6, 3),
        (7, 5, 3),
        (9, 5, 1)
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    
    return None

def is_board_full(board):
    return " " not in board[1:]

def play_game():
    board = [" "] * 10
    current_player = "X"

    print_instructions()

    while True:
        print_board(board)
        print(f"Player {current_player}, enter your move (1-9): ")
        
        player_input = input()

        if player_input.lower() == 'q':
            print("Thanks for playing! Goodbye!")
            return None

        try:
            move = int(player_input)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9 or 'q' to quit.")
            continue

        if move < 1 or move > 9 or board[move] != " ":
            print("Invalid move, try again.")
            continue

        board[move] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return winner 

        if is_board_full(board):  
            print_board(board)  
            print("It's a draw!")  
            return None

        current_player = "O" if current_player == "X" else "X"  


def main():
    player1_wins = 0
    player2_wins = 0
    
    for i in range(10):
        print(f"--- Game {i+1} ---")
        winner = play_game()
        if winner == "X":
            player1_wins += 1
        elif winner == "O":
            player2_wins += 1

    print(f"\nPlayer 1 wins: {player1_wins}")
    print(f"Player 2 wins: {player2_wins}")
    
    if player1_wins > player2_wins:
        print("Player 1 wins the set!")
    elif player1_wins < player2_wins:
        print("Player 2 wins the set!")
    else:
        print("The set is a draw!")


if __name__ == "__main__":
    main()