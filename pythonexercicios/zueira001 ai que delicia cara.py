import pygame
pygame.mixer.init()
pygame.mixer.music.load('delicia.mp3')
pygame.mixer.music.play()
pygame.event.wait(input('agora voce escuta ?'))
