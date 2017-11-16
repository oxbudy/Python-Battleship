#Battleship attempt
rowp1 = [[" "," A"," B"," C"," D"," E"], ["1"," /"," /"," /"," /"," /"], ["2"," /"," /"," /"," /"," /"],
       ["3"," /"," /"," /"," /"," /"], ["4", " /", " /", " /", " /", " /"], ["5"," /"," /"," /"," /"," /"]]

def Showboardp1():
#Prints Player1's row
    for pos in range(6):
        for num in range(6):
            print(rowp1[pos][num], end="")
        print("")



def Placeships():
    #Prompts users to place ships at coordinates at start of the game
    scout = input("Where would you like to place your 1st ship (2x1)? Type the coordinate and direction like so: c2h")
    scout = list(scout)

    Shipprocessp1(scout)

    scout2 = input("Where would you like to place your 2nd ship (2x1)? Type the coordinate and direction like so: c2h")
    scout2 = list(scout2)

    Shipprocessp1(scout2)

def Shipprocessp1(ship):
    # Handles placing the ships using user entered coordinates

    ship[1] = int(ship[1])

    for col1 in enumerate("abcde"):
        if ship[0] == col1[1]:
            if ship[2] == "h":
                if ship[0] == "e":
                    print("Invalid placement! Remember that the extra length of each ship extends right and down from "
                          "your original XY coordinate!")
                    Placeships()
                else:
                    rowp1[ship[1]][col1[0] + 1] = " o"
                    rowp1[ship[1]][col1[0] + 2] = " o"

            else:
                if ship[1] == 5:
                    print("Invalid placement! Remember that the extra length of each ship extends right and down from "
                          "your original XY coordinate!")
                    Placeships()
                else:
                    rowp1[ship[1]+1][col1[0]+1] = " o"
                    rowp1[ship[1]][col1[0]+1] = " o"

def Shipprocessp2(ship):
    # Handles placing the ships using user entered coordinates

    ship[1] = int(ship[1])

    for col1 in enumerate("abcde"):
        if ship[0] == col1[1]:
            if ship[2] == "h":
                if ship[0] == "e":
                    print("Invalid placement! Remember that the extra length of each ship extends right and down from "
                          "your original XY coordinate!")
                    Placeships()
                else:
                    rowp2[ship[1]][col1[0] + 1] = " o"
                    rowp2[ship[1]][col1[0] + 2] = " o"

            else:
                if ship[1] == 5:
                    print("Invalid placement! Remember that the extra length of each ship extends right and down from "
                          "your original XY coordinate!")
                    Placeships()
                else:
                    rowp2[ship[1]+1][col1[0]+1] = " o"



def Playerone():
    #Player one chooses where to attack
    p1turn = input("Player 1, what coordinate would you like to attack? Remember to enter in XY format ")
    p1turn = list(p1turn)
    p1turn[1] = int(p1turn[1])

    for search in enumerate("abcde"):
        if p1turn[0] == search[1]:
            if rowp1[p1turn[1]][search[0]+1] == " o":
                print("Hit!")
                rowp1[p1turn[1]][search[0]+1] = " *"
            else:
                print("Missed!")
                rowp1[p1turn[1]][search[0] + 1] = " ."

#--------------------------------------------




clear = "\n" * 100
winner = False

Remainingspots = 4
Showboardp1()
Placeships()
print(clear)
while winner == False:
    Showboardp1()
    Playerone()
    for wincon in range(6):
        for wincon2 in range(5):
            if rowp1[wincon][wincon2] == " *":
                Remainingspots -= 1
    if Remainingspots == -6:
        winner = True
    print(clear)

print("You won a very easy game")