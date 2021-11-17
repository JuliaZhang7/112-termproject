from cmu_112_graphics import *
import math, copy, os
def appStarted(app):
    app.level=0
    app.messages = ['appStarted']
    app.line=[]
    app.lines=[]
    app.ball=[]
    app.balls=[]
    app.ballsreal=[]#hold ball object
    app.ballmode=True
    app.linemode=False

class Ball(object):
    def __init__(self, radius, cx,cy):
        self. r=radius
        self.cx=cx
        self.cy=cy
        self.mass=(4/3)*math.pi*self.r**3
        self.dx=0
        self.dy=0
    def __repr__(self):
        return f'a ball centered at {self.cx,self.cy}, its r is{self.r})'

def keyPressed(app, event):
    if (event.key == 'f'):
        app.ballmode=not app.ballmode
        app.linemode=not app.linemode
def mousePressed(app, event):
    if app.linemode:
        app.line=[]
        app.lines.append((event.x,event.y))
    else:#ball mode
        app.ball=[]
        app.balls.append((event.x,event.y))
    app.messages.append(f'mousePressed at {(event.x, event.y)}')
def mouseReleased(app, event):
    app.messages.append(f'mouseReleased at {(event.x, event.y)}')
    if app.linemode:
        app.lines.append((event.x,event.y))
    else:
        app.balls.append((event.x,event.y))
        
def appendBall(app):
    #print(app.balls)
    if len(app.balls)%2==1:#this ensure every time there is complete drag
            for xy in range (0,len(app.balls)-1,2):
                x1=app.balls[xy][0]
                y1=app.balls[xy][1]
                x2=app.balls[xy+1][0]
                y2=app.balls[xy+1][1]
                r=math.sqrt((x2-x1)**2+(y2-y1)**2)
                ball=Ball(r,x1,y1)
                app.ballsreal.append(ball)
    else:
            for xy in range (0,len(app.lines)-1,2):
                x1=app.lines[xy][0]
                y1=app.lines[xy][1]
                x2=app.lines[xy+1][0]
                y2=app.lines[xy+1][1]
                r=math.sqrt((x2-x1)**2+(y2-y1)**2)
                ball=Ball(r,x1,y1)
                app.ballsreal.append(ball)
def mouseDragged(app, event):
    if app.linemode:
        app.line.append((event.x,event.y))
    else:
        app.ball.append((event.x,event.y))
        
def createline(app,canvas):#black lines that are unchangable
    if len(app.lines)<2:
        pass
    elif len(app.lines)%2==0:#this ensure every time there is complete drag
        for xy in range (0,len(app.lines),2):
            x1=app.lines[xy][0]
            y1=app.lines[xy][1]
            x2=app.lines[xy+1][0]
            y2=app.lines[xy+1][1]
            canvas.create_line(x1,y1,x2,y2,fill='black',width=4)
    else:
        for xy in range (0,len(app.lines)-1,2):
            x1=app.lines[xy][0]
            y1=app.lines[xy][1]
            x2=app.lines[xy+1][0]
            y2=app.lines[xy+1][1]
            canvas.create_line(x1,y1,x2,y2,fill='black',width=4)


def drawline(app,canvas):#temprary
    if len(app.line)==0:
        pass
    else:
        x1=app.line[0][0]
        y1=app.line[0][1]
        x2=app.line[len(app.line)-1][0]
        y2=app.line[len(app.line)-1][1]
        canvas.create_line(x1,y1,x2,y2,fill='pink',width=3)
def drawcircle(app,canvas):#temperary
    #print(app.ballsreal)
    if len(app.ball)==0:
        pass
    else:
        x1=app.ball[0][0]
        y1=app.ball[0][1]
        x2=app.ball[len(app.ball)-1][0]
        y2=app.ball[len(app.ball)-1][1]
        r=math.sqrt((x2-x1)**2+(y2-y1)**2)
        canvas.create_oval(x1-r,y1-r,x1+r,y1+r,fill='white',width=3)
def createcircle(app,canvas):#pink circle that are unchangable
    if len(app.balls)<2:
        pass
    elif len(app.balls)%2==0:#this ensure every time there is complete drag
        for xy in range (0,len(app.balls),2):
            x1=app.balls[xy][0]
            y1=app.balls[xy][1]
            x2=app.balls[xy+1][0]
            y2=app.balls[xy+1][1]
            r=math.sqrt((x2-x1)**2+(y2-y1)**2)
            ball=Ball(r,x1,y1)
            #app.ballsreal.append(ball)
            canvas.create_oval(x1-r,y1-r,x1+r,y1+r,fill='pink',width=3)
    else:
        for xy in range (0,len(app.balls)-1,2):
            x1=app.balls[xy][0]
            y1=app.balls[xy][1]
            x2=app.balls[xy+1][0]
            y2=app.balls[xy+1][1]
            r=math.sqrt((x2-x1)**2+(y2-y1)**2)
            ball=Ball(r,x1,y1)
            #app.ballsreal.append(ball)
            canvas.create_oval(x1-r,y1-r,x1+r,y1+r,fill='pink',width=3)
    #print(app.ballsreal)
    '''if len(app.ballsreal)<1:
        pass
    else:#this ensure every time there is complete drag
        for ball in app.ballsreal:
            x1=ball.cx
            y1=ball.cy
            r=ball.r
            canvas.create_oval(x1-r,y1-r,x1+r,y1+r,fill='pink',width=3)
    else:
        for xy in range (0,len(app.balls)-1,2):
            x1=app.balls[xy][0]
            y1=app.balls[xy][1]
            x2=app.balls[xy+1][0]
            y2=app.balls[xy+1][1]
            r=math.sqrt((x2-x1)**2+(y2-y1)**2)
            canvas.create_oval(x1-r,y1-r,x1+r,y1+r,fill='pink',width=3)'''


def redrawAll(app, canvas):
    font = 'Arial 20 bold'
    #canvas.create_text(app.width/2,  30, text='Events Demo', font=font)
    if app.linemode:
        drawline(app,canvas)
    elif app.ballmode:
        drawcircle(app,canvas)
    canvas.create_polygon(50,100,150,100,150,300,50,300,fill='pink')
    createline(app,canvas)
    createcircle(app,canvas)
    n = min(10, len(app.messages))
    i0 = len(app.messages)-n
    '''for i in range(i0, len(app.messages)):
        canvas.create_text(app.width/2, 100+50*(i-i0),
                           text=f'#{i}: {app.messages[i]}',
                           font=font)'''
    # canvas.create_text(app.width/2, app.height/2,
    #                    text='Draw your Freddy Fractal here!',
    #                    font='Arial 24 bold')

def runFreddyFractalViewer():
    print('Running Freddy Fractal Viewer!')
    runApp(width=700, height=700)

runFreddyFractalViewer()
