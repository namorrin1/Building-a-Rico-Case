'''
def main():
    print("Hello Welcome to the Rico Case: \n")
    coreLoop()


def coreLoop():
    toggle = True
    while(toggle):
        choice = input(
        "Press 'A' to activate Manual Control Mode \n" \
        "Press 'B' to activate Write Mode \n" \
        "Press 'C' to activate Roomba Mode \n" \
        "Press 'D' to activate Draw Mode \n" \
        "Press 'E' to activate Song Mode \n")
        toggle = switch(choice.upper())

def switch(choice):
    match choice: 
        case 'A':
            print("Welcome to Manual Control Mode \n")
            #manual code goes here
            return False
        case 'B':
            print("Welcome to Write Mode \n")
            usrStrInput = input("Enter the phrase you want Rico to repeat: \n"
                           "The phrase cannot exceed 15 characters \n" \
                           "Enter phrase here:")
            write(usrStrInput)
            return False
        case 'C':
            print("Welcome to Roomba Mode \n")
            usrRoombaToggle = input("Enter 'Go' to make Rico become a Roomba \n"
                                    "Enter 'Stop' to make Rico stop \n"
                                    "Enter command here: ")
            roomba(usrRoombaToggle)
            
            return False
        case 'D': 
            print("Welcome to Draw Mode \n")
            usrDrawInput = input("Choose a shape for Rico to draw: \n" \
                                "Type 'Square' for Rico to draw a Square \n" \
                                "Type 'Hexagon' for Rico to draw a Hexagon \n" \
                                "Type 'Star' for Rico to draw a Star \n" \
                                "Enter your choice here: ")
            usrDrawLength = int(input("Enter the length for your Shape: "))
            drawMode(usrDrawInput, usrDrawLength)
            return False
        case 'E':
            print("Welcome to Song Mode \n")
            usrSongChoice = input("Choose a song for Rico to sing: \n" \
                                "Type 'Mary' for Mary Had a Little Lamb \n" \
                                "Type 'Saints' for Oh When the Saints Come Marching In \n" \
                                "Type 'Twinkle' for Twinkle Twinkle Little Star \n" \
                                "Enter your choice here: ")
            
            songMode(usrSongChoice)
            return False
        case _:
            print("Not a valid choice! Please Enter a Letter from A -> E")
            return True
        
def drawMode(drawInput, drawLength):
    if drawInput == 'SQUARE':
        makeSquare(drawLength)
    elif drawInput == 'HEXAGON':
        makeHex(drawLength)
    elif drawInput == 'STAR':
        makeStar(drawLength)

def songMode(songChoice):
    if songChoice == 'MARY':
        makeMary()
    elif songChoice == 'SAINTS':
        makeSaints()
    elif songChoice == 'TWINKLE':
        makeTwinkle()
    

main()
'''