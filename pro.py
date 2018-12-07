import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("My Super Game Programming")
icone = pygame.image.load('ball.gif')
pygame.display.set_icon(icone)

screen = pygame.display.set_mode((640, 429))
fond = pygame.image.load('pelouse.png').convert()
screen.blit(fond,(0,0))
#joueur1 = pygame.image.load('joueur.png').convert()
#screen.blit(joueur1, (250, 0))
joueur2 = pygame.image.load('joueur.jpg').convert()
position_joueur2 = joueur2.get_rect()
screen.blit(joueur2, position_joueur2)
pygame.display.flip()

continuer = True
pygame.key.set_repeat(400, 30)

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                position_joueur2 = position_joueur2.move(0, 3)
            if event.key == K_UP:
                position_joueur2 = position_joueur2.move(0, -3)
            if event.key == K_RIGHT:
                position_joueur2 = position_joueur2.move(3, 0)
            if event.key == K_LEFT:
                position_joueur2 = position_joueur2.move(-3, 0)
    screen.blit(fond, (0,0))
    screen.blit(joueur2, position_joueur2)
    pygame.display.flip()
