import pygame
pygame.init()
screen=pygame.display.set_mode((1200,600))
Q=12
mario=[0]*Q
for n in range(12):
    mario[n]=pygame.image.load(str(n)+'.png')
    mario[n]=pygame.transform.scale(mario[n],(100,100))
    mario_rect=mario[n].get_rect(center=(450,500))
mario_rect=mario[0].get_rect(center=(450,500))    
pipe_image=pygame.image.load('pipe.png')
pipe_rect=pipe_image.get_rect()
pipe1_image=pygame.image.load('pipe1.png')
pipe1_rect=pipe1_image.get_rect()
bg=pygame.image.load('bg8.png')
delta=0
x,y=450,500
dy=-20
clock=pygame.time.Clock()
jump=False
count=-1
collision,collision1=0,0
Sum,i,delta=0,0,0
k=0
def start():
    global Time,ingame,start_time,Sum_Time,Sum
    mario_rect=mario[0].get_rect(center=(450,500))
    start_image=pygame.image.load('start1.png')
    start_rect=start_image.get_rect(center=(150,250))
    screen.blit(start_image,start_rect)
    if pygame.mouse.get_pressed()[0] == 1:
        start_time = pygame.time.get_ticks()
        Time=0
        Sum_Time=0
        ingame=True
        Sum=0
def times():
    global Time,ingame,start_time,finish_time,Sum
    if ingame  and Time<=finish_time:
        Time= (pygame.time.get_ticks() - start_time)//1000
        text=font.render(str(Time),True,'blue')
        screen.blit(text,(900,50))
        
        text4=font.render('Time in sec=',True,'blue')
        screen.blit(text4,(600,50))
        
    if Time>finish_time:
        text=font.render(str(Time),True,'blue')
        screen.blit(text,(1900,50))
        ingame=False
Sum_Time=0
finish_time=20
Time=0
font=pygame.font.Font(None,70)
ingame=False
while True:
    screen.blit(bg,(0,0))
    count+=1 
    count1=count//3
    count2=count1%Q
    pipe_rect=pipe_image.get_rect(center=((900+i,520)))
    pipe1_rect=pipe1_image.get_rect(center=((900+i,570)))
    collision=pipe_rect.colliderect(mario_rect)
    if collision==0 and k==0:
            screen.blit(pipe_image,pipe_rect)
    if collision==1:
        k=1
    if k==1:
        screen.blit(pipe1_image,pipe1_rect)
    delta=collision-collision1
    if delta==1 and k==1:
        Sum=Sum+1
        print('Sum=',Sum)
    collision1=collision
    if ingame:
        i-=20
        if i<-1000:
            i,k=0,0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    start()
    times()
    if Time>finish_time:
        text2=font.render('Number of collisions=',True,'blue')
        screen.blit(text2,(150,350))
        text3=font.render(str(Sum),True,'blue')
        screen.blit(text3,(700,350))
    keys=pygame.key.get_pressed()
    mario_rect=mario[0].get_rect(center=(x,y))
    if ingame==False:
        screen.blit(mario[0], mario_rect)
    if ingame==True:
        screen.blit(mario[count2], mario_rect)
    if keys[pygame.K_SPACE]:
            jump=True
    if ingame!=True:
        x,y=450,550
    if ingame and jump:
        y=y+dy
        dy+=1
        if y>500:
            jump=False
            dy=-20
    clock.tick(50)
    pygame.display.update()
