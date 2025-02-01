player =0
turn =1

board="""\
| |1|2|3|4|5|6|7|8|9|10|
|A| | | | | | | | | |  |
|B| | | | | | | | | |  |
|C| | | | | | | | | |  |
|D| | | | | | | | | |  |
|E| | | | | | | | | |  |
|F| | | | | | | | | |  |
|G| | | | | | | | | |  |
|H| | | | | | | | | |  |
|I| | | | | | | | | |  |
|J| | | | | | | | | |  |"""


while(player==0):
    x = str(input('Please enter "P1" or "P2": '))
    match x:
        case "P1":
            player = "Player 1"
        case "P2":
            player = "Player 2"

print()
print(player,", Turn ",turn)
print(board)

move = str(input('Please enter sector to attack (ie, "A1"): '))