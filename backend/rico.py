from lib.BirdBrain import Finch
import time
finch = Finch('A')
#finch.setMove('F', 10, 100)
#finch.setTurn('R', 360, 30)
def main(): 
    makeSaints()

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
    
def makeSaints():
    
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
main()
#makeMary()
#makeSquare(25)
#makeHex(15)
#makeStar(25)
