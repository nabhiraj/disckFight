from ball import Ball
#we have only created collision detection for the two balls.
#will the help of this two ball collision detection multiple ball collision detection can be formed.
def getDis(p1,p2):
    x1=p1[0]
    y1=p1[1]
    x2=p2[0]
    y2=p2[1]
    return ((y2-y1)**2+(x2-x1)**2)**0.5

def speedScore(ball):
    v=ball.getVelocity()
    return (v[0]**2 +v[1]**2)

def iscolliding(b1,b2):
    pos1=b1.getLocation()
    pos2=b2.getLocation()
    dis=getDis(pos1,pos2)#impliment this.
    if dis<=b1.getBallSize()+b2.getBallSize():
        return True
    else:
        return False

#now lets thing about applying the collision.
def applyCollision(b1,b2):#assuming that there is a collision.
    #if two velocity are same they will remain unchange.
    #if two velocity are opposite they will opposite in reverse direction.
    vel_1=b1.getVelocity()
    vel_1_x=vel_1[0]
    vel_1_y=vel_1[1]
    vel_2=b2.getVelocity()
    vel_2_x=vel_2[0]
    vel_2_y=vel_2[1]
    flag=True 
    if vel_1_x*vel_2_x<=0:
        vel_1_x*=-1
        vel_2_x*=-1
        flag=False
    if vel_1_y*vel_2_y<=0:
        vel_1_y*=-1
        vel_2_y*=-1
        flag=False

    if flag:
        if speedScore(b1)<=speedScore(b2):
            vel_1_x*=-1
            vel_1_y*=-1
        else:
            vel_2_x*=-1
            vel_2_y*=-1



    b1.vel_x=vel_1_x
    b1.vel_y=vel_1_y
    b2.vel_x=vel_2_x
    b2.vel_y=vel_2_y
    #all changes are done.
    #now we have to do the calculation of file
    if speedScore(b1)>speedScore(b2):
        b2.life-=3
        b2.siz-=1
    elif speedScore(b1)<speedScore(b2):
        b1.life-=3
        b1.siz-=1
        
        

    


