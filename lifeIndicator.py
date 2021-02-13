#in this file we will write the code for the indicator of a perticular ball.
import pygame
class LifeIndicators:
    def __init__(self,bl,yloc,ms):
        self.ballList=bl
        self.yloc=yloc
        self.ms=ms
    
    def drawLifeBars(self):
        count=self.yloc
        for ball in self.ballList:
            ballLife=ball.getLife()
            ballColor=ball.getClr()
            #now we need to figure out how to draw the rectangel.
            pygame.draw.rect(self.ms,ballColor, pygame.Rect(0,count,ballLife,25))
            count+=30     

            
    
        
