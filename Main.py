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
    while True:
        if position.isdigit():
            position = int(position)
            if position in range (1,10):
                break

        position = input("Please enter a valid input(1-9): ")
    return int(position)

# Checks if the given position is available or is already taken
def is_postition_available(board, position):
    if board[position] in [1,2,3,4,5,6,7,8,9]:
        return True
    else:
        return False

# Checks if there is any available space in the board for the game to continue
def is_board_full(board):
    for i in range(1,10):
        if i in board:
            return False
    return True

# Checks if either of the players have won the game
def iswin(board,player):
    if board[1] == board[2] == board[3] == player:
        return True
    elif board[1] == board[4] == board[7] == player:
        return True
    elif board[4] == board[5] == board[6] == player:
        return True
    elif board[7] == board[8] == board[9] == player:
        return True
    elif board[2] == board[5] == board[8] == player:
        return True
    elif board[3] == board[6] == board[9] == player:
        return True
    elif board[1] == board[5] == board[9] == player:
        return True
    elif board[7] == board[5] == board[3] == player:
        return True
    else:
        return False

# Asks the user if they want to continue playing or stop the game
def is_replay():
    isreplay = input("Do you want to continue this game or stop playing?(Y/N): ")
    isreplay = isreplay.upper()
    while isreplay not in ["Y","N"]:
        isreplay = input("Please enter a valid input (only Y/N): ")
    if isreplay == "Y":
        return True
    else:
        return False

if __name__ == "__main__":    
    isreplay = True
    while isreplay == True:
        board = [0,1,2,3,4,5,6,7,8,9]
        player1, player2 = player_input()
        while True:
            print("The current board is: ")
            display_board(board)

            print("Player 1 turn: ")
            player1_position = user_position()
            if is_postition_available(board, player1_position):
                board = place_marker(board, player1, player1_position)
            else:
                print("Sorry, postition not available")
                player1_position = user_position()
            
            if iswin(board, player1):
                display_board(board)
                print("Player 1 won the game")
                break
            elif is_board_full(board):
                print("The game ended in a draw")
                break
            else:
                print("The current board is: ")
                display_board(board)

            print("Player 2 turn: ")
            player2_position = user_position()
            if is_postition_available(board, player2_position):
                board = place_marker(board, player2, player2_position)
            else:
                print("Sorry, postition not available")
                player2_position = user_position()
            
            if iswin(board, player2):
                display_board(board)
                print("Player 2 won the game")
                break
            elif is_board_full(board):
                print("The game ended in a draw")
                break
            else:
                print("The current board is: ")
                display_board(board)

        isreplay = is_replay()
    else:
        print("Thank you for your time!")
        
       

    
    