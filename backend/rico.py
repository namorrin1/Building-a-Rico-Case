from lib.BirdBrain import Finch
#import keyboard
import time
finch = Finch('A')
#finch.setMove('F', 10, 100)
#finch.setTurn('R', 360, 30)
def main(): 
    roomba()
    '''
    count = 0
    toggle = True
    while(toggle):
        distance = finch.getDistance()
        print("distance:",distance)
        if (count > 20):
            toggle = False
        count+=1
    ''' 

    '''
    distance = finch.getDistance()
    print("distance: ", distance)
    for i in range (1, 10):
        print("distance: ", distance)
        distance = finch.getDistance() 
    '''

def roomba():
    roombaToggle = True
    while(roombaToggle):
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

def write(str):
    #str = "Hello World"
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
