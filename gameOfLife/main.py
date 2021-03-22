import sys, pygame
from random import randint
import time
import math
import numpy as np

pygame.init()

size_w = 1000
size_h = 1000
cantidad = 100
size_rect = (size_h / cantidad)
color_rect = (125, 125 ,125)

bg = 0, 0, 0

#window
screen = pygame.display.set_mode((size_w, size_h))
pygame.display.set_caption("The game of life")

pause = False

states = []

for y in  range( 0, cantidad):
    row = []
    for x in range( 0, cantidad):
        state = randint(0, 1)
        row.append(state)
    states.append(row)

while 1:

    newStates = np.copy(states)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            pause = not pause
        
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            x, y =math.floor(posX/size_rect), math.floor(posY/size_rect)
            newStates[x][y] = not mouseClick[2]

    screen.fill(bg)
    
    #game
    for y in range( 0, cantidad):
        for x in range( 0, cantidad):

            if not pause:

                neighbour = states[(x - 1) % cantidad][(y - 1) % cantidad] + \
                            states[(x    ) % cantidad][(y - 1) % cantidad] + \
                            states[(x + 1) % cantidad][(y - 1) % cantidad] + \
                            states[(x - 1) % cantidad][(y    ) % cantidad] + \
                            states[(x + 1) % cantidad][(y    ) % cantidad] + \
                            states[(x - 1) % cantidad][(y + 1) % cantidad] + \
                            states[(x    ) % cantidad][(y + 1) % cantidad] + \
                            states[(x + 1) % cantidad][(y + 1) % cantidad]

                #come back to ife
                if  states[x][y] == 0 and neighbour == 3:
                    newStates[x][y] = 1
                               
                #to be die
                if states[x][y] == 1 and (neighbour < 2 or neighbour > 3):
                    newStates[x][y] = 0

            if newStates[x][y] == 1:
                pygame.draw.rect(screen, color_rect, (x * size_rect, y * size_rect, size_rect, size_rect), 1)
            else:
                pygame.draw.rect(screen, color_rect, (x * size_rect, y * size_rect, size_rect, size_rect), 0)

    states = np.copy(newStates)
    pygame.display.update()