import random
import math
from cmu_112_graphics import *
def appStarted(app):
    app.length=20
    app.timerDelay=10
    app.angle=0
    app.centerx=app.width/2
    app.centery=app.height/2
    app.radius=[10,15,17,15,16,21]
    app.ballcenterx=300
    app.ballcentery=300
    app.t=0

def changeAngle(app):
    
    app.angle+=0.01
def drawLine(app,canvas,x,y):
    if app.angle<3:
        print(app.angle)
        x1=x-app.length*math.cos(app.angle)
        y1=y+app.length*math.sin(app.angle)
        x2=x+app.length*math.cos(app.angle)
        y2=y-app.length*math.sin(app.angle)
        lenOfSide=30#math.sqrt((x2-x1)**2+(y2-y1)**2)
        changeInX=(y2-y1)*app.length/(lenOfSide)
        changeInY=(x2-x1)*app.length/(lenOfSide)
        canvas.create_polygon(x1-changeInX,y1+changeInY,x2-changeInX,y2+changeInY,
                x2+changeInX,y2-changeInY,x1+changeInX,y1-changeInY,width=4,fill='white',outline='pink')
    
def drawBall(app,canvas):
    x=app.ballcenterx+5*app.t
    x1=app.ballcenterx-3*app.t
    x2=app.ballcenterx+7*app.t
    y1=app.ballcentery+(((math.sqrt(50)+1)-1*app.t)**2-50)
    y2=app.ballcentery+(((math.sqrt(80)+1)-1*app.t)**2-80)
    y3=app.ballcentery+(((math.sqrt(100)+1)-1*app.t)**2-100)
    y4=app.ballcentery+(((math.sqrt(120)+1)-1*app.t)**2-120)
    canvas.create_oval(x-app.radius[0],y1-app.radius[0],x+app.radius[0],y1+app.radius[0],fill='white',width=2)
    canvas.create_oval(x-app.radius[1],y2-app.radius[1],x+app.radius[1],y2+app.radius[1],fill='white',width=2)
    canvas.create_oval(x1-app.radius[0],y1-app.radius[0],x1+app.radius[0],y1+app.radius[0],fill='white',width=2)
    canvas.create_oval(x1-app.radius[3],y3-app.radius[3],x1+app.radius[3],y3+app.radius[3],fill='white',width=2)
    canvas.create_oval(x2-app.radius[3],y4-app.radius[3],x2+app.radius[3],y4+app.radius[3],fill='white',width=2)
def mousePressed(app, event):
    app.ballcenterx=event.x
    app.ballcentery=event.y
    
    print('changed!')
def timerFired(app):
    changeAngle(app)
    app.t+=1
    app.t=app.t%40

def redrawAll(app, canvas,):
    #drawBall(app,canvas)
    drawLine(app,canvas,300,400)
def rotatingRectangle():
    runApp(width=600, height=600)
rotatingRectangle()