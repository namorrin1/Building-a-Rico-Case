from lib.BirdBrain import Finch
#import keyboard
import threading 
import time
finch = Finch('A')
#finch.setMove('F', 10, 100)
#finch.setTurn('R', 360, 30)
def main():
    print("Hello. Welcome to the Rico Case: \n")
    #roomba()
    #drawMode('hexagon', 10)
    #roomba('go')
    coreLoop()

    
    

def coreLoop():
    toggle = True
    while(toggle):
        choice = input(
        "Press 'A' to activate Manual Control Mode \n" \
        "Press 'B' to activate Write Mode \n" \
        "Press 'C' to activate Roomba Mode \n" \
        "Press 'D' to activate Draw Mode \n" \
        "Press 'E' to activate Song Mode \n" \
        "Press 'Q' to quit\n")
        toggle = switch(choice.upper())

def switch(choice):
    match choice: 
        case 'A':
            print("Welcome to Manual Control Mode \n")
            #manual code goes here
            return True
        case 'B':
            print("Welcome to Write Mode \n")
            usrStrInput = input("Enter the phrase you want Rico to repeat: \n"
                           "The phrase cannot exceed 15 characters \n" \
                           "Enter phrase here:")
            write(usrStrInput)
            return True
        case 'C':
            print("Welcome to Roomba Mode \n")
            usrRoombaToggle = input("Enter 'Go' to make Rico become a Roomba \n"                 
                                    "Enter command here: ")
            if usrRoombaToggle.upper() == 'GO':
                roomba()
            
            return True
        case 'D': 
            print("Welcome to Draw Mode \n")
            usrDrawInput = input("Choose a shape for Rico to draw: \n" \
                                "Type 'Square' for Rico to draw a Square \n" \
                                "Type 'Hexagon' for Rico to draw a Hexagon \n" \
                                "Type 'Star' for Rico to draw a Star \n" \
                                "Enter your choice here: ")
            usrDrawLength = int(input("Enter the length for your Shape: "))
            drawMode(usrDrawInput, usrDrawLength)
            return True
        case 'E':
            print("Welcome to Song Mode \n")
            usrSongChoice = input("Choose a song for Rico to sing: \n" \
                                "Type 'Mary' for Mary Had a Little Lamb \n" \
                                "Type 'Saints' for Oh When the Saints Come Marching In \n" \
                                "Type 'Twinkle' for Twinkle Twinkle Little Star \n" \
                                "Enter your choice here: ")
            
            songMode(usrSongChoice)

            return True
        case 'Q':
            return False
        case _:
            print("Not a valid choice! Please Enter a Letter from A -> E")
            return True
        
def drawMode(drawInput, drawLength):
    if drawInput.upper() == 'SQUARE':
        makeSquare(drawLength)
    elif drawInput.upper() == 'HEXAGON':
        makeHex(drawLength)
    elif drawInput.upper() == 'STAR':
        makeStar(drawLength)

def songMode(songChoice):
    if songChoice.upper() == 'MARY':
        makeMary()
    elif songChoice.upper() == 'SAINTS':
        makeSaints()
    elif songChoice.upper() == 'TWINKLE':
        makeTwinkle()


def roomba():
    status = {'active' : True}
    def drive():
        #this runs in the background thread 
        while status['active']:
            distance = finch.getDistance()
            if distance > 15: 
                finch.setMotors( 15, 15)
            else:
                finch.stop() 
                finch.setTurn('L', 90, 50)
            time.sleep(0.05) #this was recommended so the loop doesn't overwork the CPU
        finch.stop()
    #background thread
    mover = threading.Thread(target=drive)
    mover.daemon = True
    mover.start()

    while True: 
        stopCommand = input("Type 'STOP' to end roomba mode: \n").upper()
        if stopCommand == 'STOP':
            status['active'] = False
            break
    mover.join()
    print("Roomba Mode Ended")
'''
def roomba(userRoombaToggle):
    if userRoombaToggle.upper() == 'GO':
        roombaToggle = True
    elif userRoombaToggle.upper() == 'STOP':
        roombaToggle = False
    print("Enter command here:")
    while(roombaToggle):
        innerRoombaInput = input()
        if innerRoombaInput.upper() == 'STOP':
            roombaToggle = False
        distance = finch.getDistance()
        print("distance: ", distance)
        while(distance > 15):
            finch.setMove('F', 15, 50)
            distance = finch.getDistance()
            print("distance: ", distance)
        finch.setTurn('L', 90, 75)
        distance = finch.getDistance()
        
            #finch.setTurn('L', 90, 75)
       
            #finch.setMove('F', 50, 50)
'''
def write(userStr):
    #str = "Hello World"
    if (len(userStr) > 15):
        finch.print("Too Long!")
    elif (len(userStr)< 1):
        finch.print("Too Short!") #wont ever happen 
    else:
        finch.print(userStr)
def makeSquare(length):
    i = 0
    while(i <4):
        finch.setMove('F',length, 75)
        finch.setTurn('R', 90, 75)
        i +=1

def makeStar(length):
    i = 0
    while (i < 5):  
        finch.setMove('F', length, 75)
        finch.setTurn('R',135, 75)
        i+=1
def makeHex(length):
    i = 0
    while(i < 6):
        finch.setMove('F', length, 75)
        finch.setTurn('R', 65, 75)
        i+=1
def makeMary():
    finch.playNote(64, 0.45)
    time.sleep(0.5)
    finch.playNote(62, 0.45)
    time.sleep(0.5)
    finch.playNote(60, 0.45)
    time.sleep(0.5)
    finch.playNote(62, 0.45)
    time.sleep(0.5)
    finch.playNote(64, 0.45)
    time.sleep(0.5)
    finch.playNote(64, 0.45)
    time.sleep(0.5)
    finch.playNote(64, 0.45)
    time.sleep(1.0)
    finch.playNote(62, 0.45)
    time.sleep(0.5)
    finch.playNote(62, 0.45)
    time.sleep(0.5)
    finch.playNote(62, 0.45)
    time.sleep(1.0)
    finch.playNote(64, 0.45)
    time.sleep(0.5)
    finch.playNote(67, 0.45)
    time.sleep(0.5)
    finch.playNote(67, 0.45)
    time.sleep(1.0)
    finch.playNote(64, 0.45)
    time.sleep(0.5)
    finch.playNote(62, 0.45)
    time.sleep(0.5)
    finch.playNote(60, 0.45)
    time.sleep(0.5)
    finch.playNote(62, 0.45)
    time.sleep(0.5)
    finch.playNote(64, 0.45)
    time.sleep(0.5)
    finch.playNote(64, 0.45)
    time.sleep(0.5)
    finch.playNote(64, 0.45)
    time.sleep(0.5)
    finch.playNote(64, 0.45)
    time.sleep(0.5)
    finch.playNote(62, 0.45)
    time.sleep(0.5)
    finch.playNote(62, 0.45)
    time.sleep(0.5)
    finch.playNote(64, 0.45)
    time.sleep(0.5)
    finch.playNote(62, 0.45)
    time.sleep(0.5)
    finch.playNote(60, 0.75)

main()
#makeMary()
#makeSquare(25)
#makeHex(15)
#makeStar(25)
