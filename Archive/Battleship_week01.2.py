import sys

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


for i in range(64,75):
    if i==64:
        print("| |1|2|3|4|5|6|7|8|9|10|")
    else:
        line = "|"+chr(i)+"|"
        for j in range(0,9):
            line = line+board[i-65][j]+"|"
        
        line = line+"  |"
        print(line)
        
#move = str(input('Please enter sector to attack (ie, "A1"): '))

#Carrier = 5
#Battleship = 4
#Cruiser = 3
#Submarine = 3
#Destroyer = 2
