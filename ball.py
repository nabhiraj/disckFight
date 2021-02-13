import pygame
#ball should have the functionality of assigniging control
#there will be a dis
class Ball:
    def __init__(self,clr,siz,init_x,init_y,ms):
        self.color=clr
        self.siz=siz
        self.x=init_x
        self.y=init_y
        self.myScreen=ms
        self.vel_x=10
        self.vel_y=10
        self.width=ms.get_width()
        self.height=ms.get_height() 
        print('the height and width is ')
        print((self.height,self.width))
        self.life=100
    
    def getClr(self):
        return self.color
    def getLife(self):
        return self.life

    def isGameOver(self):
        if self.life<=0:
            return True
        else:
            return False

    def getLocation(self):
        return (self.x,self.y)

    def getVelocity(self):
        return (self.vel_x,self.vel_y)
    
    def getBallSize(self):
        return self.siz

    def setControl(self,left,right,up,down):#this defines the type of control key which this ball uses
        self.ControlDict={}
        self.ControlDict['left']=left
        self.ControlDict['right']=right
        self.ControlDict['up']=up
        self.ControlDict['down']=down

    def isKeyApplicable(self,k):#may not be used right now.
        if k in self.ControlDict.values():
            return True
        else:
            return False
    
    def applyKey(self,k):
        if self.ControlDict['left']==k:
            self.decVelX()
        if self.ControlDict['right']==k:
            self.incVelX()
        if self.ControlDict['up']==k:
            self.decVely()
        if self.ControlDict['down']==k:
            self.incVelY()
            
    def applyFrame(self):
        self.x+=self.vel_x
        self.y+=self.vel_y

    def drawBall(self):#pygame dependent code
        pygame.draw.circle(self.myScreen,self.color,(self.x,self.y),self.siz)

    def incVelX(self):
        self.vel_x+=5

    def incVelY(self):
        self.vel_y+=5

    def decVelX(self):
        self.vel_x-=5
    
    def decVely(self):
        self.vel_y-=5

    def isTopLimit(self):
        if self.y<=0:
            return True
        else:
            return False

    def isBottomLimit(self):
        if self.y>=self.height:
            return True
        else:
            return False

    def isRightLimit(self):
        if self.x>=self.width:
            return True
        else:
            return False

    def isLeftLimit(self):
        if self.x<=0:
            return True
        else:
            return False

    def applyBoundryCollision(self):
        if self.isTopLimit() or self.isBottomLimit():
            self.vel_y*=-1
            self.life-=5
        if self.isRightLimit() or self.isLeftLimit():
            self.vel_x*=-1
            self.life-=5