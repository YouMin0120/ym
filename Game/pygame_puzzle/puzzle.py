import pygame
from pygame.locals import *

YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

w, h = 1600, 800
screen = pygame.display.set_mode((w, h))

img = pygame.image.load('candy1.png')
img.convert()

rect = img.get_rect()
rect.center = w // 2, h // 2

running = True
moving = False

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    screen.fill(YELLOW)
    screen.blit(img, rect)

    pygame.draw.rect(screen, BLUE, rect, 2)

    pygame.display.update()

pygame.quit()