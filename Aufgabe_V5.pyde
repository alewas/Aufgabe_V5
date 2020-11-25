from random import *
import math

a = randint(1, 13)
b = randint(14, 100)
t = True
txt =""

def setup():
    size(1600, 1000)
    global bg
    bg = loadImage("mountain1.jpg")

def draw():
    global y

    background(bg)
    
    xPos = 100
    yPos = 100
    textSize(64)

    fill(0,139,0)
    text("Ist " + str(a) + " Primfaktor von " + str(b) + "? J/N", xPos, yPos)
    text(txt, 300, 310)
    stroke(0, 0, 0)
    strokeWeight(12)
    
    
    circle(483, 867, 60)
    # circle(x-Koordinate, y-Koordinate, Durchmesser)
    point(747, 753)
    point(887, 611)
    point(1033, 467)
    point(1177, 315)
    point(1321, 203)
    point(1445, 47)
       

if a > 1:
    for i in range(2, a//2):
        if (a % i) == 0:
            t = False
            break
        else:
            if (a % b) == 0:
                t = True
            else: t = False
        
def keyPressed():
    global txt
    if (key == "j" and t == True) or (key == "n" and t == False):
        txt = "Richtig"
    else:
        txt = "Falsch"
        
print "hello world"
