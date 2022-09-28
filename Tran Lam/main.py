#Tic Tac Toe game 

Xplayer = "X"
gameRunning = True
winner = None
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#This function prints the board game
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] + " | " )
    print ("-----------")
    print(board[3] + " | " + board[4] + " | " + board[5] + " | " )
    print ("-----------")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | " )
    print ("-----------")

#This function takes player input
def playerInput(board):
    inp = int(input("Enter a number from 1-9:"))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = Xplayer
    elif inp < 1 or inp > 9:
        print("Invalid input. Please enter a valid number.")
    else: 
        print("The spot is already taken.")

    #input verification
#This function check for win or tie 
    #check row 
def checkRow(board):
    global winner  
    if board [0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True 
    if board [3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True 
    if board [6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True 

    #check column
def checkColumn(board):
    global winner  
    if board [0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True 
    if board [1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True 
    if board [2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True 

    #check diagonos
def checkDiag(board):
    global winner 
    if board [0] == board[4] == board[8] and board[0] != "-":
        winner = board[1]
        return True 
    if board [2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True 
    
    #check tie
def checkTie(board):
    global gameRunning
    if "-" not in board: 
        printBoard(board)
        print("It is a tie!")
        gameRunning = False 
    
    #check Win 
def checkWin(board):
    global gameRunning
    if checkDiag(board) or checkRow(board) or checkColumn(board): 
        print(f"The winner is {winner}")
        gameRunning = False

#This function switch players.
def switchPlayer():
    global Xplayer 
    if Xplayer == "X":
        Xplayer = "O"
    else:
        Xplayer = "X"

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()

