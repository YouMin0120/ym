import pygame

pygame.init()

background = pygame.display.set_mode((319 , 524))
pygame.display.set_caption("IMAGE_TEST")

image_test = pygame.image.load("candy1.png")

size_test_width = background.get_size()[0]
size_test_height = image_test.get_size()[1]

play = True
while play:
    background.blit(image_test, [0, 0])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(1)
            print(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
            print("2")
            print(pygame.mouse.get_pos())
pygame.quit()
#