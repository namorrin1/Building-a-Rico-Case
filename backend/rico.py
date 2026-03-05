from lib.BirdBrain import Finch
import keyboard
import threading 
import time
import keyboard
finch = Finch('A')
#finch.setMove('F', 10, 100)
#finch.setTurn('R', 360, 30)

def main():
    print("Hello. Welcome to the Rico Case: \n")
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
            print("Welcome to Manual Control Mode \n" \
            "Click 'W' to move forward \n" \
            "Click 'A' to turn left \n" \
            "Click 'S' to move backward \n" \
            "Click 'D' to turn right \n")
            move()
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
        singMary()
    elif songChoice.upper() == 'SAINTS':
        singSaints()
    elif songChoice.upper() == 'TWINKLE':
        singTwinkle()

def move() : 
    #this is so that the keys pressed for movement control do not echo in the cmd line after exiting
    keyboard.block_key('w')
    keyboard.block_key('a')
    keyboard.block_key('s')
    keyboard.block_key('d')
    keyboard.block_key('space')
    keyboard.block_key('q')

    control = True # a state to hold whether or not controls are on or off
    togPres = False # a state to determine whether or not the toggle has been pressed(will be space)
    try:    
        while True :
            if keyboard.is_pressed("q"):
                finch.setMotors(0,0)
                print("Exiting Manual Movement Control")
                break 
            if keyboard.is_pressed("space") and not togPres :
                    control = not control #control is off
                    togPres = True #toggle was pressed
                    if not control : 
                        finch.setMotors(0,0) #if control is off then finch should not move
            if not keyboard.is_pressed("space") : 
                togPres = False 
                if control : 
                    if keyboard.is_pressed("w") : #move forward 
                        finch.setMotors(0,0)
                        time.sleep(0.10)   
                        finch.setMotors(25,25)
                    elif keyboard.is_pressed("s") : #back
                        finch.setMotors(0,0)
                        time.sleep(0.10)
                        finch.setMotors(-25,-25) 
                    elif keyboard.is_pressed("a") : #left
                        finch.setMotors(-30,30)
                    elif keyboard.is_pressed("d"): 
                        finch.setMotors(30,-30) # right
                else : 
                    finch.setMotors(0,0) # stops if no input is being handled
                
            time.sleep(0.05) # use sleep to not overload bot.
    finally:    #unblocks the keys after blocking them so they dont echo in the cmd line. 
        for key in ['w', 'a', 's', 'd', 'space', 'q']:
            try:
                keyboard.unblock_key(key)
            except:
                pass
        finch.setMotors(0,0)
        finch.stop()
#rafbranch ^ 
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
        finch.setTurn('R',144, 75)
        i+=1
def makeHex(length):
    i = 0
    while(i < 6):
        finch.setMove('F', length, 75)
        finch.setTurn('R', 65, 75)
        i+=1
def singMary():
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
def singSaints():   
    # Phrase 1
    finch.playNote(60, 0.50)
    time.sleep(0.5)
    finch.playNote(64, 0.50)
    time.sleep(0.5)
    finch.playNote(65, 0.50)
    time.sleep(0.5)
    finch.playNote(67, .8)
    time.sleep(1)
    finch.playNote(60, 0.50)
    time.sleep(0.5)
    finch.playNote(64, 0.50)
    time.sleep(0.5)
    finch.playNote(65, 0.50)
    time.sleep(0.5)
    finch.playNote(67, 0.80)
    time.sleep(1)
    # Phrase 2
    finch.playNote(60, 0.50)
    time.sleep(0.5)
    finch.playNote(64, 0.50)
    time.sleep(0.5)
    finch.playNote(65, 0.50)
    time.sleep(0.5)
    finch.playNote(67, 0.8)
    time.sleep(1)
    finch.playNote(64, 0.8)
    time.sleep(1)
    finch.playNote(60, 0.8)
    time.sleep(1)
    finch.playNote(64, 0.8)
    time.sleep(1)
    finch.playNote(62, 0.8)
    time.sleep(1.5)
    # Phrase 3
    finch.playNote(64, 0.5)
    time.sleep(0.6)
    finch.playNote(64, 0.5)
    time.sleep(0.5)
    finch.playNote(62, 0.5)
    time.sleep(0.5)
    finch.playNote(60, .8)
    time.sleep(1)
    finch.playNote(60, 0.5)
    time.sleep(0.5)
    finch.playNote(64, 0.8)
    time.sleep(1)
    finch.playNote(67, 0.5)
    time.sleep(0.6)
    finch.playNote(67, 0.5)
    time.sleep(0.5)
    finch.playNote(65, 0.8)
    time.sleep(1)
    # Phrase 4
    finch.playNote(60, 0.5)
    time.sleep(0.5)
    finch.playNote(64, 0.5)
    time.sleep(0.5)
    finch.playNote(65, 0.5)
    time.sleep(0.5)
    finch.playNote(67, 0.8)
    time.sleep(1)
    finch.playNote(64, 0.8)
    time.sleep(1)
    finch.playNote(60, 0.8)
    time.sleep(1)
    finch.playNote(62, 0.8)
    time.sleep(1)
    finch.playNote(60, 1)
    time.sleep(1)
def singTwinkle():
    finch.playNote(60, 0.5)
    time.sleep(.6)
    finch.playNote(60, 0.5)
    time.sleep(.5)
    finch.playNote(67, 0.5)
    time.sleep(.6)
    finch.playNote(67, 0.5)
    time.sleep(.5)
    finch.playNote(69, 0.5)
    time.sleep(.6)
    finch.playNote(69, 0.5)
    time.sleep(.5)
    finch.playNote(67, 0.8)
    time.sleep(1)
    finch.playNote(65, 0.5)
    time.sleep(.6)
    finch.playNote(65, 0.5)
    time.sleep(.5)
    finch.playNote(64, 0.5)
    time.sleep(.6)
    finch.playNote(64, 0.5)
    time.sleep(.5)
    finch.playNote(62, 0.5)
    time.sleep(.6)
    finch.playNote(62, 0.5)
    time.sleep(.5)
    finch.playNote(60, 0.8)
    time.sleep(1)
    finch.playNote(67, 0.5)
    time.sleep(.6)
    finch.playNote(67, 0.5)
    time.sleep(.5)
    finch.playNote(65, 0.5)
    time.sleep(.6)
    finch.playNote(65, 0.5)
    time.sleep(.5)
    finch.playNote(64, 0.5)
    time.sleep(.6)
    finch.playNote(64, 0.5)
    time.sleep(.5)
    finch.playNote(62, 0.8)
    time.sleep(1)
    finch.playNote(67, 0.5)
    time.sleep(.6)
    finch.playNote(67, 0.5)
    time.sleep(.5)
    finch.playNote(65, 0.5)
    time.sleep(.6)
    finch.playNote(65, 0.5)
    time.sleep(.5)
    finch.playNote(64, 0.5)
    time.sleep(.6)
    finch.playNote(64, 0.5)
    time.sleep(.5)
    finch.playNote(62, 0.8)
    time.sleep(1)
    finch.playNote(60, 0.5)
    time.sleep(.6)
    finch.playNote(60, 0.5)
    time.sleep(.5)
    finch.playNote(67, 0.5)
    time.sleep(.6)
    finch.playNote(67, 0.5)
    time.sleep(.5)
    finch.playNote(69, 0.5)
    time.sleep(.6)
    finch.playNote(69, 0.5)
    time.sleep(.5)
    finch.playNote(67, 0.8)
    time.sleep(1)
    finch.playNote(65, 0.5)
    time.sleep(.6)
    finch.playNote(65, 0.5)
    time.sleep(.5)
    finch.playNote(64, 0.5)
    time.sleep(.6)
    finch.playNote(64, 0.5)
    time.sleep(.5)
    finch.playNote(62, 0.5)
    time.sleep(.6)
    finch.playNote(62, 0.5)
    time.sleep(.5)
    finch.playNote(60, 1)
    time.sleep(1)

main()

