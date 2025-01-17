import sys
import random

player = 0
turn = 1

#board="""\
#| |1|2|3|4|5|6|7|8|9|10|
#|A| | | | | | | | | |  |
#|B| | | | | | | | | |  |
#|C| | | | | | | | | |  |
#|D| | | | | | | | | |  |
#|E| | | | | | | | | |  |
#|F| | | | | | | | | |  |
#|G| | | | | | | | | |  |
#|H| | | | | | | | | |  |
#|I| | | | | | | | | |  |
#|J| | | | | | | | | |  |"""

if(sys.argv[1]=="P1"):
    player = "Player 1"
if(sys.argv[1]=="P2"):
    player = "Player 2"

while(player==0):
    x = str(input('Invalid argument. Please enter "P1" or "P2": '))
    match x:
        case "P1":
            player = "Player 1"
        case "P2":
            player = "Player 2"

print()
print(player,", Turn ",turn)

board=[[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",]]

def printBoard():
    for i in range(64,75):
        if i==64:
            print("| |1|2|3|4|5|6|7|8|9|10|")
        else:
            line = "|"+chr(i)+"|"
            for j in range(0,9):
                line = line+board[i-65][j]+"|"
            
            line = line+"  |"
            print(line)

printBoard()

shipsPlaced = False

def placeShip(length,type):
    
    curLen = 1
    finished = False
    while(finished == False):
        
        x = random.randrange(0,9)
        y = random.randrange(0,9)
        
        if(shipOri(x,y,length,type) == True):
            finished = True

def shipOri(posX,posY,length,type):
    finished = False
    
    while(finished == False):
        
        failed1 = 0
        failed2 = 0
        failed3 = 0
        failed4 = 0
        
        if((failed1+failed2+failed3+failed4)==4):
            return False
        
        curX = posX
        curY = posY
        dir = random.randrange(1,4)
        
        
        
        if(dir == 1):
            placed = 1
            
            while(placed < length):
                
                if(curX+1 > 9):
                    failed1 = 1
                    placed = length
                elif(board[curX+1][curY] == " "):
                    board[curX+1][curY] = type
                    curX = curX+1
                    placed = placed+1
                else :
                    failed1 = 1
                    placed = length
                
                if(placed == length and failed1 == 0):
                    return True
                    
        elif(dir == 2):
            
            placed = 1
            
            while(placed < length):
                
                if(curY+1 > 9):
                    failed2 = 1
                    placed = length
                elif(board[curX][curY+1] == " "):
                    board[curX][curY+1] = type
                    curY = curY+1
                    placed = placed+1
                else :
                    failed2 = 1
                    placed = length
                    
                if(placed == length and failed2 == 0):
                    return True
                    
        elif(dir == 3):
            
            placed = 1
            
            while(placed < length):
                
                if(curX-1 > 9):
                    failed3 = 1
                    placed = length
                elif(board[curX-1][curY] == " "):
                    board[curX-1][curY] = type
                    curX = curX-1
                    placed = placed+1
                else :
                    failed3 = 1
                    placed = length
                    
                if(placed == length and failed3 == 0):
                    return True
                    
        elif(dir == 4):
            
            placed = 1
            
            while(placed < length):
                
                if(curY-1 > 9):
                    failed1 = 1
                    placed = length
                elif(board[curX][curY-1] == " "):
                    board[curX][curY-1] = type
                    curY = curY-1
                    placed = placed+1
                else:
                    failed4 = 1
                    placed = length            
                    
                if(placed == length and failed4 == 0):
                    return True

placeShip(5,"C")
placeShip(4,"B")
placeShip(3,"R")
placeShip(3,"S")
placeShip(2,"D")
    
printBoard()

#move = str(input('Please enter sector to attack (ie, "A1"): '))

#Carrier = 5
#Battleship = 4
#Cruiser = 3
#Submarine = 3
#Destroyer = 2