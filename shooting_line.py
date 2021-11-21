import random
import math
from cmu_112_graphics import *
def appStarted(app):
    app.x=100
    app.y=100
    app.angle=0
    app.len=0
    app.timerDelay=3

def drawLine(app,canvas):
    x1=app.x+app.len*math.cos(app.angle)
    y1=app.y+app.len*math.sin(app.angle)
    canvas.create_line(app.x,app.y,x1,y1,fill='blue',width=4)

def mousePressed(app, event):
    app.x=event.x
    app.y=event.y
    app.angle=random.randint(20,70)
    app.len=0
def timerFired(app):
    app.len+=10
    app.len=app.len%600

def redrawAll(app, canvas):
    drawLine(app,canvas)
def shootingLine():
    runApp(width=600, height=600)
shootingLine()