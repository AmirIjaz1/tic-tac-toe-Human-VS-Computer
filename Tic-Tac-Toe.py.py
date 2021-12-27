import random

# Game Title
print("     ______________________________________      ")
print("    |             WELCOME TO              |      ")
print("    |    ----------------------------     |      ")
print("    |    *  _____    _____   _____  *     |      ")
print("    |    *    |        |       |    *     |      ")
print("    |    *    |        |       |    *     |      ")
print("    |    *    ||C      |AC     |0E  *     |      ")
print("    |    *--------------------------*     |      ")
print("    |_____________________________________|      ")


#randomly choose who will start first the game(toss)
def who_start():
    return random.randint(1,2)

#initialize blank board
def initialize_board(board):
    for i in range(0,3):
        for j in range(0,3):
            board[i][j]=" "


#this function will initialize board and print the current player(who will start first)
def start_game(board,players,player):
    initialize_board(board)
    players[1]=input("Enter your name P1 (symbol X) : ")
    print(players[player],"Won the toss.",players[player],"will start first ")
    print()

#will print the board
def printboard(board):
    cell=""
    print("..........")
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]=="O":
                cell="O"
            elif board[i][j]=="X":
                cell="X"
            else:
                cell=" "
            print("|",cell,end="")
          
        print("|")
        print("__________")
    print()
    
#take input from the player where he want to put his bet
#player moves with input
def user_move(board,players,player):
    print(players[player]," now will take move")
    row=int(input("choose row where you want to put the bet: "))
    col=int(input("choose column where you want to put the bet: "))
    if player==1:
        board[row-1][col-1]="X"
    else:
        board[row-1][col-1]="O"

    printboard(board)


#computer defined moves
def computer_move(board,players,player):
    print(players[player],"has taken move")
    #winning moves 
    #check for rows
    for i in range(3):
        if board[i].count("O")==2:
            for j in range(3):
                if board[i][j]=="":
                    board[i][j]="O"
                    printboard(board)
                    return
    
    
    #check for column
    for i in range(3):
        count=0
        for j in range(3):
            if board[j][i]=="O":
                count+=1
        if count==2:
            for j in range(3):
                if board[i][j]=="":
                    board[i][j]="O"
                    printboard(board)
                    return
                                                  
    #check for 1st diagonal
    count1=0
    locationM=-1
    for i in range(3):
        if board[i][i]=="O":
            count1+=1
        if board[i][i]=="":
            locationM=i
    if count1==2 and locationM!=-1:
        board[locationM][locationE]="O"
        printboard(board)
        return

    #check for 2nd diagonal
    count1=0
    locationM=-1
    for i in range(3):
        if board[i][2-i] == "O":
            count1 += 1
        if board[i][i] == "":
            locationM = i
    if count1 == 2 and locationM != -1:
        board[locationM][2-locationE] = "O"
        printboard(board)
        return
    
    #for stoping the opponent winnings
    
    #check for rows
    for i in range(3):
        if board[i].count("X")==2:
            for j in range(3):
                if board[i][j]=="":
                    board[i][j]="O"
                    prinboard(board)
                    return
    #check for column
    for i in range(3):
        count=0
        for j in range(3):
            if board[j][i]=="X":
                count+=1
        if count==2:
            for j in range(3):
                if board[i][j]=="":
                    board[i][j]="O"
                    printboard(board)
                    return
    #check for 1st diagonal
    count1=0
    locationM=-1
    for i in range(3):
        if board[i][i]=="X":
            count1+=1
        if board[i][i]=="":
            locationM=i
    if count1==2 and locationM!=-1:
        board[locationM][locationE]="O"
        printboard(board)
        return

    #check for 2nd diagonal
    count1=0
    locationM=-1
    for i in range(3):
        if board[i][2-i] == "X":
            count1 += 1
        if board[i][i] == "":
            locationM = i
    if count1 == 2 and locationM != -1:
        board[locationM][2-locationE] = "O"
        printboard(board)
        return
        
   #non-critical bet(preferred corners and center)
    if board[0][0]=="":
        board[0][0]=="O"
        printboard(board)
        return

    if board[1][1]=="":
        board[1][1]=="O"
        printboard(board)
        return
        
    if board[0][2]=="":
        board[0][2] == "O"
        printboard(board)
        return
    
    if board[2][0] == "":
        board[2][0] == "O"
        printboard(board)
        return
    
    if board[2][2] == "":
        board[2][2] == "O"
        printboard(board)
        return
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] == "O"
                printboard(board)
                return
            
         
#check the board conditions        
def winning_conditions(board):
    for player in range(1,3):
        if player==1:
            symbol="X"
        else:
            symbol="O"
        for i in range(0,3):
            if(board[i][0]==symbol)and(board[i][1]==symbol)and (board[i][2]==symbol):
                return player+1
        for i in range(0,3):
            if (board[0][i] == symbol) and (board[1][i] == symbol) and (board[2][i] == symbol):
                return player+1
        if (board[0][0] == symbol) and (board[1][1] == symbol) and (board[2][2] == symbol):
            return player+1
        if (board[0][2] == symbol) and (board[1][1] == symbol) and (board[2][0] == symbol) :
            return player+1

    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==" ":
                return 0
    return 1

#toggle the player
def flip_player(playeringame):
    if playeringame==1:
        return 2
    else:
        return 1


#announce the result
def result_state(state,states,players):
    if states[state]=="DRAW":
        print("Game draw")
    elif states[state]=="P1 WINS":
        print(players[1],"won the game")
    elif states[state] == "P2 WINS":
        print(players[2], "won the game")
    print()

    return int(input("If you want to play again press 1 or if you want to exit press O: "))


#this will restart the game if user want to play again            
def restartgame(board,players,whostarted):
    initialize_board(board)
    whostarted=flip_player(whostarted)
    print("............___________________........ ")
    print("\t\t\tin this game ",players[whostarted],"will start the game.")
    print(" ")


    return whostarted


#main parogram
def main():
   
    
    #variables

   #      row_1(board-index 0)[" "," "," "]
   #      row-2(board-index 1)[" "," "," "]
   #      row-3(board-index 2)[" "," "," "]
   board=[[" "," "," "],[" "," "," "],[" "," "," "]]

   # P1 at index of 1 and  computer  is at index of 2
   players=[" ","P1","computer"]

   #these are the 4 states
   states=["PLAY","DRAW","P1 WINS","P2 WINS"]

   #current player
   playeringame=0

   #initial state is 0(PLAY)
   state=0

   #after toogle here we will store our current player
   whostarted=0

  
   playeringame=who_start()
   whostarted=playeringame
   start_game(board,players,whostarted)
    
   while True:
        
        #check whose turn is to put the bet
        if playeringame==1:
            user_move(board, players, playeringame)
        else:
            computer_move(board, players, playeringame)
        
        #check the state/condition of the board
        state=winning_conditions(board)

        if states[state]=="PLAY":
            playeringame=flip_player(playeringame)
        else:
            playmore=result_state(state,states,playeringame)
            if playmore==1:             #check user want to play again or not
                playeringame=restartgame(board,players,whostarted)
                whostarted=playeringame
                
            else:
                print("\t\t\tThanks for playing")
 
                break


main()

