#we will develop a demo game here to check if the things are working or not.
#we have to generate a collision detection mechanishm.
from ball import Ball
import pygame
import collisionDtectioni
import lifeIndicator
running=True
pygame.init()
screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
b1=Ball((0,255,0),50,200,200,screen)
b1.setControl(pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN)
b2=Ball((0,0,255),50,100,100,screen)
b2.setControl(pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s)
ballList=[b1,b2]
li=lifeIndicator.LifeIndicators(ballList,0,screen)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            b1.applyKey(event.key)
            b2.applyKey(event.key)
    screen.fill((0,0,0))
    b1.applyFrame()
    b1.applyBoundryCollision()
    b1.drawBall()
    b2.applyFrame()
    b2.applyBoundryCollision()
    if collisionDtectioni.iscolliding(b1,b2):
        collisionDtectioni.applyCollision(b1,b2)
    b2.drawBall()
    if b1.isGameOver() or b2.isGameOver():
        break#lets quit the game.
    li.drawLifeBars()
    pygame.time.delay(73)
    pygame.display.flip()
pygame.quit()