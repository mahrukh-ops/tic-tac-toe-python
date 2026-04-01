# Tic tac toe
import random

board = [ " " for _ in range(9)]


def print_board():
    print()
    print(board[0] + ":" + board[1] + ":" + board[2])
    print("--+---+--")
    print(board[3] + ":" + board[4] + ":" + board[5])
    print("--+---+--")
    print(board[6] + ":" + board[7] + ":" + board[8])
    print()

def player_move(player):
    while True:  # Keep asking until the player enters a valid move
        try:
            position = int(input(f"Player {player}, choose position (1-9): ")) - 1
            
            # Check if the number is between 0 and 8 (1-9 on screen)
            if position < 0 or position > 8:
                print("Invalid input! Choose a number 1-9.")
                continue  # Ask again
            
            # Check if the cell is empty
            if board[position] == " ":
                board[position] = player
                break  # Move done, exit loop
            else:
                print("Position already taken! Try again.")
                
        except ValueError:
            print("Invalid input! Enter a number 1-9.")

    # AI selects a random empty position
def ai_move():
    empty_positions = [i for i, spot in enumerate(board) if spot == " "]
    position = random.choice(empty_positions)
    board[position] = "O"
    print(f"AI chooses position {position + 1}")
    
def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def game(): 
     current_player = "X"

     for turn in range(9):
        print_board()

        if current_player == "X":
           player_move("X")
        else:
            ai_move()

        if check_winner(current_player):
            print_board()
            if current_player == "X":
                print("congratulations! You win!")
            else:
                print("AI wins! Better Luck next time.")          
            return

        current_player = "O" if current_player == "X" else "X"

     print_board()
     print("It's a draw!")

while True:
    board = [ " " for _ in range(9)]
    game()

    choice=input("play again?(y/n): "). lower()
    if choice != 'y':
        print("Thanks for playing!")
        break
    