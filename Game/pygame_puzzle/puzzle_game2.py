import random
import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255 , 255 , 0)

pygame.init()

def game_line():
    pygame.draw.line(screen, BLACK , (80, 0), (80, 400), 5)
    pygame.draw.line(screen, BLACK , (160, 0), (160, 400), 5)
    pygame.draw.line(screen, BLACK , (240, 0), (240, 400), 5)
    pygame.draw.line(screen, BLACK , (320, 0), (320, 400), 5)
    pygame.draw.line(screen, BLACK , (0, 80), (400, 80), 5)
    pygame.draw.line(screen, BLACK , (0, 160), (400, 160), 5)
    pygame.draw.line(screen, BLACK , (0, 240), (400, 240), 5)
    pygame.draw.line(screen, BLACK , (0, 320), (400, 320), 5)


imgFT = pygame.image.load('unnamed.png')
imgS = pygame.image.load('unnamed2.png')
imgT = pygame.image.load('unnamed3.png')
imgF = pygame.image.load('unnamed4.png')
imgFI = pygame.image.load('unnamed5.png')


rect = imgFT.get_rect()
rect = imgS.get_rect()
rect = imgT.get_rect()
rect = imgF.get_rect()
rect = imgFI.get_rect()



w, h = 400 , 400
screen = pygame.display.set_mode((w, h))

blank = []
for i in range(25):
    blank.append(random.randrange(5))

run = True
move = False
while run:
    screen.fill(BLUE)
    game_line()
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                move = True
        elif event.type == MOUSEBUTTONUP:
            move = False
        elif event.type == MOUSEMOTION and move:
            rect.move_ip(event.rel)
        pygame.draw.rect(screen, BLUE, rect, 2)

    blank_num = 0
    y = 20
    for i in range(5):
        x = 10
        for a in range(5):
            if blank[blank_num] == 0:
                screen.blit(imgFT, (x, y))
            elif blank[blank_num] == 1:
                screen.blit(imgS, (x, y))
            elif blank[blank_num] == 2:
                screen.blit(imgT, (x, y))
            elif blank[blank_num] == 3:
                screen.blit(imgF, (x, y))
            elif blank[blank_num] == 4:
                screen.blit(imgFI, (x, y))
            x += 80
            blank_num += 1
        y += 80


    pygame.display.update()