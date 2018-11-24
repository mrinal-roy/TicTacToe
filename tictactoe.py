import random

def choose_first():
    A = random.randint(1,2)
    print("Player-{} goes first.".format(A))
    return A

def display_board(board):
    print('\n'*300)
    print(" "+board[0]+" | "+board[1]+" | "+board[2])
    print("---"+"|"+"---"+"|"+"---")
    print(" "+board[3]+" | "+board[4]+" | "+board[5])
    print("---"+"|"+"---"+"|"+"---")
    print(" "+board[6]+" | "+board[7]+" | "+board[8])
    
def player_input(A):
    if A == 1:
        print("Enter PLAYER-{} mark as either X or O: ".format(A))
        player1 = str(input()).upper()
        while (player1 != "X" and player1 != "O"):
            print("Enter PLAYER-{} mark as either X or O: ".format(A))
            player1 = str(input()).upper()
        if player1 == "X":
            player2 = "O"
        else:
            player2 = "X"
        return player1
    else:
        print("Enter PLAYER-{} mark as either X or O: ".format(A))
        player2 = str(input()).upper()
        while (player2 != "X" and player2 != "O"):
            print("Enter PLAYER-{} mark as either X or O: ".format(A))
            player2 = str(input()).upper()
        if player2 == "X":
            player1 = "O"
        else:
            player1 = "X"
        return player2
    

def player_choice(board):
    pos = int(input("Enter the position 1-9 where you want to place your marker: "))
    if space_check(board,pos):
        return pos
    else:
        pos = int(input("Entered position is not vacant; enter new position between 1-9: "))
    return pos
    
def space_check(board, position):
    return (board[position-1]!="X" and board[position-1]!="O")

def place_marker(board, marker, position):
    board[position-1] = marker
    display_board(board)
    
def full_board_check(board):
    count_full = 0
    for each in board:
        if (each == "X" or each == "O"):
            count_full += 1
        else:
            continue
    if count_full == 9:
        full = True
    else:
        full = False
    return full

def win_check(board, mark):
    if (board[0]==mark and board[1]==mark and board[2]==mark):
        return True
    elif (board[3]==mark and board[4]==mark and board[5]==mark):
        return True
    elif (board[6]==mark and board[7]==mark and board[8]==mark):
        return True
    elif (board[0]==mark and board[3]==mark and board[6]==mark):
        return True
    elif (board[1]==mark and board[4]==mark and board[7]==mark):
        return True
    elif (board[2]==mark and board[5]==mark and board[8]==mark):
        return True
    elif (board[0]==mark and board[4]==mark and board[8]==mark):
        return True
    elif (board[2]==mark and board[4]==mark and board[6]==mark):
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')
playTicTacToe = True
while playTicTacToe:
    
    board = ['1','2','3','4','5','6','7','8','9']
    display_board(board)

    marker = player_input(choose_first())

    position = player_choice(board)

#if space_check(board, position):
    place_marker(board, marker, position)

    while ((win_check(board,marker)==False) and (full_board_check(board)==False)):
        if marker == "X":
            marker = "O"
            print("Player with O mark to enter marker position choice.")
            position = player_choice(board)
            if space_check(board, position):
                place_marker(board, marker, position)
        else:
            marker = "X"
            print("Player with X mark to enter marker position choice.")
            position = player_choice(board)
            if space_check(board, position):
                place_marker(board, marker, position)
            
    if win_check(board,"X"):
        print("Player with X mark wins.")
    elif win_check(board,"O"):
        print("Player with O mark wins.")
    elif full_board_check(board):
        print("No One Wins!!! Good Luck to Both Players for Next Time!!!")

    print()
    playAgain = str(input("Do you want to play the game again? Enter 'Y' for Yes, OR 'N for No:'")).upper()
    if playAgain == "Y":
        playTicTacToe = playAgain
    else:
        playTicTacToe = False
        print("Do you serieusly want to quit? Then type 'N' buddy.")
        playAgain = str(input()).upper()
        if playAgain == "N":
            print("Thank you for playing Tic Tac Toe!!! See you soon again!!!")
        else:
            print("Are you kidding? Its time to QUIT !!!")
            
    
