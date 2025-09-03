import random
import time

def check_game_over(board, winning_combos, current_player):
    winner = check_winner(board, winning_combos)
    if winner:
        print(f"Three in a row! The winner is {current_player}")
        return True
    if "_" not in board.values():
        print("It's a draw!")
        return True
    return False

def computer_move(board, winning_combos, computer_mark="O", player_mark="X"):
    for spot in board:
        if board[spot] == "_":
            board[spot] = computer_mark
            if check_winner(board, winning_combos) == computer_mark:
                return spot
            board[spot] = "_"  
    
    for spot in board:
        if board[spot] == "_":
            board[spot] = player_mark
            if check_winner(board, winning_combos) == player_mark:
                board[spot] = "_" 
                return spot
            board[spot] = "_"
    
    empty_spots = [s for s in board if board[s] == "_"]
    return random.choice(empty_spots)

def check_winner(board, winning_combos):
    for combo in winning_combos:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != "_":
            return board[a]
    return None

def print_board(board):
    print()
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])
    print()

def player_versus_player(winning_combos):
    username1 = ""
    username2 = ""
    
    while username1 == "":
        username1 = input("Enter a username to use, player one (atleast 1 character): ")
    while username2 == "":
        username2 = input("Enter a username to use, player two (atleast 1 character): ")

    username1_mark = "X"
    username2_mark = "O"
    current_player = username1

    board = {1: "_", 2: "_", 3: "_", 4: "_", 5: "_", 6: "_", 7: "_", 8: "_", 9: "_",}
    print_board(board)

    while True:
        print(f"{current_player}'s turn")
        spot = ""

        while spot == "":
            try:
                spot = int(input("Please enter where you would like to place your mark (1 - 9): "))
            except ValueError:
                print("Enter a valid number please")
                continue

            if spot not in board:
                print("Invalid spot, please enter a spot between 1 and 9")
                spot = ""
                continue

            if board[spot] == "_":
                board[spot] = username1_mark if current_player == username1 else username2_mark
                print_board(board)
                winner = check_winner(board, winning_combos)
                if check_game_over(board, winning_combos, current_player):
                    return 
                current_player = username2 if current_player == username1 else username1
            else:
                print("That spot is already taken!")
                print()

def player_versus_computer(winning_combos):
    username = ""
    while username == "":
        username = input("Enter a username to use (atleast 1 character): ")
    
    player_mark = "X"
    computer_mark = "O"
    current_player = username
    winner = None

    board = {1: "_", 2: "_", 3: "_", 4: "_", 5: "_", 6: "_", 7: "_", 8: "_", 9: "_",}
    print_board(board)

    while True:

        print(f"{current_player}'s turn: ")
        spot = ""

        if current_player == "Computer":
            spot = computer_move(board, winning_combos, computer_mark, player_mark)
            time.sleep(1)
            board[spot] = computer_mark
            print_board(board)
            winner = check_winner(board, winning_combos)
            if winner:
                print(f"Three in a row! The winner is {current_player}")
                return
            if "_" not in board.values():
                print("It's a draw!")
                return
            current_player = username

        elif current_player == username:
            while spot == "":
                try:
                    spot = int(input("Please enter where you would like to place your mark (1 - 9): "))
                except ValueError:
                    print("Enter a valid number please")
                    continue

                if spot not in board:
                    print("Invalid spot, please enter a spot between 1 and 9")
                    spot = ""
                    continue

                if board[spot] == "_":
                    board[spot] = player_mark if current_player == username else computer_mark
                    print_board(board)
                    winner = check_winner(board, winning_combos)
                    if check_game_over(board, winning_combos, current_player):
                        return
                    current_player = "Computer" if current_player == username else username
                else:
                    print("That spot is already taken!")
                    print()

def main():
    print("Tic Tac Toe")
    print()
    print("Choose to play against a computer (1) or a two-player game(2)")
    print("1. Player vs Computer")
    print("2. Player vs Player")

    winning_combos = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # cols
    [1, 5, 9], [3, 5, 7]              # diagonals
    ]

    while True:
        try:
            choice = int(input("Choose 1 or 2 (choose 0 to quit): "))
        except ValueError:
            print("Please choose a valid option")
            continue
        
        match choice:
            case 1:
                print("You chose option 1")
                print()
                player_versus_computer(winning_combos)
            case 2:
                print("You chose option 2")
                print()
                player_versus_player(winning_combos)
            case 0:
                print("Exiting...")
                print()
                break
            case _:
                print("Invalid choice, please choose 0, 1 or 2")
                print()

if __name__ == "__main__":
    main()