import sys
import pygame
import random
import socket
from pygame.locals import *


pygame.init()

window_width=963
window_height=542
white = (216,216,216)
black = (39, 39, 39)

size = (window_width, window_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Whist")



def display():
    page = pygame.image.load("Pictures/theHomepage.png").convert()
    name = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name)<29:
                        name += event.unicode
        

            screen.fill(black)
            screen.blit(page,(0,0))
            font = pygame.font.SysFont('Comic Sans MS', 25)
            text = font.render("" + name, True, black)
            screen.blit(text,(375,122))
            pygame.display.update()
            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] > 650 and event.pos[0] < 750 and event.pos[1] > 110 and event.pos[1] < 140:
                    page = pygame.image.load("Pictures/menu.png").convert()
                    screen.blit(page,(0,0))
            pygame.display.flip()

#To Do: Issues to be solved with buttons as buttons with overlapping co-ordinates trigger both events.
#I.E Clicking enter on the homepage may also trigger the join public game button on the next menu 
#May require use of new utilities or new programming language(s).
display()
