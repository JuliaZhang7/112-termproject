#in this version, try to use object for both bricks and ball
#in every bounce, the energy is losed..and it end up sliding..
#every bounce is weaker than before
#fix the problem of dropping
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
    app.bricks=[]#hold bricks object
    app.ballmode=True
    app.linemode=False
    app.timerDelay =20
    app.lineDic=dict()#one ball connect one dot, a dot connect multiple, ball key
    app.gravity=0.3#the acceleration always point down, it's 4 for debugging porpuse
    app.timepass=0#set this to keep track of time
    app.board=[(100,100),(300,300),(300,500)]
    app.buttonlist=[]
    #app.boardList=[(app.board.cor1X,app.board.cor1Y),(app.board.cor2X,app.board.cor2Y)]
#this check if the range expressed with two tuples have over lap
def checkInRange(firstTuple,secTuple):
    farest=max(secTuple[1],firstTuple[1])
    cloest=min(secTuple[0],firstTuple[0])
    distance=abs(farest-cloest)
    rangeOfFir=abs(firstTuple[1]-firstTuple[0])
    rangeOfSec=abs(secTuple[1]-secTuple[0])
    return distance<=rangeOfFir+rangeOfSec
def getRangeIndeption(firstTuple,secTuple):
    farest=max(secTuple[1],firstTuple[1])
    cloest=min(secTuple[0],firstTuple[0])
    rangeOfFir=abs(firstTuple[1]-firstTuple[0])
    rangeOfSec=abs(secTuple[1]-secTuple[0])
    return (rangeOfFir+rangeOfSec)-(farest-cloest)
class Ball(object):
    def __init__(self, radius, cx,cy):
        self. r=radius
        self.cx=cx
        self.cy=cy
        self.time=0
        self.mass=5#(4/3)*math.pi*(self.r/30)**3(later i will compute this)
        self.forcey=0#the force that was on the y direction
        self.forcex=0
        self.dx=0
        self.dy=0
        self.hasbounced=0#this check how many times a ball bonced
    def __repr__(self):
        return f'a ball centered at {self.cx,self.cy}, its r is{self.r})'
    def ballSlide(self,brick):
        coefficient=1/brick.slope
        cos=coefficient/(math.sqrt(1+coefficient**2))
        sin=1/(math.sqrt(1+coefficient**2))
    
        tan=sin/cos
        self.time=0
        #ball.dy-=(((ball.time)/60)*app.gravity)+100
        self.dy=tan*(sin*(self.mass*0.3*3))#((1/brick.slope)*(ball.mass*app.gravity*3))
        if brick.slope<0:
            self.dx=(-self.dy/(sin/cos))
            #print('x',self.dx,'y',self.dy)
        else:
            self.dx=self.dy/(sin/cos)+1
            #print('x',self.dx,'y',self.dy)
#a button object with each on or off, all button off at first, with cx,cy
#a board which takes a list of button
class Button(object):
    def __init__(self,cx,cy):
        self.cx=cx
        self.cy=cy
        self.press=False
        self.color='pink'
        self.r=10
    def __repr__(self):
        return f'button centered at {self.cx,self.cy}, pressed?{self.press})'
class Board(object):#the board to solve, hard coded
    def __init__(self,listofButton):#both tuple
        self.buttonList=listofButton


class Brick(object):
    def __init__(self, start, end):
        self.start=start
        self.end=end
        self.slope=(self.end[1]-self.start[1])/(self.end[0]-self.start[0])
        self.mass=1000000000
    def __repr__(self):
        return f'a brick with start: {self.start}, end:{self.end})'
    def getYrange(self,xrange):#this xrange is a tuple of x range for a given ball!
        point1=xrange[0]
        point2=xrange[1]#p1,p2,p3,p4 is four dot on brick by cutting verticly by bounds
        changeOnY=self.end[1]-self.start[1]
        point1Online=self.start[1]+(((point1-self.start[0]))/((self.end[0]-self.start[0]))*changeOnY)
        point2Online=self.start[1]+((point2-self.start[0])/((self.end[0]-self.start[0]))*changeOnY)
        higherPoint=max(point1Online,point2Online)#the slope can be + or -
        lowerPoint=min(point1Online,point2Online)
        #print('higher:',higherPoint,'lower',lowerPoint)
        lenOfLine=math.sqrt((self.end[0]-self.start[0])**2+(self.end[1]-self.start[1])**2)
        verticleChange=(self.end[0]-self.start[0])*8/(lenOfLine)
        return (lowerPoint-verticleChange,higherPoint+verticleChange)
    def getXrange(self):#get the x range of a brick
        lenOfLine=math.sqrt((self.end[0]-self.start[0])**2+(self.end[1]-self.start[1])**2)
        changeInX=(self.end[1]-self.start[1])*6/(lenOfLine+0.01)
        return (self.start[0]-changeInX,self.end[0]+changeInX)

def createBoard(app,coor1,coor2):
    for button in app.board:
        print(button)
        b=Button(button[0],button[1])
        
        app.buttonlist.append(b)
        print(app.buttonlist)
def drawBoard(app,canvas):
    for button in app.buttonlist:
        print(button)
        b=Button(button[0],button[1])
        
        app.buttonlist.append(b)
        print(app.buttonlist)
        drawbutton(button,canvas)

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
        appendBrick(app)
    else:
        app.balls.append((event.x,event.y))
        appendBall(app)#check if it can add ball
        app.ball=[]

#if we are colliding
#set the dy to 0, minus the normal force to it 
#don;t let grafity affect! i hard code this ,QAQ
def balltoBrickSlide(app,ball,brick):
    print('slifing')
    coefficient=1/brick.slope
    cos=coefficient/(math.sqrt(1+coefficient**2))
    sin=1/(math.sqrt(1+coefficient**2))
    
    tan=sin/cos
    ball.time=0
    #ball.dy-=(((ball.time)/60)*app.gravity)+100
    ball.dy=tan*(sin*(ball.mass*app.gravity*3))
    ball.forcey=0#((1/brick.slope)*(ball.mass*app.gravity*3))
    '''if brick.slope<0:
        ball.dx=(-ball.dy/(sin/cos))
        print('x',ball.dx,'y',ball.dy)
    else:
        ball.dx=ball.dy/(sin/cos)
        print('x',ball.dx,'y',ball.dy)'''
    #ball.dy-=((app.timepass/60)*app.gravity)
#u know, the thing is, the lower it gets, the faster it is
#to solve, let dx responde to dy
def balltoBrickBounce(app,ball,brick):
    coefficient=1/brick.slope
    cos=coefficient/(math.sqrt(1+coefficient**2))
    sin=1/(math.sqrt(1+coefficient**2))
    
    ball.hasbounced+=1
    '''if (ball.mass*app.gravity*3)/(ball.hasbounced)>4:
        ball.dy=(-ball.mass*app.gravity*1.5)/(ball.hasbounced)
        ball.dx=(-ball.dy/(cos/sin))'''
    #slding
        #balltoBrickSlide(app,ball,brick)
    if ball.cx<brick.end[0]:
        #print('x related ',sin,'y relates',cos)
        if brick.slope<0:
            ball.forcex=-sin*app.gravity*ball.mass
            ball.forcey=app.gravity-cos*app.gravity*ball.mass
        else:
            ball.forcex=sin*app.gravity*ball.mass
            ball.forcey=(app.gravity-cos*app.gravity*ball.mass)
            #ball.cy+=1
def balltoBrickColli(app):
    #print('runnning collision check')
    for ball in app.ballsreal:
        
        ballxrange=(ball.cx-ball.r,ball.cx+ball.r)
        ballyrange=(ball.cy-ball.r,ball.cy+ball.r)
        for brick in app.bricks:
            brickXrange=brick.getXrange()
            brickYrange=brick.getYrange(ballxrange)
            if checkInRange(ballxrange,brickXrange) and checkInRange(ballyrange,brickYrange):
                #print(ball.mass*app.gravity)
                #ball.dy=-ball.mass*app.gravity*3
                #ball.dx=brick.slope*(ball.mass*app.gravity)
                indeptionX=getRangeIndeption(ballxrange,brickXrange)
                indeptionY=getRangeIndeption(ballyrange,brickYrange)
                #print('indeption',indeptionX,indeptionY)
                #ball.cy-=indeptionY
                ball.dy=0
                #ball.dx=0
                ball.ballSlide(brick)
                #balltoBrickBounce(app,ball,brick)s
                return True
            else:
                ball.forcey=app.gravity*ball.mass
                ball.forcex=0
def drawboardLine(app,canvas):
    #print(app.lineDic)
    for ball in app.lineDic:
        ballx=ball.cx
        bally=ball.cy
        boardx=app.lineDic[ball][0]
        boardy=app.lineDic[ball][1]
        if 0<ballx<app.width and 0<bally<app.height:
            canvas.create_line(ballx,bally,boardx,boardy,fill='blue',width=4)
    #if app.board.color
def balltoBoardColli(app):
    for ball in app.ballsreal:
        for boardTuple in app.boardList:
            if boardTuple[0]-app.board.boardR<ball.cx<boardTuple[0]+app.board.boardR:
                if boardTuple[1]-app.board.boardR<ball.cy<boardTuple[1]+app.board.boardR:#finish collision checking
                    print('hell yeahhhhhhhhhhh!!!!!!!!')
                    app.lineDic[ball]=boardTuple
                    if app.boardList.index(boardTuple)==0:#we touch the 0 board
                        app.board.color1='blue'
                        #draw line
                    else:
                        app.board.color2='blue'
                else:
                    app.board.color1='pink'
                    app.board.color2='pink'
def appendBall(app):
    if len(app.balls)<2:
        pass
    else:
        tuplecenter=app.balls[::-1][1]
        tupler=app.balls[::-1][0]
        x1=tuplecenter[0]
        y1=tuplecenter[1]
        x2=tupler[0]
        y2=tupler[1]
        r=math.sqrt((x2-x1)**2+(y2-y1)**2)
        ball=Ball(r,x1,y1)
        ball.forcey=app.gravity*ball.mass
        app.ballsreal.append(ball)
def mouseDragged(app, event):
    if app.linemode:
        app.line.append((event.x,event.y))
    else:
        app.ball.append((event.x,event.y))
def moveBalls(app):#this can make everyball move accroding t their dx dy
    for ball in app.ballsreal:
        ball.dy+=ball.forcey/ball.mass
        ball.dx+=ball.forcex/ball.mass
        #print(ball.forcey)
        ball.cx+=ball.dx
        ball.cy+=ball.dy
def timerFired(app):
    moveBalls(app)
    balltoBrickColli(app)
    balltoBoardColli(app)
    for ball in app.ballsreal:
        ball.time+=1
def createBrick(app,canvas):#black lines that are unchangable
    #print(app.lines)
    for brick in app.bricks:
        start=brick.start
        end=brick.end
        x1=start[0]
        y1=start[1]
        x2=end[0]
        y2=end[1]
        lenOfSide=math.sqrt((x2-x1)**2+(y2-y1)**2)
        changeInX=(y2-y1)*8/(lenOfSide+0.01)#0.01 to solve for /0 situation
        changeInY=(x2-x1)*8/(lenOfSide+0.01)#the change in Y 
        canvas.create_polygon(x1-changeInX,y1+changeInY,x2-changeInX,y2+changeInY,
            x2+changeInX,y2-changeInY,x1+changeInX,y1-changeInY,fill='grey',width=3)

def drawCollisionCheck(app,canvas):
    if balltoBrickColli(app):
        canvas.create_text(app.width/2, app.height/2+40,
                            text='holy moly!',
                            font='Arial 20 bold')

def drawbutton(button,canvas):
    x1=button.cx
    y1=button.cy
    r=button.r
    canvas.create_oval(x1-r,y1-r,x1+r,y1+r,fill='white',width=3)
    print('drawing a button')
    canvas.create_oval(x1-6,y1-6,x1+6,y1+6,fill=button.color,width=3)

def drawline(app,canvas):#temprary
    if len(app.line)==0:
        pass
    else:
        x1=app.line[0][0]
        y1=app.line[0][1]
        x2=app.line[len(app.line)-1][0]
        y2=app.line[len(app.line)-1][1]
        lenOfSide=math.sqrt((x2-x1)**2+(y2-y1)**2)
        changeInX=(y2-y1)*8/(lenOfSide+0.01)#0.01 to solve for /0 situation
        changeInY=(x2-x1)*8/(lenOfSide+0.01)#the change in Y 
        canvas.create_polygon(x1-changeInX,y1+changeInY,x2-changeInX,y2+changeInY,
        x2+changeInX,y2-changeInY,x1+changeInX,y1-changeInY,fill='pink',width=3)
def appendBrick(app):
    if len(app.lines)<2:
        pass
    else:
        tupleStart=app.lines[::-1][1]
        tupleEnd=app.lines[::-1][0]
        brick=Brick(tupleStart,tupleEnd)
        app.bricks.append(brick)
        print(brick)
def drawcircle(app,canvas):#temperary
    if len(app.ball)==0:
        pass
    else:
        x1=app.ball[0][0]
        y1=app.ball[0][1]
        x2=app.ball[len(app.ball)-1][0]
        y2=app.ball[len(app.ball)-1][1]
        r=math.sqrt((x2-x1)**2+(y2-y1)**2)
        canvas.create_oval(x1-r,y1-r,x1+r,y1+r,fill='white',width=3)
#draw them from ballsreal
def createcircle(app,canvas):
    for ball in app.ballsreal:
        centerx=ball.cx
        centery=ball.cy
        radius=ball.r
        canvas.create_oval(centerx-radius,centery-radius,
                    centerx+radius,centery+radius,fill='pink',width=3)

def redrawAll(app, canvas):
    font = 'Arial 20 bold'
    #canvas.create_text(app.width/2,  30, text='Events Demo', font=font)
    if app.linemode:
        drawline(app,canvas)
    elif app.ballmode:
        drawcircle(app,canvas)
    
    createBrick(app,canvas)
    createcircle(app,canvas)
    drawboardLine(app,canvas)
    drawBoard(app,canvas)
    drawCollisionCheck(app,canvas)
    n = min(10, len(app.messages))
    i0 = len(app.messages)-n
    
    canvas.create_text(app.width/2, app.height/2,
                           text='click f to switch mode',
                           font=font)

def runfragmentViewer():
    print('drag to create ball and brick!')
    runApp(width=600, height=600)

runfragmentViewer()
