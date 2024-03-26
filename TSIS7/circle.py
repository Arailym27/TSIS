import pygame
import sys
pygame.init()
W=1400
H=1050

screen=pygame.display.set_mode((W,H))
pygame.display.set_caption("CIRCLE")

x=W//2
y=H//2
speed=20


clock=pygame.time.Clock()
b=60

white=(255,255,255)
RED=(255,0,0)
pygame.display.flip()
do=True
while do:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            do=False
                  #pygame.time.delay(20)20-миллисекунд продолжительность задержки
                  #ooooorrrr
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - speed >= 0:  # Проверка, чтобы мяч не вышел за левую границу экрана
        x -= speed
    elif keys[pygame.K_RIGHT] and x + speed <= W:  # Проверка, чтобы мяч не вышел за правую границу экрана
        x += speed
    if keys[pygame.K_UP] and y - speed >= 0:  # Проверка, чтобы мяч не вышел за верхнюю границу экрана
        y -= speed
    elif keys[pygame.K_DOWN] and y + speed <= H:  # Проверка, чтобы мяч не вышел за нижнюю границу экрана
        y += speed
   
    screen.fill(white)
    pygame.draw.circle(screen,RED,(x,y),10)       
    clock.tick(b) 
    pygame.display.flip()


