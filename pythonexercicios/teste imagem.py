import pygame

pygame.init()

window = pygame.display.set_mode((300, 350))

pygame.display.set_caption(' Ah que delicia cara')

black = (0, 0, 0)

white = (255, 255, 255)

image = pygame.image.load("teste.jpg").convert_alpha()
pygame.mixer.music.load('delicia.mp3')
pygame.mixer.music.play()

gameLoop = True
while gameLoop:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            gameLoop = False

    window.fill(white)

    window.blit(image, (0, 0))

    pygame.display.flip()

pygame.quit()
