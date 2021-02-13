import pygame
pygame.init()
screen = pygame.display.set_mode([500,500]) 
running=True
x=250
y=100
vel_x=10
vel_y=10
while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    vel_y-=5
                if event.key==pygame.K_DOWN:
                    vel_y+=5
                if event.key==pygame.K_RIGHT:
                    vel_x+=5
                if event.key==pygame.K_LEFT:
                    vel_x-=5
        x+=vel_x
        y+=vel_y
        if x>=500 or x<=0:
            vel_x=vel_x*-1
        if y>=500 or y<0:
            vel_y=vel_y*-1
        screen.fill((255,255,255))
        pygame.draw.circle(screen,(0,0,155),(x,y),34)
        pygame.time.delay(68)
        pygame.display.flip()
pygame.quit()