"""
Hintergrundbild
"""

y = 0

def setup():
    size(1600, 1000)
    # Das Hintergrundbild muss die gleiche Anzahl Pixel, wie das definierte Fenster haben
    # Hintergrundbild muss mit der richtigen Anzahl Pixel bereits abgespeichert sein.
    # 1600 x 1000 pixel
    global bg
    bg = loadImage("mountain1.jpg")


def draw():
    global y

    background(bg)
