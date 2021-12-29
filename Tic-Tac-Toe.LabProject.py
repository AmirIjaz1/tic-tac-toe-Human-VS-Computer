#-------------------Hafiz Amir Ijaz(SP18-BCS-026)
#-------------------Abdullah Bin Tahir(SP18-BCS-011)




select=False
player =1
count=0

def winnerCheck(list_2d):
    row=0
    col=0
    while(row<=2):
        if(list_2d[row][col]=='x' and list_2d[row][col+1]=='x' and list_2d[row][col+2]=='x'):
            print("Computer Wins")
            main()
        row+=1

    row=0
    col=0
    while(col<=2):
        if(list_2d[row][col]=='x' and list_2d[row+1][col]=='x' and list_2d[row+2][col]=='x'):
            print("Computer Wins")
            main()

        col+=1

def addComputerValue(list_2d):
    global select
    terminate=True
    row=0
    while(row<=2 and terminate):
        col=0
        while(col<=2):
            if(list_2d[row][col]!='x' and list_2d[row][col]!=1):
                list_2d[row][col]='x'
                terminate=False
                break
            elif(list_2d[col][row]!='x' and list_2d[col][row]!=1):
                list_2d[col][row]='x'
                terminate=False
                break
            col+=1
        row+=1

    select=False    
    declareValues(list_2d)

def computerTurn(list_2d):
    check=True
    global select
    store=0
    print("Computer Turn")
    row=0
    while(row<=2):
        col=0
        datacheck=0
        while(col<=2):
            if(list_2d[row][col]==1):
                datacheck+=1    
            else:
                store=col
            col+=1
            # else:
            #     break
        if datacheck==2 and list_2d[row][store]!='x':
            list_2d[row][store]='x'
            check=False
            select=False
            declareValues(list_2d)
        row+=1

    col=0
    while(col<=2):
        row=0
        datacheck=0
        while(row<=2):
            if(list_2d[row][col]==1):
                datacheck+=1    
            else:
                store=row
            row+=1
            # else:
            #     break
        if datacheck==2 and list_2d[store][col]!='x':
            list_2d[store][col]='x'
            check=False
            select=False    
            declareValues(list_2d)
        col+=1
    
    diagonal=0
    countValue=0
    storeValue=0
    while(diagonal<=2):
        if(list_2d[diagonal][diagonal]==1):
            countValue+=1
        else:
            storeValue=diagonal
        diagonal+=1
    if(countValue==2 and list_2d[storeValue][storeValue]!='x'):
        list_2d[storeValue][storeValue]='x'
        check=False
        select=False  
        declareValues(list_2d)

    if(check):
        addComputerValue(list_2d)
    else:
        select=False    
        declareValues(list_2d)

def getUserValue(list_2d):
    global select
    print("Player No ",player, " Your Turn")
    row=eval(input("Enter Row No"))
    col=eval(input("Enter Column No"))
    if(list_2d[row][col]==1 or list_2d[row][col]=='x'):
        print("This Position Is Already Taken Please Select A New One")
        getUserValue(list_2d)
    else:
        list_2d[row][col]=1
        select=True
        declareValues(list_2d)
    


def declareValues(list_2d):
    global select, count
    count+=1
    i=0
    while(i<=2):
        j=0
        while(j<=2):
            print(" ",list_2d[i][j],end =" ")
            j+=1
        i+=1    
        print("")
    if(count<10):
        if(select):
            computerTurn(list_2d)
        else:
            winnerCheck(list_2d)
            getUserValue(list_2d)   
    else:
        print("Game Draw")
        main() 
        
def main():
    global count
    count=0
    check=eval(input("You want to Playe The Game Prees 1 For Yes Else Press 2 "))
    
    if(check==1):
        list_2d=[ [0,0,0,] , [0,0,0] , [0,0,0] ] 
        declareValues(list_2d)
    else:
        print("Thanks For Playing The Game")
        quit()


main()