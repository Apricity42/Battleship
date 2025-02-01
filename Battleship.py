import sys
import random

#Global declaration
player = 0
turn = 1

safeC = 5
safeB = 4
safeR = 3
safeS = 3
safeD = 2

if(len(sys.argv) > 1):
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
print(player)
print("")

#Board reference
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
#|J| | | | | | | | | |  |

#Global declaration

blankBoard=[[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",],[" "," "," "," "," "," "," "," "," "," ",]]

defBoard = blankBoard.copy()
offBoard = blankBoard.copy()
startDefBoard = blankBoard.copy()

def printBoard(boardU1):
    print("")
    for i in range(64,75):
        if i==64:
            print("| |1|2|3|4|5|6|7|8|9|10|")
        else:
            line = "|"+chr(i)+"|"
            for j in range(0,9):
                line = line+boardU1[i-65][j]+"|"
            
            line = line+boardU1[i-65][9]+" |"
            print(line)
    print("")
def placeShip(boardU2,length,type):
    
    curLen = 1
    finished = False
    while(finished == False):
        
        x = random.randrange(0,9)
        y = random.randrange(0,9)
        
        if(shipOri(boardU2,x,y,length,type) == True):
            finished = True

def shipOri(boardU3,posX,posY,length,type):
    
    finished = False

    if(boardU3[posX][posY] != " "):
        return False
    
    failed1 = 0
    failed2 = 0
    failed3 = 0
    failed4 = 0
    
    while(finished == False):
        
        if((failed1+failed2+failed3+failed4)==4):
            return False
        
        curX = posX
        curY = posY
        dir = random.randrange(1,5)
        
        if(dir == 1):
            placed = 0
            safe = 1
            while(placed < length):
                
                if(curX+1 > 9 or curX+1 < 0):
                    failed1 = 1
                    placed = length
                elif(boardU3[curX+1][curY] == " "):
                    curX = curX+1
                    safe = safe+1
                else:
                    failed1 = 1
                    placed = length
                    
                if(safe == length):
                    curX = posX
                    curY = posY
                    
                    boardU3[curX][curY] = type
                    placed = 1
                    
                    while(placed < length):
                        boardU3[curX+1][curY] = type
                        curX = curX+1
                        placed = placed+1
                        
                    return True
                    
        elif(dir == 2):
            placed = 0
            safe = 1
            while(placed < length):
                
                if(curY+1 > 9 or curY+1 < 0):
                    failed2 = 1
                    placed = length
                elif(boardU3[curX][curY+1] == " "):
                    curY = curY+1
                    safe = safe+1
                else:
                    failed2 = 1
                    placed = length
                    
                if(safe == length):
                    curX = posX
                    curY = posY
                    
                    boardU3[curX][curY] = type
                    placed = 1
                    
                    while(placed < length):
                        boardU3[curX][curY+1] = type
                        curY = curY+1
                        placed = placed+1
                        
                    return True
                    
        elif(dir == 3):
            placed = 0
            safe = 1
            while(placed < length):
                
                if(curX-1 > 9 or curX-1 < 0):
                    failed3 = 1
                    placed = length
                elif(boardU3[curX-1][curY] == " "):
                    curX = curX-1
                    safe = safe+1
                else:
                    failed3 = 1
                    placed = length
                    
                if(safe == length):
                    curX = posX
                    curY = posY
                    
                    boardU3[curX][curY] = type
                    placed = 1
                    
                    while(placed < length):
                        boardU3[curX-1][curY] = type
                        curX = curX-1
                        placed = placed+1
                        
                    return True
                    
        elif(dir == 4):
            placed = 0
            safe = 1
            while(placed < length):
                
                if(curY-1 > 9 or curY-1 < 0):
                    failed4 = 1
                    placed = length
                elif(boardU3[curX][curY-1] == " "):
                    curY = curY-1
                    safe = safe+1
                else:
                    failed4 = 1
                    placed = length
                    
                if(safe == length):
                    curX = posX
                    curY = posY
                    
                    boardU3[curX][curY] = type
                    placed = 1
                    
                    while(placed < length):
                        boardU3[curX][curY-1] = type
                        curY = curY-1
                        placed = placed+1
                        
                    return True

#def saveOriginal(initial, copy):
    

def takeInput():
    
    validInput = False
    validX = -1
    validY = -1
    
    while(not(validInput)):
        tempInput = str(input('Fire at coordinate: '))
        
        if(len(tempInput) == 2 or len(tempInput) == 3):
            if(tempInput[0].isalpha()):
                try:
                    dummyVal = int(tempInput[1])

                    conditionalCheck = True
                    twoDigit = False
                    
                    if(len(tempInput) == 3):
                        if(type(tempInput[2]) == int):
                            #conditionalCheck already true
                            twoDigit = True
                        else:
                            conditionalCheck = False
                            
                    if(conditionalCheck):
                        if(ord(tempInput[0].upper()) >= 65 and ord(tempInput[0].upper()) <= 74):
                            validX = ord(tempInput[0].upper()) - 65
                            
                            tempY = int(tempInput[1:])
                            if(tempY >= 1 and tempY <= 10):
                                validY = tempY - 1
                                validInput = True
                except ValueError as ve:
                    dummyVal = False
    
    return [validX, validY]

def processInput(board, coords):
    #Ships: C|B|R|S|D
    #Hit: H
    #Miss: M
    
    global safeC
    global safeB
    global safeR
    global safeS
    global safeD
    
    value = board[coords[0]][coords[1]]
    
    if(value == "H" or value == "M"):
        return False
    elif(value == " "):
        print("Miss")
        board[coords[0]][coords[1]] = "M"
        return True
    else:
        if(value == "C"):
            safeC=safeC - 1
            board[coords[0]][coords[1]] = "H"
            
            if(safeC == 0):
                print("Sunk Carrier")
                return True
            else:
                print("Hit")
                return True
                
        if(value == "B"):
            safeB=safeB - 1
            board[coords[0]][coords[1]] = "H"
            
            if(safeB == 0):
                print("Sunk Battleship")
                return True
            else:
                print("Hit")
                return True
                
        if(value == "R"):
            safeR=safeR - 1
            board[coords[0]][coords[1]] = "H"
            
            if(safeR == 0):
                print("Sunk Cruiser")
                return True
            else:
                print("Hit")
                return True
                
        if(value == "S"):
            safeS=safeS - 1
            board[coords[0]][coords[1]] = "H"
            
            if(safeS == 0):
                print("Sunk Submarine")
                return True
            else:
                print("Hit")
                return True
                
        if(value == "D"):
            safeD=safeD - 1
            board[coords[0]][coords[1]] = "H"
            
            if(safeD == 0):
                print("Sunk Destroyer")
                return True
            else:
                print("Hit")
                return True
    
def gameLoop():
    gameOngoing = True
    
    while(gameOngoing):
        turnFinished = False
        
        while(not(turnFinished)):
            turnFinished = processInput(defBoard, takeInput())
            
        printBoard(defBoard)    
            
            


placeShip(defBoard,5,"C") #Carrier = 5
placeShip(defBoard,4,"B") #Battleship = 4
placeShip(defBoard,3,"R") #Cruiser = 3
placeShip(defBoard,3,"S") #Submarine = 3
placeShip(defBoard,2,"D") #Destroyer = 2

gameLoop()

printBoard(defBoard)
