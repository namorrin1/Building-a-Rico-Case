from lib.BirdBrain import Finch
import time
import keyboard
finch = Finch('A')
#finch.setMove('F', 10, 100)
#finch.setTurn('R', 360, 30)
def main(): 
    # roomba()
    move() 
def move() : 

    control = False
    togPres = False
    while True : 

     if keyboard.is_pressed("space") and not togPres :
            control = not control
            togPres = True
            if not control : 
                finch.setMotors(0,0) 
     if not keyboard.is_pressed("space") : 
        if control : 
            if keyboard.is_pressed("w") : #move forward
                finch.setMotors(50,50)
            elif keyboard.is_pressed("s") : #back 
                finch.setMotors(-50,-50) 
            elif keyboard.is_pressed("a") : #left
                finch.setMotors(-30,30)
            elif keyboard.is_pressed("d"): 
                finch.setMotors(30,-30) # right
        else : 
            finch.setMotors(0,0)
        
        time.sleep(0.05)

def roomba():
    distance = 0 
    while (distance >= 15):
        finch.setMove('F',25,50)
        distance == finch.getDistance
def write(str):
    finch.print(str)
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
