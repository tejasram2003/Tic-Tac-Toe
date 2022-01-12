#TicTacToe program

# Displays the board 
def display_board(board):
    print(board[1],"|",board[2],"|",board[3])
    print("-"*11)
    print(board[4],"|",board[5],"|",board[6])
    print("-"*11)
    print(board[7],"|",board[8],"|",board[9])
    print(" ")

# Recieves user input for Player1 and assigns Player2 based on Player1 input,
# Returns the tuple of Player choices
def player_input():
    player1_choice = input("player 1: Do you wanna play as X or O: ")
    player1_choice = player1_choice.upper()
    while player1_choice not in ["X","O"]:
        player1_choice = input("Please enter a valid input: ")
    if player1_choice == "X":
        player2_choice = "O"
    else:
        player2_choice = "X"

    return (player1_choice, player2_choice)

# Takes in the position and marks the marker in that position
def place_marker(board, marker, position):
    board[position] = marker
    return board

# Picks out a user randomly to go first
def toss():
    import random
    from random import randint
    toss = random.randint(1,2)
    return toss

# Getting user input for position
def user_position():
    position = input("Define your next move(1-9): ")
    while int(position) not in range (1,10):
        position = input("Please enter a valid input(1-9): ")
    return int(position)

# Checks if the given position is available or is already taken
def position_check(board, position):
    if board[position] in [1,2,3,4,5,6,7,8,9]:
        return True
    else:
        return False

def full_board_check(board):
    for i in range(1,10):
        if i in board:
            return False
    return True

if __name__ == "__main__":
    board = ["x"]
    if full_board_check(board) == True:
        print("Board is full, game over")
    else:
        print("The board is still available")
    
    