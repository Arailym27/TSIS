import pygame
import sys
pygame.init()
W=600
H=400

screen=pygame.display.set_mode((W,H))
pygame.display.set_caption("Mickey's Clock")
pygame.display.set_icon(pygame.image.load("/Users/arajlymkabykenova/Desktop/PP2/1.jpeg"))
x=W//2
y=H//2
speed=3



image_clck=pygame.image.load("clck.jpeg")
clock=pygame.time.Clock()
b=60

white=(255,255,255)
pygame.draw.rect(screen,white,(10,10,50,100),1)


a=(255,0,134)

pygame.draw.lines(screen,a,True,[(200,80),(100,80),(50,70)])
pygame.display.flip()
do=True
while do:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            do=False
                  #pygame.time.delay(20)20-миллисекунд продолжительность задержки
                  #ooooorrrr
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=speed   
    elif keys[pygame.K_RIGHT]:
        x+=speed   
    screen.fill(white)
    pygame.draw.circle(screen,a,(x,y),10)       
    clock.tick(b) 
    pygame.display.flip()


'''
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

'''


